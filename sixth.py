import sys
import requests
from lxml import html

#python sixth.py https://www.jcu.cz



def download_url_and_get_all_hrefs(url):
    """
    Stáhne obsah URL, zkontroluje stavový kód, a pokud je 200,
    vyhledá všechny absolutní odkazy v <a> elementech na stránce.
    """
    try:
        response = requests.get(url, timeout=10)
        if not response.ok:
            raise Exception(f"HTTP chyba: {response.status_code} na URL: {url}")

        # Parse HTML obsah
        root = html.fromstring(response.content)

        # Najít všechny absolutní odkazy
        hrefs = [href for href in root.xpath('//a/@href') if href.startswith('http')]
        return hrefs

    except requests.exceptions.RequestException as e:
        raise Exception(f"Chyba při stahování stránky: {e}")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Zadejte URL jako parametr.")

        url = sys.argv[1]
        print(f"Stahuji odkazy z URL: {url}")

        # Hlavní odkazy na první stránce
        all_hrefs = download_url_and_get_all_hrefs(url)
        print("Nalezené odkazy:")
        for href in all_hrefs:
            print(href)

        # Analýza podstránek:
        print("\nOdkazy z dalších stránek:")
        for href in all_hrefs[:5]:  # Omezíme na prvních 5 odkazů (pro ukázku)
            try:
                nested_hrefs = download_url_and_get_all_hrefs(href)
                print(f"\nOdkazy nalezené na {href}:")
                for nested_href in nested_hrefs:
                    print(nested_href)
            except Exception as nested_error:
                print(f"Chyba při analýze odkazu {href}: {nested_error}")

    except Exception as e:
        print(f"Program skončil chybou: {e}")

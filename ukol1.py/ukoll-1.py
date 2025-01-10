# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text a vypise ho pozpatku
# vytvorte funkce pozpatku(), ktera jako parametr bere text a vraci ho pozpatku tzn "ahoj" -> "joha"
# osetrete chybove stavy pomoci try - except
import sys

# def pozpatku(text):
#     text_pozpatku = ""
#     for pismeno in reversed(text):
#         text_pozpatku += pismeno
#     return text_pozpatku


def pozpatku(text):
    text_pozpatku = ""
    i = len(text) - 1
    while i >= 0:
        pismeno = text[i]
        text_pozpatku += pismeno
        i -= 1
    return text_pozpatku


if __name__ == "__main__":
    try:
        soubor = sys.argv[1]
        with open(soubor, "r") as fp:
            obsah = fp.read()
            obracene = pozpatku(obsah)
            print(obracene)
    except IndexError:
        print("Zadej nazev souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")

------------------------------------------------------------------------------------------------------------------------

import sys

def pozpatku(text):
    """Vrátí text obrácený pozpátku."""
    return text[::-1]  # Efektivnější než použití smyčky

if __name__ == "__main__":
    try:
        # Získání názvu souboru z příkazové řádky
        soubor = sys.argv[1]

        # Načtení obsahu souboru
        with open(soubor, "r", encoding="utf-8") as fp:
            obsah = fp.read()

            if not obsah.strip():  # Pokud je soubor prázdný
                print("Soubor je prázdný.")
            else:
                # Obrácení textu a výpis
                obracene = pozpatku(obsah)
                print(obracene)

    except IndexError:
        print("Zadejte název souboru jako argument z příkazové řádky.")
    except FileNotFoundError:
        print("Zadaný soubor neexistuje.")
    except Exception as e:
        print(f"Došlo k neočekávané chybě: {e}")

--------------------------------------------------------------------------------------------------------

import sys

def pozpatku(text):
    """
    Funkce přijímá text a vrací jej pozpátku.
    """
    return text[::-1]

if __name__ == "__main__":
    try:
        # Kontrola, zda byl zadán argument pro název souboru
        soubor = sys.argv[1]
        
        # Načtení obsahu souboru
        with open(soubor, "r", encoding="utf-8") as fp:
            obsah = fp.read()
        
        # Obrácení textu a jeho výpis
        obracene = pozpatku(obsah)
        print(obracene)
    
    except IndexError:
        # Chyba, pokud není zadán název souboru
        print("Chyba: Zadejte název souboru jako argument při spuštění programu.")
    
    except FileNotFoundError:
        # Chyba, pokud soubor neexistuje
        print(f"Chyba: Soubor '{sys.argv[1]}' neexistuje.")
    
    except Exception as e:
        # Obecná chyba
        print(f"Neočekávaná chyba: {e}")

#spustim python program.py textovy_soubor.txt
# -> vyjde těvš joha
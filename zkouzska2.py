# Příklad 3: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

#data z url - Stáhneme data z kurzovního lístku
#zpracovani obsahu - # Ověříme, že byl požadavek úspěšný     # Získáme textový obsah odpovědi     # Rozdělíme obsah na jednotlivé řádky
#nacteni kurzu a overenei kurzu -     # Prohledáme řádky, kde jsou uvedeny kurzy - # Přeskočíme první dva řádky (datum a hlavičku tabulky)  
# # Ujistíme se, že řádek má dostatek sloupců
#vypocet castky - # Získáme kód měny, množství a kurz             # Převedeme kurz a množství na čísla             # Vypočítáme výslednou částku v CZK
#vyjimka     # Pokud měna nebyla nalezena, vyhodíme výjimku

import requests

def convert_to_czk(amount, currency):
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    response = requests.get(url)
   
    if not response.ok:
        raise Exception("Nepovedlo se")

    data = response.text

    lines = data.splitlines()

    for line in lines[2:]: 
        fields = line.split('|')
        if len(fields) < 5:
            continue

        country, currency_name, amount_in_rate, code, rate = fields

        if code == currency:
            rate = float(rate.replace(',', '.'))
            amount_in_rate = int(amount_in_rate)

            result = amount * (rate / amount_in_rate)
            return round(result, 2)

    raise ValueError(f"Měna {currency} nebyla našlá")

# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."

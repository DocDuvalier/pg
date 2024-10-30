def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    typ = figurka["typ"]
    start = figurka["pozice"]
   
    # Kontrola platnosti cílové pozice (mimo šachovnici)
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
   
    # Kontrola, zda je cílová pozice volná
    if cilova_pozice in obsazene_pozice:
        return False

    # Výpočet rozdílu pozic pro snazší ověřování pravidel
    delta_row = cilova_pozice[0] - start[0]
    delta_col = cilova_pozice[1] - start[1]
   
    # Pravidla pro pohyb jednotlivých figur
    if typ == "pěšec":
        # Pohyb o jedno nebo dvě pole vpřed, pokud je výchozí pozice
        if delta_col == 0:
            if delta_row == 1:
                return cilova_pozice not in obsazene_pozice
            elif delta_row == 2 and start[0] == 2:
                return (start[0] + 1, start[1]) not in obsazene_pozice and cilova_pozice not in obsazene_pozice
        return False
   
    elif typ == "jezdec":
        # Pohyb ve tvaru "L"
        return (abs(delta_row), abs(delta_col)) in [(2, 1), (1, 2)]
   
    elif typ == "věž":
        # Horizontální nebo vertikální pohyb s kontrolou překážek
        if delta_row == 0:  # Pohyb ve sloupci
            step = 1 if delta_col > 0 else -1
            for col in range(start[1] + step, cilova_pozice[1], step):
                if (start[0], col) in obsazene_pozice:
                    return False
            return True
        elif delta_col == 0:  # Pohyb v řádku
            step = 1 if delta_row > 0 else -1
            for row in range(start[0] + step, cilova_pozice[0], step):
                if (row, start[1]) in obsazene_pozice:
                    return False
            return True
        return False
   
    elif typ == "střelec":
        # Diagonální pohyb s kontrolou překážek
        if abs(delta_row) == abs(delta_col):
            row_step = 1 if delta_row > 0 else -1
            col_step = 1 if delta_col > 0 else -1
            for i in range(1, abs(delta_row)):
                if (start[0] + i * row_step, start[1] + i * col_step) in obsazene_pozice:
                    return False
            return True
        return False
   
    elif typ == "dáma":
        # Kombinace věže a střelce
        if delta_row == 0 or delta_col == 0:  # Pohyb jako věž
            return je_tah_mozny({"typ": "věž", "pozice": start}, cilova_pozice, obsazene_pozice)
        elif abs(delta_row) == abs(delta_col):  # Pohyb jako střelec
            return je_tah_mozny({"typ": "střelec", "pozice": start}, cilova_pozice, obsazene_pozice)
        return False
   
    elif typ == "král":
        # Pohyb o jedno pole ve všech směrech
        return max(abs(delta_row), abs(delta_col)) == 1
    # Implementace pravidel pohybu pro různé figury zde.
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cislo = int(cislo)
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desítky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    desetazdvacet = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    if cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return desetazdvacet[cislo - 10]
    elif cislo < 100:
        desetiny = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return desítky[desetiny]
        else:
            return f"{desítky[desetiny]} {jednotky[jednotka]}"
    elif cislo == 100:
        return "sto"
    else:
        return "Číslo mimo rozsah"
    

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
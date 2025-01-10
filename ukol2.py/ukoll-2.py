# napiste funkci, ktera podle typu "+"", "-", "*", "/" provede operaci a vrati vysledek

def operace(typ, a, b):
    matematicka_operace = None
    if typ == "+":
        matematicka_operace = a + b
    elif typ == "-":
        matematicka_operace = a - b
    elif typ == "*":
        matematicka_operace = a * b
    elif typ == "/":
        matematicka_operace = a / b
    return matematicka_operace

if __name__ == "__main__":
    operace("+", 1, 2)  # 3
    operace("-", 2, 1)  # 1
    operace("*", 0, 5)  # 0
    operace("/", 4, 2)  # 2

----------------------------------------------------------------------------------------------------

def operace(typ, a, b):
    """
    Provede matematickou operaci mezi dvěma čísly na základě zadaného typu operace.
    
    :param typ: Typ operace, jeden z "+", "-", "*", "/".
    :param a: První číslo.
    :param b: Druhé číslo.
    :return: Výsledek operace.
    :raises ValueError: Pokud je typ operace neplatný.
    :raises ZeroDivisionError: Pokud dojde k pokusu o dělení nulou.
    """
    if typ == "+":
        return a + b
    elif typ == "-":
        return a - b
    elif typ == "*":
        return a * b
    elif typ == "/":
        if b == 0:
            raise ZeroDivisionError("Dělení nulou není povoleno.")
        return a / b
    else:
        raise ValueError(f"Neplatný typ operace: '{typ}'. Povolené typy jsou: '+', '-', '*', '/'.")

# Příklady použití
if __name__ == "__main__":
    # Testy operací
    print(operace("+", 1, 2))  # Výstup: 3
    print(operace("-", 2, 1))  # Výstup: 1
    print(operace("*", 0, 5))  # Výstup: 0
    print(operace("/", 4, 2))  # Výstup: 2

    # Test chybových stavů
    try:
        print(operace("/", 4, 0))  # Očekává chybu: ZeroDivisionError
    except ZeroDivisionError as e:
        print(e)

    try:
        print(operace("%", 4, 2))  # Očekává chybu: ValueError
    except ValueError as e:
        print(e)

-------------------------------------------------------------------------------------------------------------

def operace(typ, a, b):
    """
    Provádí matematickou operaci mezi dvěma čísly na základě zadaného typu.
    :param typ: Typ operace ('+', '-', '*', '/')
    :param a: První číslo
    :param b: Druhé číslo
    :return: Výsledek operace nebo chybová zpráva při neplatné operaci
    """
    try:
        if typ == "+":
            return a + b
        elif typ == "-":
            return a - b
        elif typ == "*":
            return a * b
        elif typ == "/":
            if b == 0:
                return "Chyba: Dělení nulou není povoleno."
            return a / b
        else:
            return "Chyba: Neplatný typ operace."
    except Exception as e:
        return f"Neočekávaná chyba: {e}"

if __name__ == "__main__":
    # Testy pro funkci operace
    print(operace("+", 1, 2))  # 3
    print(operace("-", 2, 1))  # 1
    print(operace("*", 0, 5))  # 0
    print(operace("/", 4, 2))  # 2
    print(operace("/", 4, 0))  # Chyba: Dělení nulou není povoleno.
    print(operace("x", 4, 2))  # Chyba: Neplatný typ operace.

# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # ZDE NAPIŠTE VÁŠ KÓD
    pass

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]

------------------------------------------------------------------------------------------------------

def process_numbers(numbers):
    # Inicializujeme prázdný seznam, kam budeme ukládat výsledky
    result = []
    
    # Iterujeme přes zadaný seznam čísel
    for num in numbers:
        # Pokud narazíme na číslo 10, ukončíme zpracování seznamu
        if num == 10:
            break
        # Pokud je číslo větší než 5, vynásobíme ho 2 a přidáme do výsledného seznamu
        if num > 5:
            result.append(num * 2)
    
    # Vrátíme výsledný seznam
    return result

----------------------------------------------------------------------------------------------------------

def process_numbers(numbers):
    """
    Zpracuje seznam celých čísel a vrátí nový seznam obsahující čísla větší než 5,
    vynásobená 2. Pokud seznam obsahuje číslo 10, zpracování se ukončí.
    """
    result = []
    for number in numbers:
        if number == 10:
            break
        if number > 5:
            result.append(number * 2)
    return result

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]

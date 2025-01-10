# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

import math

class Shape:
    #Abstraktní třída Shape, která definuje základní strukturu pro geometrické tvary.
    def area(self):
        #Abstraktní metoda, která bude implementována v podtřídách.
        #Abstraktní metoda, kterou musí implementovat všechny podtřídy.
        #Vrací plochu daného tvaru.
        return 0.0

class Rectangle(Shape):
    #Třída Rectangle reprezentuje obdélník.
    def __init__(self, width, height):
        #Inicializace atributů šířky a výšky.
        #Inicializace obdélníku se šířkou a výškou.
        self.width = width
        self.height = height

    def area(self):
        #Vypočítá plochu obdélníku: šířka * výška.
        #Vypočítá a vrátí plochu obdélníku (šířka × výška).
        return self.width * self.height

class Circle(Shape):
    #Třída Circle reprezentuje kruh.
    def __init__(self, radius):
        #Inicializace atributu poloměru.
        #Inicializace kruhu s poloměrem.
        self.radius = radius

    def area(self):
        #Vypočítá plochu kruhu: π * poloměr^2.
        #Vypočítá a vrátí plochu kruhu (π × poloměr²).
        return math.pi * (self.radius ** 2)


from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass
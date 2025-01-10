# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

    #Abstraktní třída Shape, která definuje základní strukturu pro geometrické tvary.
        #Abstraktní metoda, která bude implementována v podtřídách.
        #Abstraktní metoda, kterou musí implementovat všechny podtřídy.
        #Vrací plochu daného tvaru.
    #Třída Rectangle reprezentuje obdélník.
        #Inicializace atributů šířky a výšky.
        #Inicializace obdélníku se šířkou a výškou.
        #Vypočítá plochu obdélníku: šířka * výška.
        #Vypočítá a vrátí plochu obdélníku (šířka × výška).
    #Třída Circle reprezentuje kruh.
        #Inicializace atributu poloměru.
        #Inicializace kruhu s poloměrem.
    # pí krát radius na 2

import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
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
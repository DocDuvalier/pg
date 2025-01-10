# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# ZDE DOPLŇTE VLASTNÍ KÓD

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

-----------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
import math

# Abstraktní třída Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstraktní metoda pro výpočet plochy."""
        pass

# Třída Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        """Inicializace šířky a výšky obdélníku."""
        self.width = width
        self.height = height

    def area(self):
        """Výpočet plochy obdélníku."""
        return self.width * self.height

# Třída Circle
class Circle(Shape):
    def __init__(self, radius):
        """Inicializace poloměru kruhu."""
        self.radius = radius

    def area(self):
        """Výpočet plochy kruhu."""
        return math.pi * (self.radius ** 2)

------------------------------------------------------------------------------------

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstraktní třída Shape, která definuje základní strukturu pro geometrické tvary.
    """
    @abstractmethod
    def area(self):
        """
        Abstraktní metoda, kterou musí implementovat všechny podtřídy.
        Vrací plochu daného tvaru.
        """
        pass

class Rectangle(Shape):
    """
    Třída Rectangle reprezentuje obdélník.
    """
    def __init__(self, width, height):
        """
        Inicializace obdélníku se šířkou a výškou.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Vypočítá a vrátí plochu obdélníku (šířka × výška).
        """
        return self.width * self.height

class Circle(Shape):
    """
    Třída Circle reprezentuje kruh.
    """
    def __init__(self, radius):
        """
        Inicializace kruhu s poloměrem.
        """
        self.radius = radius

    def area(self):
        """
        Vypočítá a vrátí plochu kruhu (π × poloměr²).
        """
        return math.pi * (self.radius ** 2)

# Pytest testy pro Příklad 3
def test_shapes():
    """
    Testy pro ověření funkcionality tříd Rectangle a Circle.
    """
    rect = Rectangle(4, 5)
    assert rect.area() == 20  # Plocha obdélníku (4 × 5 = 20)

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3  # Plocha kruhu (π × 3² ≈ 28.3)

    # Test, že se nelze vytvořit instanci abstraktní třídy Shape
    try:
        shape = Shape()
    except TypeError:
        pass

class Osoba:
    def __init__(self, jmeno, vek) -> None:
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"


class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik) -> None:
        super().__init__(jmeno, vek)
        self.rocnik = rocnik
    
    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"


class Ucitel(Osoba):
    def __init__(self, jmeno, vek, obor) -> None:
        super().__init__(jmeno, vek)
        self.obor = obor
    
    def __str__(self) -> str:
        return f"Ucitel {self.jmeno} uci obor {self.obor}"


if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT")

    print(student1)
    print(student2)
    print(ucitel)

------------------------------------------------------------------------------------------------------

class Osoba:
    def __init__(self, jmeno, vek) -> None:
        if not isinstance(vek, int) or vek < 0:
            raise ValueError("Věk musí být nezáporné celé číslo.")
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"
    
    def __repr__(self) -> str:
        return f"Osoba(jmeno='{self.jmeno}', vek={self.vek})"


class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik) -> None:
        super().__init__(jmeno, vek)
        if not isinstance(rocnik, int) or rocnik <= 0:
            raise ValueError("Ročník musí být kladné celé číslo.")
        self.rocnik = rocnik
    
    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"
    
    def __repr__(self) -> str:
        return f"Student(jmeno='{self.jmeno}', vek={self.vek}, rocnik={self.rocnik})"


class Ucitel(Osoba):
    def __init__(self, jmeno, vek, obor) -> None:
        super().__init__(jmeno, vek)
        self.obor = obor
    
    def __str__(self) -> str:
        return f"Ucitel {self.jmeno} uci obor {self.obor}"
    
    def __repr__(self) -> str:
        return f"Ucitel(jmeno='{self.jmeno}', vek={self.vek}, obor='{self.obor}')"


if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT")

    print(student1)  # Výstup: Student Adam studuje 2 rocnik
    print(student2)  # Výstup: Student Eva studuje 1 rocnik
    print(ucitel)    # Výstup: Ucitel Tomas uci obor IT

    # Testování metod __repr__
    print(repr(student1))  # Výstup: Student(jmeno='Adam', vek=20, rocnik=2)
    print(repr(ucitel))    # Výstup: Ucitel(jmeno='Tomas', vek=40, obor='IT')

--------------------------------------------------------------------------------------------------------------------------------------------------

class Osoba:
    def __init__(self, jmeno: str, vek: int) -> None:
        """
        Inicializace základní třídy Osoba.
        :param jmeno: Jméno osoby
        :param vek: Věk osoby
        """
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, vek={self.vek})"


class Student(Osoba):
    def __init__(self, jmeno: str, vek: int, rocnik: int) -> None:
        """
        Inicializace třídy Student.
        :param jmeno: Jméno studenta
        :param vek: Věk studenta
        :param rocnik: Ročník, který student studuje
        """
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.rocnik} ročník"


class Ucitel(Osoba):
    def __init__(self, jmeno: str, vek: int, obor: str) -> None:
        """
        Inicializace třídy Učitel.
        :param jmeno: Jméno učitele
        :param vek: Věk učitele
        :param obor: Obor, který učitel vyučuje
        """
        super().__init__(jmeno, vek)
        self.obor = obor

    def __str__(self) -> str:
        return f"Učitel {self.jmeno} učí obor {self.obor}"


if __name__ == "__main__":
    # Vytvoření instancí tříd
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    ucitel = Ucitel("Tomas", 40, "IT")

    # Výpis instancí
    print(student1)
    print(student2)
    print(ucitel)

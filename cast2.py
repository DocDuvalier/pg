def zacatek_while(): 
    print("začátek")

    i = 0

    while i<5:
        print("o")
        i += 1
        
    print("Konec")

def zacatek_for():
    print ("zacatek")

    for i in range(5):
        print("o", i)

    print("konec")

def in_range(min_number, max_number, number):
    print("is in range")
    print("is not in range")

in_range(100, 1000, 2000)
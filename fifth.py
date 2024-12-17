import sys

#program by měl být spustitelný voláním: python fifth.py cesta/k/obrazku.jpg

jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'

def read_header(file_name, header_length):
    """
    Načte prvních 'header_length' bytů ze souboru 'file_name'.
    Vrátí načtené byty, nebo vyvolá výjimku při chybě.
    """
    try:
        with open(file_name, 'rb') as file:
            return file.read(header_length)
    except FileNotFoundError:
        raise FileNotFoundError(f"Soubor {file_name} neexistuje.")
    except Exception as e:
        raise Exception(f"Chyba při čtení souboru {file_name}: {e}")

def is_jpeg(file_name):
    """
    Zkontroluje, zda je soubor typu JPEG porovnáním jeho hlavičky s definovanou hlavičkou JPEG.
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header

def is_gif(file_name):
    """
    Zkontroluje, zda je soubor typu GIF porovnáním jeho hlavičky s definovanými hlavičkami GIF.
    """
    header = read_header(file_name, max(len(gif_header1), len(gif_header2)))
    return header.startswith(gif_header1) or header.startswith(gif_header2)

def is_png(file_name):
    """
    Zkontroluje, zda je soubor typu PNG porovnáním jeho hlavičky s definovanou hlavičkou PNG.
    """
    header = read_header(file_name, len(png_header))
    return header == png_header

def print_file_type(file_name):
    """
    Vypíše typ souboru na základě jeho hlavičky. Pokud typ není rozpoznán, vypíše 'neznámý typ'.
    """
    if is_jpeg(file_name):
        print(f"Soubor {file_name} je typu JPEG.")
    elif is_gif(file_name):
        print(f"Soubor {file_name} je typu GIF.")
    elif is_png(file_name):
        print(f"Soubor {file_name} je typu PNG.")
    else:
        print(f"Soubor {file_name} je neznámého typu.")

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise IndexError("Zadejte název souboru jako argument příkazové řádky.")
        
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError as e:
        print(f"Chyba: {e}")
    except FileNotFoundError as e:
        print(f"Chyba: {e}")
    except Exception as e:
        print(f"Vyskytla se chyba: {e}")

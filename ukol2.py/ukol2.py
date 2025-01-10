# Příklad 2: Práce s externími knihovnami a soubory
# Zadání:
# Napište funkci `fetch_and_save_data`, která:
# 1. Načte data z URL (https://jsonplaceholder.typicode.com/posts).
# 2. Do staženého json souboru přidá klíč `userName` s hodnotou jména uživatele podle klíče `userId` z URL (např. 1 -> "Leanne Graham").
# 3. Data uloží do souboru `data.json` ve formátu JSON.
# Použijte knihovny `requests` a `json`.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    # ZDE NAPIŠTE VÁŠ KÓD
    pass

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    try:
        # 1. Načtení dat z URL
        response = requests.get(url)
        response.raise_for_status()  # Ověří, zda byla odpověď úspěšná
        
        # Převod staženého JSON na Python seznam/dictionary
        data = response.json()

        # 2. Přidání klíče `userName` podle `userId`
        for item in data:
            user_id = item.get("userId")
            item["userName"] = user_names.get(user_id, "Unknown User")  # Výchozí hodnota je "Unknown User", pokud `userId` není ve slovníku

        # 3. Uložení dat do souboru `data.json` ve formátu JSON
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return True  # Funkce se provedla úspěšně
    except Exception as e:
        print(f"Došlo k chybě: {e}")
        return False  # Pokud dojde k chybě, vrátíme `False`

-------------------------------------------------------------------------------------------------------------

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data():
    """
    Načte data z URL, přidá klíč `userName` podle `userId` a uloží data do souboru `data.json`.
    """
    try:
        # 1. Načtení dat z URL
        response = requests.get(url)
        response.raise_for_status()  # Vyvolá chybu, pokud není status 200
        data = response.json()  # Převod odpovědi na JSON

        # 2. Přidání klíče `userName`
        for item in data:
            user_id = item.get("userId")
            item["userName"] = user_names.get(user_id, "Unknown")  # Přidáme uživatelské jméno nebo "Unknown"

        # 3. Uložení dat do souboru
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)  # Formátujeme a ukládáme JSON

        return True  # Indikace úspěšného dokončení

    except requests.RequestException as e:
        print(f"Chyba při načítání dat: {e}")
        return False
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")
        return False

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])

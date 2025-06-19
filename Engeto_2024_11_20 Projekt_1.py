# projekt_1.py: první projekt do Engeto Online Python Akademie
# author : Ing. Pavel Mrkva
# email: pavel.mrkva@seznam.cz

# VSTUPPNI UDAJE


TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.""",
]

user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]

# RESENI
# 1. cast - mnozstvi slov

import string
import sys

if __name__ == "__main__":

    jmeno = input("Enter user name:")  # kontrola uzivatele
    heslo = input("Enter password:")

    if jmeno not in user:
        print("Unregistered user.", "\nEnd.")
        sys.exit()  # Pokud spatne jmeno.
    index = user.index(jmeno)  # kontrola hesla
    if password[index] != heslo:
        print("Wrong password.Log in again.", "\nEnd.")
        sys.exit()  # Pokud spatne heslo.
    else:
        print("Welcome to the app", jmeno, ".")
        print(20 * "=")
        print("We have 3 texts to be analyzed.")
        print(20 * "_")
    attempts = 3  # vyber vety uzivatelem - 3 pokusy
    while attempts > 0:
        veta_i = input("Enter text Nr. 1 or 2 or 3: ")
        if veta_i in {"1", "2", "3"}:
            break
        attempts -= 1
        print(
            f"Wrong Nr. chosen. There are still {attempts} left.\n{20 * "_"}"
        )
    else:
        print("Wrong entry three times.\nEnd.")
        sys.exit()  # pokud 3x spatna volba vety
    print(f"Text Nr. {veta_i} is chosen:")
    veta = TEXTS[int(veta_i) - 1]  # vyber vety pomoci indexu
    print(veta)
    print(20 * "_")
    print(" ")

    translator = str.maketrans(
        "", "", string.punctuation
    )  # metoda odstraneni interpunkce
    veta_t = veta.translate(translator)  # veta bez interpunkce
    veta_s = veta_t.split()
    results_1 = {
        "pocet_slov": 0,
        "start_velka_pismena": 0,
        "velka_pismena": 0,
        "mala_pismena": 0,
        "pocet_cisel": 0,
        "suma_cisel": 0,
    }
    results_1["pocet_slov"] = len(veta_s)
    for slovo in veta_s:
        slovo_s = slovo.split()  # slova rozdelena na znaky
        if slovo_s[0].istitle():  # pokud 1. znak je velke pismeno
            results_1["start_velka_pismena"] += 1
        if slovo.isupper() and slovo.isalpha():
            results_1["velka_pismena"] += 1
        if slovo.islower():
            results_1["mala_pismena"] += 1
        if slovo.isdigit():
            results_1["pocet_cisel"] += 1
        if slovo.isdigit():
            results_1["suma_cisel"] = results_1["suma_cisel"] + int(slovo)
    print(
        "There are",
        results_1["pocet_slov"],
        "words in the selected text.",
    )
    print(
        "There are",
        results_1["start_velka_pismena"],
        "titlecase words.",
    )
    print("There are", results_1["velka_pismena"], "uppercase words.")
    print("There are", results_1["mala_pismena"], "lowercase words.")
    print("There are", results_1["pocet_cisel"], "numeric strings.")
    print(
        "The sum of all the numbers is ",
        results_1["suma_cisel"],
        ".",
    )
    # 2. cast - delky slov

    delky_slov = {}  # slovnik {delky_slov:vyskyt}
    for slovo in veta_s:
        delky_slov[len(slovo)] = delky_slov.get(len(slovo), 0) + 1
    keys = delky_slov.keys()
    sorted_keys = sorted(keys)  # serazeni klicu od nejmensiho k nejvetsimu
    values = delky_slov.values()
    nejdelsi_slovo = max(values)
    print(" ")
    print((int(nejdelsi_slovo) + 5 + 5 + 8 + 2) * "-")
    print(f"{"LEN":>5}|{"OCCURENCES":^{int(nejdelsi_slovo) + 8}}|{"NR.":<4}")
    print((int(nejdelsi_slovo) + 5 + 5 + 8 + 2) * "-")
    delky_slov_sorted = (
        {}
    )  # novy slovnik {delky_slov:vyskyt} serazeny podle klicu, tj. podle delky slov
    for key in sorted_keys:
        delky_slov_sorted[key] = delky_slov[key]
    for key, vyskyt in delky_slov_sorted.items():
        print(
            f"{key:>5}|{('*' * int(vyskyt)):<{int(nejdelsi_slovo) + 8}}|{vyskyt}"
        )
    print(
        "\nNote:"
        + "\n  LEN.............word length"
        + "\n  OCCURANCES......number of words of a given length (graphic representation)"
        + "\n  NR..............number of words of a given lenght"
    )  # vysvetlivky

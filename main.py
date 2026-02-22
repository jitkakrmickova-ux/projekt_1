# registrovaní uživatelé
USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass456"
}

# vyžádání jména a hesla
username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")

# kontrola správné dvojice
if USERS.get(username) == password:
    print(f"Ahoj {username}, vítej v aplikaci!")
else:
    print("Uživatelské jméno nebo heslo nejsou správné. Program se ukončuje.")
    quit()

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
print("-" * 40)
print("Máme k dispozici 3 texty k analýze.")
print("-" * 40)

choice = input("Vyber číslo textu (1–3): ")

# kontrola, zda uživatel zadal platné číslo
if not choice.isdigit() or int(choice) not in range(1, 4):
    print("Neplatná volba. Program se ukončuje.")
    quit()

# převod na index (0, 1, 2)
selected_text = TEXTS[int(choice) - 1]
# rozdělení textu na slova
words = selected_text.split()

# očištění slov od interpunkce
clean_words = [word.strip(".,!?;:") for word in words]

# počítání kategorií
total_words = len(clean_words)
titlecase_words = sum(1 for w in clean_words if w.istitle())
uppercase_words = sum(1 for w in clean_words if w.isupper() and w.isalpha())
lowercase_words = sum(1 for w in clean_words if w.islower())
numeric_strings = [w for w in clean_words if w.isdigit()]
sum_numbers = sum(int(n) for n in numeric_strings)

# výpis výsledků
print("-" * 40)
print(f"Počet slov: {total_words}")
print(f"Slova začínající velkým písmenem: {titlecase_words}")
print(f"Slova psaná velkými písmeny: {uppercase_words}")
print(f"Slova psaná malými písmeny: {lowercase_words}")
print(f"Počet čísel: {len(numeric_strings)}")
print(f"Součet všech čísel: {sum_numbers}")
print("-" * 40)
# graf četnosti délek slov
lengths = {}

for word in clean_words:
    length = len(word)
    lengths[length] = lengths.get(length, 0) + 1

print("DÉLKY SLOV:")
print("-" * 40)

for length in sorted(lengths):
    count = lengths[length]
    print(f"{length:>2} | {'*' * count} {count}")


# week3_search.py
slots = [
    [1, "EV", "Free"],
    [2, "Regular", "Occupied"],
    [3, "EV", "Occupied"]
]

print("1. Search by ID\n2. Search by Type")
ch = int(input("Choice: "))

if ch == 1:
    sid = int(input("Enter ID: "))
    found = False
    for s in slots:
        if s[0] == sid:
            print("Found:", s)
            found = True
    if not found:
        print("Not Found")

elif ch == 2:
    stype = input("Enter Type: ").lower()
    for s in slots:
        if s[1].lower() == stype:
            print(s)
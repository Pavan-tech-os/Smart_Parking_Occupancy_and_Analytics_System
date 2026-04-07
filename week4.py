# week4_functions.py
slots = []

def add_slot():
    sid = int(input("ID: "))
    stype = input("Type: ")
    status = input("Status: ")
    slots.append([sid, stype, status])
    print("Added")

def view_slots():
    for s in slots:
        print(s)

def search_slot():
    sid = int(input("Enter ID: "))
    for s in slots:
        if s[0] == sid:
            print("Found:", s)

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        add_slot()
    elif ch == 2:
        view_slots()
    elif ch == 3:
        search_slot()
    elif ch == 4:
        break
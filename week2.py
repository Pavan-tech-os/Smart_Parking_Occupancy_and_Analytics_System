# week2_menu.py
slots = []

while True:
    print("\n1. Add Slot\n2. View Slots\n3. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        sid = int(input("Enter Slot ID: "))
        stype = input("Enter Type: ")
        status = input("Enter Status: ")

        slots.append([sid, stype, status])
        print("Slot Added!")

    elif ch == 2:
        print("\n--- All Slots ---")
        for s in slots:
            print(f"ID:{s[0]}, Type:{s[1]}, Status:{s[2]}")

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
# week8_exception.py

from parking import *

p = ParkingLot()

while True:
    print("\n1.Add 2.View 3.Exit")

    try:
        ch = int(input("Enter choice: "))

        if ch == 1:
            sid = int(input("Enter ID: "))
            stype = input("Enter Type: ")
            p.add(Slot(sid, stype))
            print("Slot Added")

        elif ch == 2:
            p.view()

        elif ch == 3:
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Invalid Input! Enter numbers only.")

    except Exception as e:
        print("Error:", e)
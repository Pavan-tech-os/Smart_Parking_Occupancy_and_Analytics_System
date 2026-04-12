# week12.py

from parking import *
from storage import save_data, load_data  #FIXED IMPORT
from week9 import occupancy  # optional (if file exists)
from week10 import report  # optional
from week11 import graphs  # optional

p = ParkingLot()

# 🔹 Load previous data
p.slots = load_data()

while True:
    print("\n1.Add \n2.View \n3.Park \n4.Leave \n5.Stats \n6.Report \n7.Graph \n8.Exit.\n")

    ch = input("Enter choice: ")

    # 🔹 Add Slot
    if ch == '1':
        try:
            sid = int(input("Enter ID: "))
            stype = input("Enter Type: ")
            p.add_slot(sid, stype)
        except:
            print("Invalid Input")

    # 🔹 View Slots
    elif ch == '2':
        p.view_slots()

    # 🔹 Park Vehicle
    elif ch == '3':
        stype = input("Enter Type: ")
        p.allocate(stype)

    # 🔹 Leave Vehicle (Time Calculation)
    elif ch == '4':
        try:
            sid = int(input("Enter ID: "))
            p.release(sid)
        except:
            print("Invalid ID")

    # 🔹 Stats (NumPy)
    elif ch == '5':
        try:
            occupancy(p.slots)
        except:
            print("Stats module not found")

    # 🔹 Report (Pandas)
    elif ch == '6':
        try:
            report(p.slots)
        except:
            print("Report module not found")

    # 🔹 Graphs (Matplotlib)
    elif ch == '7':
        try:
            graphs(p.slots)
        except:
            print("Graph module not found")

    # 🔹 Exit
    elif ch == '8':
        save_data(p.slots)
        print("Data Saved. Exiting...")
        break

    else:
        print("Invalid Choice")
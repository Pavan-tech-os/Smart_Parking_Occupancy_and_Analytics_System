# Smart Parking System (SPAOAS)

import csv
import pandas as pd
import matplotlib.pyplot as plt


# 🔹 Slot Class
class Slot:
    def __init__(self, sid, stype, status):
        self.sid = sid
        self.stype = stype
        self.status = status


# 🔹 Parking Class
class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)
        print("Slot Added")

    def view_slots(self):
        print("\n--- Parking Slots ---")
        for s in self.slots:
            print(f"ID:{s.sid}, Type:{s.stype}, Status:{s.status}")

    def update_slot(self, sid, status):
        for s in self.slots:
            if s.sid == sid:
                s.status = status
                print("Updated Successfully")
                return
        print("Slot Not Found")

    def allocate_slot(self, stype):
        for s in self.slots:
            if s.stype == stype and s.status == "Free":
                s.status = "Occupied"
                print("Allocated Slot:", s.sid)
                return
        print("No Slot Available")


# 🔹 Save to CSV
def save_data(slots):
    with open("slots.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Type", "Status"])
        for s in slots:
            writer.writerow([s.sid, s.stype, s.status])


# 🔹 Load from CSV
def load_data():
    slots = []
    try:
        with open("slots.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                slots.append(Slot(int(row[0]), row[1], row[2]))
    except:
        pass
    return slots


# 🔹 Pandas Report
def generate_report(slots):
    df = pd.DataFrame({
        "ID": [s.sid for s in slots],
        "Type": [s.stype for s in slots],
        "Status": [s.status for s in slots]
    })

    print("\n--- Report ---")
    print(df)

    print("\n--- Slot Type Count ---")
    print(df["Type"].value_counts())


# 🔹 Graphs using Matplotlib
def show_graph(slots):
    df = pd.DataFrame({
        "Status": [s.status for s in slots],
        "Type": [s.stype for s in slots]
    })

    # Bar Chart
    status_count = df["Status"].value_counts()
    plt.figure()
    status_count.plot(kind="bar")
    plt.title("Parking Status (Bar Chart)")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()

    # Pie Chart
    plt.figure()
    status_count.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Parking Occupancy (Pie Chart)")
    plt.ylabel("")
    plt.show()


# 🔹 MAIN PROGRAM
parking = ParkingLot()

# Load previous data
parking.slots = load_data()

while True:
    print("\n1.Add 2.View 3.Update 4.Allocate 5.Report 6.Graph 7.Save & Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        sid = int(input("Enter ID: "))
        stype = input("Enter Type: ")
        status = input("Enter Status: ")
        parking.add_slot(Slot(sid, stype, status))

    elif ch == '2':
        parking.view_slots()

    elif ch == '3':
        sid = int(input("Enter ID: "))
        status = input("Enter New Status: ")
        parking.update_slot(sid, status)

    elif ch == '4':
        stype = input("Enter Type: ")
        parking.allocate_slot(stype)

    elif ch == '5':
        generate_report(parking.slots)

    elif ch == '6':
        show_graph(parking.slots)

    elif ch == '7':
        save_data(parking.slots)
        print("Data Saved Successfully")
        break

    else:
        print("Invalid Choice")
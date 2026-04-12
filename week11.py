# week11.py

import matplotlib.pyplot as plt

def graphs(slots):
    free = sum(1 for s in slots if s.status == "Free")
    occ = sum(1 for s in slots if s.status == "Occupied")

    # 🔹 Bar Graph
    plt.figure()
    plt.bar(["Free", "Occupied"], [free, occ])
    plt.title("Parking Status")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()

    # 🔹 Pie Chart
    plt.figure()
    plt.pie([free, occ], labels=["Free", "Occupied"], autopct="%1.1f%%")
    plt.title("Occupancy Distribution")
    plt.show()
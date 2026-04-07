# week11_chart.py
import matplotlib.pyplot as plt

free = 4
occupied = 6

plt.bar(["Free","Occupied"], [free, occupied])
plt.title("Parking Status")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()
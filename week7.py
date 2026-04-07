# week7_file.py
import csv

slots = [[1,"EV","Free"], [2,"Regular","Occupied"]]

# write
with open("slots.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID","Type","Status"])
    writer.writerows(slots)

# read
print("\nFrom File:")
with open("slots.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
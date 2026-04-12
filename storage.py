# storage.py

import csv
from parking import Slot   # import class

# 🔹 Save data to CSV
def save_data(slots):
    try:
        with open("slots.csv", "w", newline="") as f:
            writer = csv.writer(f)

            # header
            writer.writerow(["ID", "Type", "Status"])

            for s in slots:
                writer.writerow([s.sid, s.stype, s.status])

        print("Data Saved Successfully")

    except Exception as e:
        print("Error while saving:", e)


# 🔹 Load data from CSV
def load_data():
    slots = []

    try:
        with open("slots.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header

            for row in reader:
                sid = int(row[0])
                stype = row[1]
                status = row[2]

                s = Slot(sid, stype)
                s.status = status

                slots.append(s)

    except FileNotFoundError:
        print("No previous data found")

    except Exception as e:
        print("Error while loading:", e)

    return slots
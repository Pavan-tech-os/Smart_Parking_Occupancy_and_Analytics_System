# week5_dict.py
slots = []
logs = []

slot = {
    "id": 101,
    "type": "EV",
    "status": "Free"
}

slots.append(slot)

# update status
slot["status"] = "Occupied"
logs.append((101, "Occupied", "10:30 AM"))

print("\nSlots:")
for s in slots:
    print(s)

print("\nLogs:")
for log in logs:
    print(log)
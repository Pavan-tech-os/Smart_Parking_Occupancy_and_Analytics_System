# week12_final.py
slots = [
    {"id":1,"type":"EV","status":"Free"},
    {"id":2,"type":"Regular","status":"Occupied"}
]

for s in slots:
    print(f"ID:{s['id']} Type:{s['type']} Status:{s['status']}")

# simple allocation
for s in slots:
    if s["status"] == "Free":
        print("\nAllocated Slot:", s["id"])
        break
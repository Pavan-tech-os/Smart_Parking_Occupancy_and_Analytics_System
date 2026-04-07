# week1_basic_slot.py
slot_id = int(input("Enter Slot ID: "))

if slot_id <= 0:
    print("Invalid Slot ID")
else:
    slot_type = input("Enter Slot Type (Regular/EV/Accessible): ")
    status = input("Enter Status (Free/Occupied): ")

    print("\n--- Slot Details ---")
    print(f"Slot ID   : {slot_id}")
    print(f"Type      : {slot_type}")
    print(f"Status    : {status}")
# week6_oop.py
class Slot:
    def __init__(self, sid, stype, status):
        self.sid = sid
        self.stype = stype
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display(self):
        print(self.sid, self.stype, self.status)


class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, slot):
        self.slots.append(slot)

    def view_slots(self):
        for s in self.slots:
            s.display()


p = ParkingLot()
s1 = Slot(1, "EV", "Free")

p.add_slot(s1)
p.view_slots()
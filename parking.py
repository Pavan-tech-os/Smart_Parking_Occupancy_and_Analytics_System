# parking.py

import time

# Slot Class
class Slot:
    def __init__(self, sid, stype):
        self.sid = sid
        self.stype = stype
        self.status = "Free"
        self.start_time = None

    def park(self):
        self.status = "Occupied"
        self.start_time = time.time()

    def leave(self):
        if self.start_time:
            duration = time.time() - self.start_time
            self.status = "Free"
            self.start_time = None
            return duration
        return 0


# ParkingLot Class
class ParkingLot:
    def __init__(self):
        self.slots = []

    def add_slot(self, sid, stype):
        self.slots.append(Slot(sid, stype))
        print("Slot Added")

    def view_slots(self):
        for s in self.slots:
            print(s.sid, s.stype, s.status)

    def allocate(self, stype):
        for s in self.slots:
            if s.stype == stype and s.status == "Free":
                s.park()
                print("Allocated Slot:", s.sid)
                return
        print("No Slot Available")

    def release(self, sid):
        for s in self.slots:
            if s.sid == sid:
                t = s.leave()
                print("Time Parked:", round(t,2), "seconds")
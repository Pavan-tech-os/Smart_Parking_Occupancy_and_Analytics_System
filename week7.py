# storage.py
import csv

def save(slots):
    with open("slots.csv","w",newline="") as f:
        w = csv.writer(f)
        for s in slots:
            w.writerow([s.sid, s.stype, s.status])

def load():
    from parking import Slot
    slots = []
    try:
        with open("slots.csv") as f:
            r = csv.reader(f)
            for row in r:
                s = Slot(int(row[0]), row[1])
                s.status = row[2]
                slots.append(s)
    except:
        pass
    return slots
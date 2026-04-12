# week9_numpy.py

import numpy as np

def occupancy(slots):
    data = []

    for s in slots:
        if s.status == "Occupied":
            data.append(1)
        else:
            data.append(0)

    arr = np.array(data)

    print("Total Slots:", len(arr))
    print("Occupied:", np.sum(arr))
    print("Free:", len(arr) - np.sum(arr))
    print("Occupancy %:", (np.sum(arr)/len(arr))*100)
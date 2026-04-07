# week9_numpy.py
import numpy as np

# 1 = occupied, 0 = free
slots = np.array([1,0,1,1,0,0,1])

total = len(slots)
occupied = np.sum(slots)
free = total - occupied

print("Total:", total)
print("Occupied:", occupied)
print("Free:", free)
print("Occupancy %:", (occupied/total)*100)
# week10_pandas.py
import pandas as pd

data = {
    "ID":[1,2,3],
    "Type":["EV","Regular","EV"],
    "Status":["Free","Occupied","Occupied"]
}

df = pd.DataFrame(data)

print("\nAll Data:")
print(df)

print("\nOccupied Slots:")
print(df[df["Status"]=="Occupied"])
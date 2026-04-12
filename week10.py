# week10_pandas.py

import pandas as pd

def report(slots):
    data = {
        "ID": [s.sid for s in slots],
        "Type": [s.stype for s in slots],
        "Status": [s.status for s in slots]
    }

    df = pd.DataFrame(data)

    print("\n--- Full Report ---")
    print(df)

    print("\n--- Slot Type Count ---")
    print(df["Type"].value_counts())
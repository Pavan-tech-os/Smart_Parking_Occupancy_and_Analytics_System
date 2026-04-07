# week8_exception.py
try:
    sid = int(input("Enter Slot ID: "))
    if sid <= 0:
        raise ValueError

    print("Valid ID:", sid)

except ValueError:
    print("Invalid ID! Must be positive number")

except:
    print("Error occurred")
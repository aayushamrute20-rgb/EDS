from datetime import datetime
by = int(input("Enter the Birth year: "))
cy = datetime.now().year
age = cy-by
print(f"You are {age} years old.")

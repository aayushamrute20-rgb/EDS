A = int(input("Enter First no: "))
S = int(input("Enter Second no: "))
M = int(input("Enter Third no: "))
if A>S and A>M:
    print(f"{A} is max.")
elif S>A and S>M:
    print(f"{S} is max.")
else:
    print(f"{M} is max.")
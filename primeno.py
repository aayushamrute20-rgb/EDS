n = int(input("Enter the num: "))
k=0
for i in range(2,n):
    if n%i == 0:
        k+=1
if k == 0:
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is not a Prime number.")
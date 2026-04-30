P = list(map(int,input("Enter the Numbers: ").split( )))
e = []
o = []
for i in P:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e)
print("len of even list: ",len(e))
print(o)
print("len of odd list: ",len(o))
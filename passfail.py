#Pass/Fail
def res(marks,cr):
    K = sum(M)
    per = (K/(cr*100))*100
    if r == "Fail":
        return r 
    elif 40<=per<50:
        print(f"{per:.2f}")
        return "Third Division"
    elif 50<=per<60:
        print(f"{per:.2f}")
        return "Second Division"
    elif 60<=per<75:
        print(f"{per:.2f}")
        return "First Division"
    elif per>=75:
        print(f"{per:.2f}")
        return "Distinction"

cr = int(input("Enter the no of courses: "))
M = list(map(int,input("Enter the Marks: ").split( )))
r = ""
if any(p<40 for p in M):
    r = "Fail"
print(res(M,cr))

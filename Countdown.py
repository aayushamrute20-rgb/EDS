import time as t
k = int(input("Enter time in seconds for Countdown: "))
for i in range(k, 0, -1):
    secs = i % 60
    mins = int(i/60) % 60
    hrs = int(i/3600)
    print(f"{hrs:02}:{mins:02}:{secs:02}")
    t.sleep(1)
print("Time's Up")
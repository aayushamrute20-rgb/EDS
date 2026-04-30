#Shopping Cart Program
foods = []
price = [3, 4 ,6, 1, 2]
prc = []
d = {}
def distribute(p, numbers):
    counts = [0] * len(numbers)
    while p > 0:
        for i, num in enumerate(numbers):
            if p >= num:
                p -= num
                counts[i] += 1
            else:
                return counts, p
    
    return counts, p

while True:
    food = input("Add food to cart(q to Quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
foods.sort()

for i in range(len(foods)):
        d[price[i]] = foods[i]
        prc.append(price[i])
prc.sort(reverse = True)

budg = int(input("Set your Budget: $"))
print()
items,left = distribute(budg, prc)
print(f"-----Your Cart(with respective price)-----\n{d}\n")
print("This budget will get you: ")
for ll in range(len(prc)):
    print(f"{items[ll]} : {foods[ll]}")
print(f"Money Left: ${left}")
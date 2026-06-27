# To add key and values in dictionary
fruits = ["Apple", "Banana", "Cherry"]
counts = [10, 5, 20]

basket = {}

for i in range(len(fruits)):
    basket[fruits[i]] = counts[i]

print(basket)

#Frequency Counter
orders = ["S", "M", "L", "M", "S", "M", "M", "L"]
inventory = {}
for sizes in orders:
    if sizes in inventory:
        inventory[sizes] = inventory[sizes] + 1
    else:
        inventory[sizes] = 1

print(inventory)

# dup detector
arr=[4,7,1,4,8,7]
bt={}
for num in arr:
    if num in bt:
        print("True")
        break
    else:
        bt[num]= 1
arr=[4,7,1,4,8,7]
dt={}
for num in arr:
    if num in dt:
        dt[num]= dt [num] + 1
        if dt[num] > 1:
            print(f"{num} has a duplicate")
        else:
            print("no duplicates")
    else:
        dt[num] = 1

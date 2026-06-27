# Create Dictionary
mp = {}

# Insert
mp["Name"] = "Duzzy"
mp["Age"] = 22

# Access
print(mp["Name"])

# Update
mp["Age"] = 23

# Check Key
if "Age" in mp:
    print("Found")

# Loop Through Dictionary
for key, value in mp.items():
    print(key, value)

# Frequency Counter Pattern
arr = [2,1,2,3,1,5,2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)

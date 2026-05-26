# solution.py
# Q1 Frequency Count

arr = [1,1,2]

d = {}

for i in arr:

    if i in d:
        d[i] += 1

    else:
        d[i] = 1

print(d)

# Q2 Duplicate Detection

arr = [1,2,3,1]

s = set()

for i in arr:

    if i in s:
        print("Duplicate Found")
        break

    s.add(i)

# Q3 First Duplicate Element

arr = [5,1,2,3,2,1]

s = set()

for i in arr:

    if i in s:
        print(i)
        break

    s.add(i)

# Q4 Count Unique Elements

arr = [1,1,2,3,3,4]

s = set()

count = 0

for i in arr:

    if i not in s:

        s.add(i)

        count += 1

print(count)


# Q5 Highest Frequency Value

arr = [1,1,1,2,2,3]

d = {}

for i in arr:

    if i in d:
        d[i] += 1

    else:
        d[i] = 1

print(max(d.values()))


# Q6 Element with Highest Frequency

arr = [1,1,1,2,2,3]

d = {}

for i in arr:

    if i in d:
        d[i] += 1

    else:
        d[i] = 1

print(max(d, key=d.get))


# Q7 Character Frequency

s = "aaabbc"

d = {}

for ch in s:

    if ch in d:
        d[ch] += 1

    else:
        d[ch] = 1

print(d)

# Q8 Most Frequent Character

s = "aaabbc"

d = {}

for ch in s:

    if ch in d:
        d[ch] += 1

    else:
        d[ch] = 1

print(max(d, key=d.get))

# Q9 Common Element Between Two Arrays

a = [1,2,3,4]

b = [6,7,3,9]

s = set(a)

for i in b:

    if i in s:
        print(True)
        break

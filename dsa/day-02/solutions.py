#To print a name n times
name= input("enter your name:")
n = int(input("Enter how many times you want to get it printed."))
def pnn(name,n):
    if n==0:
        return
    print(name)
    pnn(name,n-1)

pnn(name,n)

#To print 1 to N
n =int(input("Enter the value of n: "))
def on(n):
    if n==0:
        return
    on(n-1)
    print(n,end=" ")

on(n)

#To print N to 1 
n=int(input("Enter the value of n: "))
def no(n):
    if n==0:
        return
    print(n,end=" ")
    no(n-1)

no(n)

# sum of first n number
n= int(input("Enter the number N:"))
def son(n):
    if n==0: 
        return 0
    a = n + son(n-1)
    return a

son(n)

# sum of first n number
n= int(input("Enter the number N:"))
def son(n):
    if n==0: 
        return 1
    a = n * son(n-1)
    return a

son(n)

# reverse an array
arr = list(map(int, input().split()))
n = len(arr)

def ran(i, arr):
    if i >= n//2:
        return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    ran(i+1, arr)

ran(0, arr)

#fibonacci series
def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

n = int(input())

for i in range(n):
    print(fib(i), end=" ")

arr = [5,1,3,2]
n = 5

def missing(arr):
    total = n * (n+1)/2
    m = 0 
    for i in range(len(arr)):
        m = arr[i] + m
    a = total - m
    return a

missing(arr)

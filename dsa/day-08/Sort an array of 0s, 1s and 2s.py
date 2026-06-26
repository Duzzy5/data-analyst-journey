arr = [2, 0, 2, 1, 1, 0]

def sort(arr):
    crr=[]
    z=0
    o=0
    t=0
    j=0
    k=0
    l=0
    for i in range(len(arr)):
        if arr[i]==0:
            z=z+1
        
        elif arr[i]==1 :
            o=o+1
        
        elif arr[i]==2:
            t=t+1
        else:
            pass
    
    while j<z:
        crr.append(0)
        j=j+1
    while k<o:
        crr.append(1)
        k=k+1
    while l<t:
        crr.append(2)
        l=l+1
    return crr

sort(arr)

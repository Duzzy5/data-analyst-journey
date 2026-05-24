#square
n = int(input("enter the number of units whose square you want form"))
def sq(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
sq(n)

#right angle triangle
n = int(input("Enter the length of heights in units"))
def rt(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
rt(n)
#numbered right angle numbered triangle
n = int(input("enter the number : "))
def rr(n):
    for i in range(n):
        for j in range(1,i+2):
            print(j,end="")
        print("")
rr(n)
#numbered right angle numbered triangle
n = int(input("enter the number : "))
def rr(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print("")
rr(n)
# right angle triangle up side down
n = int(input("Enter the number of units"))
def rau(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()
rau(n)
# right angle triangle up side down
n = int(input("Enter the number of units"))
def rau(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()
rau(n)
#pyramids
n =int(input("enter the unit height of pyramids"))
def pr(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        print("")
pr(n)
# upside down pyramid
n = int(input("Enter the length of units"))
def aa(n):
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n*2-1-i*2):
            print("*",end="")
        print("")
aa(n)
#upper pyramid lower pyramid sandwich
n = int(input("Enter the length of units"))
def uplp(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        print("")
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n*2-1-i*2):
            print("*",end="")
        print("")
uplp(n)
#triangle having vertical base
n = int(input("Enter the length of units from centre:"))
def tvb(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(n-1):
        for j in range(n-i-1):
            print("*",end="")
        print()
tvb(n)
#binary way of right angle triangle
n =  int(input("enter the height and units:"))
def bt(n):
    for i in range(n):
        if i%2 == 1 :
            for j in range(i+1):
                if (j%2) == 0:
                    print("0",end="")
                else:
                    print("1",end="")
        else:
            for j in range(i+1):
                if (j%2) == 0:
                    print("1",end="")
                else:
                    print("0",end="")
        print("")
bt(n)
n =int(input()) 
def hm(n):
        for i in range(n):
            for j in range(1,i+2):
                print(j,end="")
            for k in range(2*n-2*(1+i)):
                print(" ",end="")
            for l in range(i+1,0,-1):
                print(l,end="")
            print("")
hm(n)
# right angle numbered triangle
n = int(input("Enter the length of heights in units"))
def rt(n):
    a=1
    b=2
    for i in range(n):
        for j in range(a,b):
            print(j,end=" ")
        print()
        a=b
        b=a+i+2
rt(n)
n = int(input("enter the height of your triangle"))
def tri(n):
    for i in range(n):
        for j in range(65,65+i+1):
              print(chr(j),end="")
        print()
tri(n)
# right angle triangle up side down
n = int(input("Enter the number of units"))
def rau(n):
    for i in range(n):
        for j in range(65,65+n-i):
            print(chr(j),end="")
        print()
rau(n)
#numbered right angle numbered triangle
n = int(input("enter the number : "))
def rr(n):
    a=65
    for i in range(n):
        for j in range(65,65+1+i):
            print(chr(a),end="")
        print("")
        a=a+1
rr(n)
#pyramids
n =int(input("enter the unit height of pyramids"))
def pr(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for k in range(65,65+1+i):
            print(chr(k),end="")
        for l in range(65+i-1,64,-1):
            print(chr(l),end="")
        print("")
pr(n)
#numbered right angle numbered triangle
n = int(input("enter the height you wanna start from: "))
def rr(n):
    for i in range(n):
        for j in range(65+n-1-i,65+n):
            print(chr(j),end=" ")
        print("")

rr(n)

n = int(input("Enter the length of the unit: "))
def dmd(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for k in range(i):
            print(" ",end="")
        for l in range(i):
            print(" ",end="")
        for m in range(n-i):
            print("*",end="")
        print("")
    for o in range(n):
        for p in range(o+1):
            print("*",end="")
        for k in range(n-1-o):
            print(" ",end="")
        for l in range(n-1-o):
            print(" ",end="")
        for m in range(o+1):
            print("*",end="")
        print("")

dmd(n)
n = int(input("Enter the length of the unit: "))
def dmd(n):
    for o in range(n):
        for p in range(o+1):
            print("*",end="")
        for k in range(n-1-o):
            print(" ",end="")
        for l in range(n-1-o):
            print(" ",end="")
        for m in range(o+1):
            print("*",end="")
        print("")
    for i in range(n):
        for j in range(n-i-1):
            print("*",end="")
        for k in range(i+1):
            print(" ",end="")
        for l in range(i+1):
            print(" ",end="")
        for m in range(n-i-1):
            print("*",end="")
        print("")
dmd(n)
#square
n = int(input("enter the number of units whose square you want form"))
def sq(n):
    for i in range(n):
        if i==0 or i==(n-1):
            for j in range(n):
                print("*",end="")
        else:
            for k in range(n):
                if k==0 or k==(n-1):
                    print("*",end="")
                else:
                    print(" ",end="")
        print("")
sq(n)

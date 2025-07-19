#sum of factors
'''
n=int(input("enter sum odf factors:"))
s=0
for i in range(1,n):    
    if n%i==0:
       print(i)
       s=s+i
print("sum of factors:",s)

n=int(input("enter number:"))
s=0
if n%2==0:
    print("Perfect")
else:
    print("not a perfect")
#string without slicing reverse
s=input("enter string :")
lst=list(s)
lst.reverse()
print("After reversing:",lst)
#sum of series
n=int(input("enter:"))
s=0
for i in range(1,n+1):
    s=s+i
    print(s,end=" ")
print()
#square
n=int(input("enter square :"))
s=1
for i in range(1,n+1):
    s=s*i
    print(s,end=" ")
print()
#power
n=int(input("enter power:"))
s=1
for i in range(1,n+1):
    s=i**i
    print(s,end=" ")
print()
'''
#reverse string
ost=input("enter string:")
rst=""
for c in ost:
    rst=c+rst
print(rst)



















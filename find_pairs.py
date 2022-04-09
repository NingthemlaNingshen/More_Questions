##find the  pairs      output:-3
a=[10,20,30,10,30,30,10,10]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
j=0
l=[]
while j<len(b):
    k=0
    c=0
    while k<len(a):
        if b[j]==a[k]:
            c=c+1
        k=k+1 
    l.append(c)
    j=j+1
print(l)
x=0
s=0
while x<len(l):
    y=l[x]//2
    s=s+y
    x=x+1
print(s)

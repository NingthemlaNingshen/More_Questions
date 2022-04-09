a=[-5,-2,21,6]
m=a[0]
s=a[0]
i=0
l=[]
while i<len(a):
    if a[i]>m:
        m=a[i]
    if a[i]<s:
        s=a[i]
    i=i+1
j=s
while j<=m:
    l.append(j)
    j=j+1
print(l)
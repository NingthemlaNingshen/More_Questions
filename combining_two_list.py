a=[2,3,4,5,6]
b=[1,8,7,9,10]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
b.sort()
print(b)
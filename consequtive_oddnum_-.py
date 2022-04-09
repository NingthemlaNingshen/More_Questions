# # l=1243579              ##output:- 1243-5-7-9
l=357911
i=0
a=str(l)
s=" "
j=i+1
while i<len(a) and j<len(a):
    if int(a[i])%2!=0 and int(a[j])%2!=0:
        s=s+a[i]+"-"
    else:
        s=s+a[i]
    i=i+1
    j=j+1
print(s+a[-1])
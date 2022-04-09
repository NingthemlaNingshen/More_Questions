s=input("enter your charecter: ")
a=""
c=""
i=0
while i<len(s):
    if s[i]!="," and s[i]!= " ":
        a=a+s[i]
    i=i+1
b=a.upper()
j=-1
while j>=-len(b):
    c+=b[j]
    j-=1
if b==c:
    print(True)
else:
    print(False)
l=["zero","one","two","three","four","five","six","seven","eight","nine"]
num=input("enter your number: ")
s=""
i=0
while i<len(num):
    j=0
    while j<len(l):
        if num[i]==str(j):
            s+=" "+l[j]
        j=j+1
    i=i+1
print(s)
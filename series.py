user=int(input("enter your number: "))
i=0
s=0
while i<=user:
    s=s+i
    i=i+1
print("1"+"/"+str(s))

#or

n=int(input("enter your number: "))
i=1
s=""
while i<=n:
    s+="1/"+str(i)+"!+"
    i+=1
print(s[0:-1])

#or

n=int(input("enter your number: "))
i=1
while i<=n:
    print("1/"+str(i),end=" !+ " )
    i=i+1
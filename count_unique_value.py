# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

l = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
a=[]
while i<len(l):
    if l[i] not in a:
        a.append(l[i])
    i=i+1
print("count: ",len(a)," ",a)


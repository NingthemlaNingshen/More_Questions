
def num():
    c=0
    for i in range(7):
        if i%2!=0:
            c=c+1
    return c
print(num())



def num(a):
    c=0
    i=1
    while i<a:
        if i%2!=0:
            c=c+1
        i=i+1
    return c
print(num(5))
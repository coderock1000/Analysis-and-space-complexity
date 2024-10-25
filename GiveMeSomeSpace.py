def arraysum(a):
    sum = 0
    for i in a:
        sum = sum+i
    return(sum)

a=[12, 3, 4, 15 ]
arraysum(a)

def sum(a):
    if(a<=0):
        return
    return (a + sum(a-1))
#sum(7)
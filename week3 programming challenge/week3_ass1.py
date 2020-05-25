m=int(input())
x=[]
notes=[10,5,1]
noteCounter = [0,0,0] 
def deno(n):      
    a=0
    for i, j in zip(notes, noteCounter): 
        if  n>= i: 
            j = n//i 
            n= n- j * i 
            a+=j
    return(a)
    '''p=0
    for i in range(len(notes)):
        q=notes[i]
        p+=int(n/q)
        a=int(n%q)
        x.append(p)

    return sum(x)'''

print(deno(m))

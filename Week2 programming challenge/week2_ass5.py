def pisano(m): 
    a,b=0,1
    for i in range(0,m*m): 
        a,b=b,(a+b)%m 
        if (a==0 and b==1): 
            return i+1
def fibo(n):

    a=[0]*(n+1)
    if n<2:
        return n
    a[0]=0
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[-1]
n,m=map(int,input().split())
result=pisano(m)
rem=n%result
print(fibo(rem)%m)
    
    



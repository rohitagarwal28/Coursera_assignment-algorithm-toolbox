def fibo(n):

    a=[0]*(n+1)
    if n<2:
        return n
    a[0]=0
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[-1]
n=int(input())
print(fibo(n))
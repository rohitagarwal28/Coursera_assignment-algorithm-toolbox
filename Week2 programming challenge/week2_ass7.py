m,n=map(int,input().split())
def fibo(n):
    #a=[0]*(n+1)
    if n<2:
        return n
    cm=n%60
    a=0
    b=1
    for i in range(cm-1):
        a,b=b,a+b
        #a[i]=(a[i-1]%10+a[i-2]%10)%10
    return (b)%10
def fiborange(m,n):
    if m==n:
        return fibo(m%60)
    else:
        m=m%60
        n=n%60
        part1=fibo(m+1)-1
        part2=fibo(n+2)-1
    return (part2-part1)%10
print(fiborange(m,n))
#
# print(fibo(n))
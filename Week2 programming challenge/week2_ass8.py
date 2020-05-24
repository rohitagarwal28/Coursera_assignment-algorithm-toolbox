n=int(input())
def fibo(n):
    #a=[0]*(n+1)
    if n<2:
        return n
    a=0
    b=1
    for i in range(n-1):
        a,b=b,(a+b)
        #a[i]=(a[i-1]%10+a[i-2]%10)%10
    return (b)%10
def sumsqfibo(n):
    n=n%60
    if n<=0:
        return n
    else:
        return (fibo(n)*fibo(n+1))%10
print(sumsqfibo(n))
#
# print(fibo(n))
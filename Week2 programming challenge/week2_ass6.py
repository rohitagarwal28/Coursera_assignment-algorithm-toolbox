n=int(input())
def fibo(n):
    #a=[0]*(n+1)
    if n<2:
        return n
    a=0
    b=1
    cm=n%60
    for i in range(2,cm+1):
        a,b=b,a+b
        #a[i]=(a[i-1]%10+a[i-2]%10)%10
    return (b)%10
def sumfibo(n):
    return (fibo(n+2)-1)%10
print(sumfibo(n))
#
# print(fibo(n))
x,y=map(int,input().split())
def gcd(x,y):
    while y:
         x,y=y,x%y
    return x
print(gcd(x,y))
    
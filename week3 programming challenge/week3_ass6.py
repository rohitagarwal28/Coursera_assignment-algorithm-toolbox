def divide(n):
    result= []
    for i in range(1,n+1):
        n-=i
        if n<=i:
            i+=n
            result.append(i)
            break
        result.append(i)

    return result
n = int(input())
res=divide(n)
print(len(res))
for j in res:
    print(j, end=' ')
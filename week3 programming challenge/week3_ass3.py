d=int(input())
m=int(input())
n=int(input())
stops=list(map(int,input().split()))
def min_refills(distance,tank,stops):
    n=len(stops)
    stops=[0]+stops+[distance]
    numrefiils,currentrefills=0,0
    while currentrefills<=n:
        lastrefill=currentrefills
        while(currentrefills<=n and (stops[currentrefills+1]-stops[lastrefill])<=tank):
            currentrefills+=1
        if currentrefills==lastrefill:
            return -1
        if currentrefills<=n:
            numrefiils+=1
    return numrefiils
print(min_refills(d,m,stops))

    





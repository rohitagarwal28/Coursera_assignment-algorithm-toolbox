n_items,cap_W=map(int,input().split())
values=[]
weights=[]
for i in range(n_items):
    a,b=map(int,input().split())
    values.append(a)  
    weights.append(b)
def knapsack(cap,w,v):
    profit=0
    fractions=[0]*len(v)
    index=list(range(len(v)))
    ratio=[v/w for w,v in zip(w,v)]
    index.sort(key=lambda i:ratio[i],reverse=True)
    for i in index:
        if w[i]<=cap:
            profit+=v[i]
            cap-=w[i]
        else:
            profit+=v[i]*(cap/w[i])
            break
    return profit
print(knapsack(cap_W,weights,values))



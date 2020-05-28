def distance(a,b):
    d = [[0]*(len(b)+1) for _ in range(len(a)+1)]

    for i in range(len(a)+1):
        d[i][0] = i
    for j in range(len(b)+1):
        d[0][j] = j
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            insert = d[i][j-1]+1
            delete = d[i-1][j]+1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1]+1
            d[i][j] = min(insert,delete,match) if a[i-1]==b[j-1] else min(insert,delete,mismatch)
    return d[len(a)][len(b)]
print(distance(input(), input()))
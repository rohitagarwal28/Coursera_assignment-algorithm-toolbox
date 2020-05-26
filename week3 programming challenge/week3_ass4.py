n=int(input())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list1.sort()
list2.sort()
prod=[(a)*(b) for a,b in zip(list1,list2)]
print(sum(prod))


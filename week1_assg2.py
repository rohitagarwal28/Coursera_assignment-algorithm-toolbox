n = int(input()) 
nums = input().strip().split()
nums = [ int(i) for i in nums ]
secondmax, firstmax = sorted(nums)[-2:]
#print(firstmax)
#print(secondmax)
print(firstmax*secondmax)

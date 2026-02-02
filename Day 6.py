import numpy as np

input = open('Test 6.txt').read().splitlines()
nums, ops = [['0' if x=='' else x for x in l.split(' ')] for l in input[:-1]], input[-1].split()

index = [len(nums[i])-1 for i in range(len(nums))]
length = []
while not index==[0 for _ in range(len(nums))]:
    

total = 0
for col in range(len(nums[0])):
    #print(nums[:][col])
    if ops[col]=='*':
        total += np.prod(np.array(nums)[:,col])
    else:
        total += np.sum(np.array(nums)[:,col])

print(total)
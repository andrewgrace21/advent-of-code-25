from sympy import proper_divisors

ranges = open('Day 2 Input.txt').read().split(',')
IDs = []
for i in range(len(ranges)):
    temp = ranges[i].split('-')
    IDs += range(int(temp[0]),int(temp[1])+1)
IDs = [str(x) for x in IDs]
sum = 0

for ID in IDs:
    div = proper_divisors(len(ID))
    found = False
    for l in div:
        if not found:
            s = [ID[i:i+l] for i in range(0,len(ID),l)]
            #print(ID, s,l)
            if len(set(s)) == 1:
                sum += int(ID)
                found = True
                print(f"Found: {ID}")
        
print(sum)
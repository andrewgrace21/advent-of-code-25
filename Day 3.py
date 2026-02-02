banks = open('Day 3 Input.txt').read().splitlines()

sum = 0
for b in banks:
    save = 0
    for d in range(11,-1,-1):
        digit = max([int(c) for c in b[save:(-d if d>0 else len(b))]])
        save = b[save:].index(str(digit))+1+save
        sum += digit * 10**d
    
print(sum)
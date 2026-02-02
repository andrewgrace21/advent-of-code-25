rotations = open("Day 1 Input.txt").read().splitlines()
current = 50
code = [(-1 if rotations[i][0]=='L' else 1)*int(rotations[i][1:]) for i in range(len(rotations))]
count = 0

for c in code:
    current += c
    if current<=0 or current>=100:
        count += abs(int(current/100))
        if (current-c)%100 != 0:
            if c<=0:
                count += 1
    current = current%100
    
print(f"Password: {count}")
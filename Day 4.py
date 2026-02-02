import numpy as np

layout = open('Day 4 Input.txt').read().splitlines()
layout = [list(l) for l in layout]
visual = layout.copy()
layout = [[0 if layout[i][j]=='.' else 1 for j in range(len(layout[0]))] for i in range(len(layout))]
start = np.sum(layout)

run = True
while run:
    count = 0
    remove = []
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j]==1:
                total = sum(layout[i+x][j+y] if all([not (x==0 and y==0), i+x>=0, i+x<len(layout), j+y>=0, j+y<len(layout[0])]) else 0 for y in [-1,0,1] for x in [-1,0,1])
                if total<4:
                    count += 1
                    remove.append((i,j))
                    visual[i][j] = 'x'
    for r in remove:
        layout[r[0]][r[1]] = 0
    if count==0:
        run = False
            
print(start - np.sum(layout))
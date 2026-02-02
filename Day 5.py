'''
input = open('Day 5 Input.txt').read().split('\n\n')
ranges, IDs = [tuple(x.split('-')) for x in input[0].splitlines()], input[1].splitlines()

count = 0
for id in IDs:
    for start,end in ranges:
        if int(id)>=int(start) and int(id)<=int(end):
            count += 1
            break

print(count)
'''

ranges = open('Day 5 Input.txt').read().split('\n\n')[0].splitlines()
ranges = [tuple(x.split('-')) for x in ranges]
ranges = list(set(ranges))

count = 0
for i,(start,end) in enumerate(ranges):
    delete = []
    start,end = int(start),int(end)
    count += end-start+1
    save_count = -(end-start+1)
    print(f"start: {start}, end: {end}")
    for r1,r2 in ranges[i+1:]:
        r1,r2 = int(r1),int(r2)
        print(f"r1: {r1}, r2: {r2}")
        if r1>=start and r2<=end:
            delete.append((str(r1),str(r2)))
            #print(start,end)
            print(f"delete: {delete}")
        elif all([r1<=start, r2>=start, r2<=end]):
            count -= r2-start+1
            save_count += r2-start+1
            print(f"high: {r2-start+1}")
            start = r2+1
            print(f"new start: {start}")
        elif all([r1>=start, r1<=end, r2>=end]):
            count -= end-r1+1
            save_count += end-r1+1
            print(f"low: {end-r1+1}")
            end = r1-1
            print(f"new end: {end}")
        elif r1<=start and r2>=end:
            count += save_count
            print(f"save: {save_count}")
            break
        print(f"count: {count}")
    for d in delete:
        ranges.remove(d)
        #print(f"d: {d}")

print(count)
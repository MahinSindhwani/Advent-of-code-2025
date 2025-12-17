ranges=[]
mergedCount = []

with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while line != '':
        a ,b = line.split('-')
        ranges.append((int(a),int(b)))
        line = f.readline().strip()
ranges.sort()

s = ranges[0][0]
e = ranges[0][1]

for item in ranges:
    if e < item[0]:
        mergedCount.append(e-s+1)
        s=item[0]
        e=item[1]
    else:
        if e < item[1]:
            e = item[1]
        

mergedCount.append(e-s+1)


print(sum(mergedCount))

        




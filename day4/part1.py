file = open('input.txt', 'r')
dict1 = {}
x=0
y=0
for ch in file.read():
    if ch == '\n':
        x+=1
        y=0
        continue
    dict1[(x,y)] = ch
    y+=1
x+=1

def validCoord(i,j):
    return i>=0 and i<x and j>=0 and j<y

directions = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

count = 0
for i in range(x):
    for j in range(y):
        nei = 0
        if dict1[(i,j)] == '@':
            for dir in directions:
                s=(i+dir[0],j+dir[1])
                if validCoord(s[0],s[1]):
                    if dict1[s] == '@':
                        nei += 1
            if nei < 4:
                count += 1

print(count)
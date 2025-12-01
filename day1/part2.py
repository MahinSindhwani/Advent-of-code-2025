inputfile = open("part1.txt", "r")
start = 50
zcount = 0
output = []
for line in inputfile:
    rotation = int(line[1:])
    if line[0] == 'R':
        if rotation > 100 :
            zcount += rotation//100
            rotation = rotation % 100
        if start == 0:
            start = (start + rotation) % 100
        else:
            start = start + rotation
            if start > 100:
                zcount += 1
            start = start % 100
        output.append(start)
    elif line[0] == 'L':
        if rotation > 100 :
            zcount += rotation//100
            rotation = rotation % 100
        if start == 0:
            start = (start-rotation)%100
        else:
            start = start - rotation
            if start < 0:
                zcount += 1
            start = start % 100
        output.append(start)

print(zcount + output.count(0))
inputfile = open("input.txt", "r")
start = 50
zcount = 0
for line in inputfile:
    rotation = int(line[1:])
    if rotation > 100 :
            zcount += rotation//100
            rotation = rotation % 100
    if line[0] == 'R':
        if start == 0:
            start = (start + rotation) % 100
        else:
            start += rotation
            if start > 100:
                zcount += 1
            start %= 100
    elif line[0] == 'L':
        if start == 0:
            start = (start-rotation)%100
        else:
            start -= rotation
            if start < 0:
                zcount += 1
            start %= 100
    if start == 0:
        zcount += 1

print(zcount)
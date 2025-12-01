f = open("input.txt", "r")
start = 50
zcount = 0
for line in f:
    if line[0] == 'R':
        start = (start + int(line[1:])) % 100
        if start == 0:
            zcount+=1
    elif line[0] == 'L':
        start = (start - int(line[1:])) % 100
        if start == 0:
            zcount+=1

print(zcount)
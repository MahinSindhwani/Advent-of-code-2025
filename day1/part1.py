inputfile = open("part1.txt", "r")
start = 50
output = []
for line in inputfile:
    if line[0] == 'R':
        start = (start + int(line[1:])) % 100
        output.append(start)
    elif line[0] == 'L':
        start = (start - int(line[1:])) % 100
        output.append(start)

print(output.count(0))
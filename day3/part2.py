def maxJolt(n):
    jolt = ''
    startInd = -1
    for i in range(-12, 0):
        digit = 1
        for j in range(startInd+1, len(n[:i])+1):
            if int(n[j]) > digit:
                digit = int(n[j])
        jolt += str(digit)
        startInd = n.find(str(digit), startInd+1)
    
    return int(jolt)

with open('input.txt', 'r') as f:
    result = []
    for line in f:
        result.append(maxJolt(line.strip()))

    print(sum(result))
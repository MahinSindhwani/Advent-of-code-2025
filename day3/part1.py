def maxJolt(n):
    m=n[:-1]
    first = 1
    for ch in m:
        if int(ch)>first:
            first=int(ch)
    
    maxInd = m.index(str(first))
    second = 1
    for i in range(maxInd+1, len(n)):
        if int(n[i])>second:
            second = int(n[i])

    return(int(str(first)+str(second)))

with open('input.txt', 'r') as f:
    result = []
    for line in f:
        result.append(maxJolt(line.strip()))

    print(sum(result))


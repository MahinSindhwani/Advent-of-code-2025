result=set()
def invalidString(n):
    s = str(n)
    if s[0]=='0':
        s = s[1:]
    for i in range(1,(len(s)//2)+1):
        sub = set()
        for j in range(0, len(s), i):
            sub.add(s[j:j+i])
        if len(sub) == 1:
            result.add(int(s))
            
with open('input.txt', 'r') as f:
    ranges=f.read().strip().split(',')
    for item in ranges:
        a, b = item.split('-')
        for i in range(int(a), int(b)+1):
            invalidString(i)

print(sum(result))
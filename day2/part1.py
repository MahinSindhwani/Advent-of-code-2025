def invalidString(n):
    s = str(n)
    if s[0] == '0':
        s = s[1:]
    length = len(s)
    if length % 2 != 0:
        return False
    half = length //2
    return s[:half] == s[half:]

def sumInvalid(f):
    total = 0
    with open(f) as f:
        ranges = f.read().strip().split(',')
    for item in ranges:
        a_str, b_str = item.split('-')
        a = int(a_str)
        b = int(b_str)

        for value in range(a, b + 1):
            if invalidString(value):
                total += value

    return total

print(sumInvalid('inputTest.txt'))
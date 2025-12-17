ranges = []
countFresh = 0

with open('input.txt', 'r') as f:
    line = f.readline().strip()
    while line != '':
        a ,b = line.split('-')
        ranges.append((int(a),int(b)))
        line = f.readline().strip()

    line = f.readline().strip() 
    while line != '':
        for item in ranges:
            if int(line) >= item[0] and int(line) <= item[1]:
                countFresh +=1
                break
    
        line = f.readline().strip()
        
print(countFresh)




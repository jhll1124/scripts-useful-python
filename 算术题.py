import random

aim_count = 100
count = 0
while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    judgment = random.randint(1, 2)
    if judgment == 1:
        if a + b <= 100:
            count += 1
            print(a, '+', b, '=', a + b, sep='')
    elif judgment == 2:
        if a - b >= 0:
            count += 1
            print(a, '-', b, '=', a - b, sep='')
    if count == aim_count:
        break

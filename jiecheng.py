while True:
    a = int(input())
    b = a
    while a >= 2:
        a -= 1
        b *= a
    print(b,len(str(b)),sep=',')

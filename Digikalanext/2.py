def transform(str):
    t,b = 0,0
    tmp = ''
    for char in str:
        if char == "A":
            if t == 0:
                tmp = tmp +char
                t = 1
                b = 0
        if char == "B":
            if b == 0:
                tmp = tmp +char
                b = 1
                t = 0
    print(str)
    print(tmp)
    return len(str)-len(tmp)


str = 'AABAAB'
print(transform(str))
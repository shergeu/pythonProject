def golden_ratio(i):
    sp = []
    num1 = 1
    num2 = 1
    while len(sp) <= i + 1:
        sp.append(num1)
        num = num1 + num2
        num1 = num2
        num2 = num
    print(sp[i] / sp[i - 1])


golden_ratio(4)


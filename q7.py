n = [int(input()) for i in range(3)]
for i in n:
    odd = (i % 2 == 1)
    if i > 50:
        if odd:
            print('west')
        else:
            print('east')
    else:
        if odd:
            print('south')
        else:
            print('north')
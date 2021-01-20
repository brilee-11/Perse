car = input()
if car == 'electric':
    print('$0')
else:
    num = float(input())
    if car == 'petrol':
        if num < 1.8:
            print('$150')
        else:
            print('$170')
    elif car == 'hybrid':
        if num < 1.8:
            print('$120')
        else:
            print('$140')
    elif car == 'diesel':
        if num < 1.8:
            print('$180')
        else:
            print('$200')
#correct
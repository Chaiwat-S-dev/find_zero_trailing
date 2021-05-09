#!/usr/bin/env python3
def factorial(input):
    fact = 1
    for i in range(1, input+1):
        fact = fact * i
    return fact

def check_zero_trailing(input):
    count = 0
    while True:
        mod = input % 10
        input //= 10
        if mod == 0:
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    while True:
        try:
            num = int(input('Pls input integer number: '))
        except Exception as e:
            print(e)
            continue

        fact = factorial(num)
        print('fact: ', fact)

        count = check_zero_trailing(fact)
        print('Found zero trailing is: ', count)


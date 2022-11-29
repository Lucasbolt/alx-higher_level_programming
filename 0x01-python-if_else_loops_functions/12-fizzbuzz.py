#!/usr/bin/python3
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print('{}'.format('FizzBuzz'))
    elif i % 3 == 0:
        print('{}'.format('Fizz'), end=' ')
    elif i % 5 == 0:
        print('{}'.format('Buzz'), end=' ')
    else:
        print('{}'.format(i), end=' ')

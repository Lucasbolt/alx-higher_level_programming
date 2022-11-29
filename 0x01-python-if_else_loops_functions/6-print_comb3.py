#!/usr/bin/python3
for i in range(9):
    a = i + 1
    while (a < 10):
        if i == 8 and a == 9:
            print('{}{}'.format(i, a))
        else:
            print('{}{}'.format(i, a), end=", ")
        a += 1

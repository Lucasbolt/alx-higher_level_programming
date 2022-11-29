#!/usr/bin/python3
def uppercase(a):
    new = ''
    for i in a:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        new += i
    print('{}'.format(new))

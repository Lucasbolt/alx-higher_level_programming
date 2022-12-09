#!/usr/bin/python3
import sys
def myconv(number = ""):
    if len(number) == 0 or number == None:
        return 0

    conv = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

    result = 0
    digits = []
    for i in number:
        if i in conv.keys():
            digits.append(conv[i])
        else:
            print("Unrecognized letter")
            sys.exit()
    if digits[-1] == max(digits) and  digits[0] != digits[-1]:
        result = digits[-1]
        for i in range(len(digits) - 1):
            result-= digits[i]
        return result
    else:
        result = sum(digits)
        return result
if __name__ == '__main__':
    print(myconv('II'))
    print(myconv('IVQ'))
    print(myconv('DCCVII'))
    print(myconv('LXXXVII'))
    print(myconv('VII'))

#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = 0
        count = 1
        while count < len(sys.argv):
            n += int(sys.argv[count])
            count += 1
        print('{}'.format(n))


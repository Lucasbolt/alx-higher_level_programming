#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print('{} argument:'.format(1))
            print('{}: {}'.format(1, sys.argv[1]))
        else:
            print('{} arguments:'.format(len(sys.argv) - 1))
            n = 1
            while n < len(sys.argv):
                print('{}: {}'.format(n, sys.argv[n]))
                n += 1
    else:
        print('{} arguments.'.format(0))

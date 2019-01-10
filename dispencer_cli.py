import sys

from dispencer_engine import dispence


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ''
        
    print(dispence(arg))

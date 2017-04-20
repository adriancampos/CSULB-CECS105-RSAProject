import sys
from eulerstheorem import calculate_remainder

if __name__ == "__main__":
    try:
        print(calculate_remainder(int(eval(sys.argv[1])), int(eval(sys.argv[2])), int(eval(sys.argv[3]))))
    except IndexError:
        print("Must pass three integers. Using default: 245**1040 / 18.")
        print(calculate_remainder(245, 1040, 18))

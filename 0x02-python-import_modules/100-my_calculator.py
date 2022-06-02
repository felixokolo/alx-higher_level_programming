#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    lent = len(args)
    if lent != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        if args[2] not in "+-*/":
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)
        else:
            a = int(args[1])
            b = int(args[3])
            if args[2] == '+':
                result = add(a, b)
            if args[2] == '-':
                result = sub(a, b)
            if args[2] == '*':
                result = mul(a, b)
            if args[2] == '/':
                result = div(a, b)
            print("{} {} {} = {}".format(a, args[2], b, result))

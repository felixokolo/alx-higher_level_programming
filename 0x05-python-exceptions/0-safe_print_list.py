#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            return c
        except Exception:
            break
        else:
            c += 1
    else:
        print("")
    return c

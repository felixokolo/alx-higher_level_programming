#!/usr/bin/python3

if __name__ == "__main__":
    def divisible_by_2(my_list=[]):
        ret = []
        for x in my_list:
            if x % 2 == 0:
                ret.append(True)
            else:
                ret.append(False)
        return ret

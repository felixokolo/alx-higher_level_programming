#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    maxi = max(list_length)
    for i in range(maxi):
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            break
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except TypeError:
            print("wrong type")
            res = 0
        finally:
            result.append(res)
    return result

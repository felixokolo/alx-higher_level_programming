#!/usr/bin/python3

if __name__ == "__main__":
    def replace_in_list(my_list, idx, element):
        if idx < 0 or idx >= len(mylist):
            return my_list.copy()
        return my_list.copy()[idx] = element

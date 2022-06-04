#!/usr/bin/python3
def no_c(my_string):
    st = ''
    for x in range(len(my_string)):
        if my_string[x] not in "cC":
            st += my_string[x]
    my_string = st
    return my_string

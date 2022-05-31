#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        print(f"{chr(ord('z') - i)}", end = "")
    else:
        print(f"{chr(ord('Z') - i)}", end = "")

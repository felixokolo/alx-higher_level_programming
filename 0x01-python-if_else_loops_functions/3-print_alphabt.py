#!/usr/bin/python3
for i in range(26):
    if i + ord('a') != ord('q') and i + ord('a') != ord('e'):
        print(f"{chr(i + ord('a'))}", end = "")

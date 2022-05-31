#!/usr/bin/python3
for i in range(26):
    print(f"{chr(ord('z') - 32 * (i % 2) - i)}", end="")

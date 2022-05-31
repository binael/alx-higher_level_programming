#!/usr/bin/python3

flag = False

for i in range(100):
    if (i // 10) >= (i % 10):
        continue

    if flag:
        print(", ", end="")

    print("{:02d}".format(i), end="")
    flag = True

print("")

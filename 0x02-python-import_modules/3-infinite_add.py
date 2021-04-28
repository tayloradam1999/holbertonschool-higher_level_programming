#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    hank = 0
    for i in range(1, n):
        hank += int(sys.argv[i])
    print("{}".format(hank))

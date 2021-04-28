#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirlen = len(dir(hidden_4))
    for i in range(0, dirlen):
        names = dir(hidden_4)[i]
        if names.startswith('__'):
            continue
        print("{}".format(names))

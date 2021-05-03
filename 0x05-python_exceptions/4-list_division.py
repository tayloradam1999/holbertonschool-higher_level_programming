#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    x = 0
    while x < list_length:
        try:
            y = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            y = 0
            print("division by 0")
        except IndexError:
            y = 0
            print("out of range")
        except TypeError:
            y = 0
            print("wrong type")
        finally:
            my_list.append(y)
            x += 1
    return my_list

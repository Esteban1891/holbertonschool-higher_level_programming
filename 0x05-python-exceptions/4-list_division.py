#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    NewList = []
    count = 0
    for a in range(list_length):
        try:
            count = my_list_1[a] / my_list_2[a]
        except(ValueError, TypeError):
            print("wrong type")
            count = 0
        except ZeroDivisionError:
            print("division by 0")
            count = 0
        except IndexError:
            print("out of range")
            count = 0
        finally:
            NewList.append(count)
    return NewList

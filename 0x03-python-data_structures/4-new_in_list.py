#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lista = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return (lista)
    else:
        lista[idx] = element
        return(lista)

import random

def extract_elements_list(list_in_which_to_choose, int_nbr_of_element_to_extract):
    lst = []
    lst_copy=list(list_in_which_to_choose)
    taille = len(lst_copy)

    while 0 < int_nbr_of_element_to_extract:
        indice = random.randint(0, taille - 1)
        lst.append(lst_copy[indice])
        lst_copy.pop(indice)
        int_nbr_of_element_to_extract-=1
        taille -=1

    return lst

# print('Liste de départ',[1,3,7,6,6,6,8])
# sublist = extract_elements_list([1,3,7,6,6,6,8], 5)
# print('La sous liste extraite est', sublist)
# print('Liste de départ après appel de la fonction est',[1,3,7,6,6,6,8])


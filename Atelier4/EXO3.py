import random
def choose_element_list(list_in_which_to_choose):
    taille=len(list_in_which_to_choose)
    indice=random.randint(0, taille-1)
    return list_in_which_to_choose[indice]

#print(choose_element_list([1,3,7,0]))
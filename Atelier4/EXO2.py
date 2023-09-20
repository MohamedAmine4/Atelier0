import random

def mix_list(list_to_mix):
    lst_copy=list(list_to_mix)
    taille = len(lst_copy)
    lst = []
    while 0 < taille:
        random_index = random.randint(0,taille-1)
        lst.append(lst_copy[random_index])
        lst_copy.pop(random_index) #pour eviter la repetition des element 
        taille-=1
    return lst



#Test de votre code
lst_sorted=[0, 1, 2, 3, 4, 5,5, 5, 6, 8, 9]
print(lst_sorted)
print('Liste triée de départ',lst_sorted)
mixed_list=mix_list(lst_sorted)
print('Liste mélangée obtenue',mixed_list)
print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted.sort())
#assert (cf. doc en ligne) permet de vérifier qu’une condition 
#est vérifiée en mode debug (désactivable)
#assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList..."

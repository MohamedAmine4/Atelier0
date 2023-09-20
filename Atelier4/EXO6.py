#from EXO5 import perf_mix
def sort_list(liste):
    list_copy=list(liste)
    r=[]
    while list_copy:
        mini=min(list_copy)
        list_copy.remove(mini)
        r.append(mini)
    return r
#print(sort_list([2,4,4,8,1,9]))

# tailles_liste = [1000, 5000, 9000, 50000, 100000]
# nombre_execution = 10
# resultat = perf_mix(sort_list,sorted, tailles_liste, nombre_execution)
# print("Temps d'exécution moyen pour la fonction mix_list :", resultat[0])
# print("Temps d'exécution moyen pour la fonction random_shuffle :", resultat[1])


    
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from EXO2 import mix_list
from EXO4 import extract_elements_list
from EXO1 import gen_list_random_int

def perf_mix(mix_list,random_shuffle,taille_list,nombre_execution)->tuple:
        temps_execution_moyen_mix_list = []
        temps_execution_random_shuffle = []
        for i in taille_list:
            temp_mix_list=0  #a chaque element de la list 50 on va calculer le temp d'execution pour executer la list de cet element [50,50]
            temp_random_shuffle=0
            list_test=gen_list_random_int(0,i,i)
            for _ in range(nombre_execution):
                #liste = [1] * i #initialiser la list par l'element de taille list
                debut_mix_list=time.perf_counter()
                mix_list(list_test)
                fin_mix_list=time.perf_counter()
                temp_mix_list+=fin_mix_list-debut_mix_list
                
                debut_random_shuffle=time.perf_counter()
                random_shuffle(list_test)
                fin_random_shuffle=time.perf_counter()
                temp_random_shuffle+=fin_random_shuffle-debut_random_shuffle
             # Calculer le temps d'exécution moyen pour chaque fonction
            temps_execution_moyen_mix_list.append(temp_mix_list / nombre_execution)
            temps_execution_random_shuffle.append(temp_random_shuffle / nombre_execution)
        return (temps_execution_moyen_mix_list, temps_execution_random_shuffle)

tailles_liste = [10, 500, 5000, 50000, 100000]
nombre_execution = 10

resultat = perf_mix(mix_list, random.shuffle, tailles_liste, nombre_execution)
# print("Temps d'exécution moyen pour la fonction mix_list :", resultat[0])
# print("Temps d'exécution moyen pour la fonction random_shuffle :", resultat[1])



def perf_mix2(extract_elements_list,random_sample,taille_list,nombre_execution)->tuple:
        temps_execution_moyen_extract_elements_list = []
        temps_execution_random_sample = []
        for i in taille_list:
            temp_extract_elements_list=0  #a chaque element de la list 50 on va calculer le temp d'execution pour executer la list de cet element [50,50]
            temp_random_sample=0
            list_test=gen_list_random_int(0,i,i)
            for j in range(nombre_execution):
                #liste = [1] * i #initialiser la list par l'element de taille list
                debut_extract_elements_list=time.perf_counter()
                extract_elements_list(list_test,6)
                fin_extract_elements_list=time.perf_counter()
                temp_extract_elements_list+=fin_extract_elements_list-debut_extract_elements_list
                
                debut_random_sample=time.perf_counter()
                random_sample(list_test,6)
                fin_random_sample=time.perf_counter()
                temp_random_sample+=fin_random_sample-debut_random_sample
             # Calculer le temps d'exécution moyen pour chaque fonction
            temps_execution_moyen_extract_elements_list.append(temp_extract_elements_list / nombre_execution)
            temps_execution_random_sample.append(temp_random_sample / nombre_execution)
        return (temps_execution_moyen_extract_elements_list, temps_execution_random_sample)
    
resultat2= perf_mix2(extract_elements_list, random.sample, tailles_liste, nombre_execution)
   
    
    
    
    
    
#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
x_axis_list = np.arange(0,5.5,0.5)
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre 
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de 
#choisir éventuellement la couleur et le marqueur
ax.plot(tailles_liste,resultat[0],'bo-',label='extract_elements_list')
ax.plot(tailles_liste, resultat[1],'r*-', label='random_sample')
ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
 title='Comparaison des temps d\'exécution entre mix_list et shuffle')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()






                
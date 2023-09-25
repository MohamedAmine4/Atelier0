import numpy as np
import random
def somme_recursive(list):
    if not list:
        return 0
    else :
        return list[0]+somme_recursive(list[1:])

#print(somme_recursive([1,2,3,4,6]))

def factorielle_recursive(n):
    if n>0:
        return n *factorielle_recursive(n-1)
    else:
        return 1 
    
#print(factorielle_recursive(5))

def longueur(list):
    if  list==[]:
        return 0
    else :
          return 1+ longueur(list[1:])
    
#print(longueur([1,2,3,4,5,6]))

def listPairs(list):
    if not list:
        return []
    elif list[0]%2==0:
        return [list[0]]+listPairs(list[1:]) #depiler et stocker
    else :
        return listPairs(list[1:]) #depiler sans stocker 

#print(listPairs([1,2,3,4,5,6]))

def concat_list(list):
    if not list:
        return []
    else :
        return list[0]+concat_list(list[1:])
        
#print(concat_list([[1,2],[3,4],[5,6]]))

def incluse(list1,list2):
    if not list1:
        return True
    elif list1[0]not in list2:
        return False
    else:
        return incluse(list1[1:],list2[1:]) 
    
#print(incluse([1,2,6],[1,2,3,5,6]))

#searchsorted:il renvoie l'indice d'element/si element n'existe pas elle renoie l'indice ou il faut d'etre

def my_searchsorted(table,indice):
    i=0
    if table==[]:
        return 0
    max_val,min_val=max(table),min(table)
    taille=len(table)
    if indice in table:
        return table.index(indice)
    else: #si la valeur n'est pas dans la table
        if indice<min_val: #signifie que la valeur rechercher doit etre en premier
            return 0
        elif indice>max_val:
            diff=indice-max_val
            return table.index(max_val)+diff
        elif indice<max_val:
            while i<taille:
                if table[i]>indice:
                 indice_val=i-1
                 min_val=table[i-1]
                 break
                i+=1
            res=indice-min_val
            return indice_val+res
#print(my_searchsorted([9],23))

# arr = np.array([1, 2, 3, 5])
# x = np.where(arr==4)
# print(x)
def my_where(table,indice):
    if not table or indice not in table:
        return []
    else:
        table_occu=[]
        taille=len(table)
        for i in range(taille):
            if table[i]==indice:
                table_occu.append(i)
    return table_occu
#print(my_where([1, 2, 3, 4, 5, 4, 4],5))


def addition(table1,table2):
    A=np.array(table1)
    B=np.array(table2)
    len(A)==len(B)
    R=A+B
    return R
table1=([3,1],[6,4])
table2=([1,8],[4,2])
#print(addition(table1,table2))

M=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(M)
M=M+10
#print(M)
M=M*2
#print(M)
#print(M[1,:]) #la deuxième ligne de la matrice M
#print(M[:,2])  #Affichez la troisième colonne de la matrice M.
#print(M[:2,:2]) #2 premier ligne et 2 premier colone 

A = np.random.randint(0, 11, size=(4, 4)) #matrice de 4x4 avec des valeur aleatoire compris entre 0 et 10
#print(A)
M_identy=np.identity(3) #matrice identity de dimension 4x4 dddddddddd
#print(M_identy)
B=np.random.randint(0,11, size=(3,3))
###### TRACE D'UNE MATRICE
def matrice_trace(B):
    taille=len(B)
    tra=0
    for i in range(taille):
       for  j in range(len(B[i])) :
        if i==j:
           tra+=B[i][j]
    return tra
D=np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(D)
#print(matrice_trace(D))
######  est symetrique 
def est_symetrique(D):  #seulement si la matrice == sa transposer
    if np.array_equal(D,D.T):#comparer deux matrice ddddddddddddd
        return True
    return False
S=np.array([[1,2,3],
            [4,5,7],
            [7,8,9]])
#print(est_symetrique(D))
#print(est_symetrique(S))

def produit_diagonal(D): # produit d'un diagonal
    matrice_diagonal=np.diagonal(D)  #diagonal dddddddddddddd
    matric_prod=np.prod(matrice_diagonal) #produit ddddddddddddddddddd
    return matric_prod
#print(produit_diagonal(D))
matric= (A + A.T)/2
#print(A)
#print(matric)
#print(est_symetrique(matric))
i=np.identity(4)
#print(produit_diagonal(i))  
taille=len(S)   
#print(S)
S_inverse = np.linalg.inv(S) #inverse ddddddddddddddddddddddddd
#print(S_inverse)
##################################################################""
def matriceAdjacence(s,a):
    taille=len(s)
    mat=np.zeros([taille,taille])
    for arc in a:
        i,j=arc
        mat[i][j]=1
       # mat[j][i]=1#si la matrice est non orienté
    return mat
  
sommets = [0,1,2,3]
arcs = [(0, 1), (0, 2), (1, 3), (2, 3)]
matrice = matriceAdjacence(sommets, arcs)
print("Matrice d'adjacence :")
print(matrice)  
  
    



                

            
           
     

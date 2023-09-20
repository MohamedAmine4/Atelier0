def position_Ver1(lst,elt) :
    cont=-1
    for i in lst :
        cont+=1
        if i==elt :
            return cont   
    return -1

def position_Ver2(lst,elt) :
    Con=-1
    i=0
    while Con<len(lst) :
        Con+=1
        if lst[i]==elt :
           return Con 
        else :
            i+=1
    return -1
    
def nb_occurrences(lst,e) :
    con=0
    for i in lst :
        if i==e :
         con+=1
    return con  

def est_triee_ver1(lst) :
     cont=0
     for i in lst : 
         if i<0 :
             cont=i
         if cont>i :
             return False
         cont=i
     return True    
         
def est_triee_ver2(lst):
    con=0
    i=0
    while con<len(lst)-1:
        indice_1er_ele=con
        indice_2eme_ele=con+1
        if lst[indice_1er_ele] > lst[indice_2eme_ele] :
           return False
        con+=1
    return True

#la meilleur version c'est la version 2     



def position_tri(lst,e) :
      debut=0
      fin=len(lst)-1
      
      while debut<=fin :
            milieu = (debut + fin) // 2  # Trouver l'indice du milieu

            if lst[milieu] == e:
             return milieu  # L'élément a été trouvé, retourne son indice
            elif lst[milieu] < e:
              debut = milieu + 1  # L'élément cible est à droite du milieu
            else:
             fin = milieu - 1  # L'élément cible est à gauche du milieu

      return -1  
  


def a_repetition(lst) :
    T=[]
    con=0
    while con<len(lst)-1 :
         x=lst[con]
         if x in T :
             return True
         else:
             T.append(x)
         con+=1
    return False 

#print(a_repetition([-1,10,100,1000,10000]))
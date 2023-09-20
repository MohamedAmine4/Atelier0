from EXO2 import dictionnaire
from EXO2 import  mots_Nlettres


def  mot_correspond(mot, motif):
     len_motif=len(motif)
     len_mot=len(mot)
     res=True
     if len_mot == len_motif :
          for i in range(len_mot) :
              if motif[i] !="." and mot[i]!=motif[i] :
                  res=False
     else :
        res=False
     return res
#print(mot_correspond("tarte", "t..t."))

def  presente(lettre, mot):
     len_mot=len(mot)
     for i in range(len_mot) :
         if mot[i]==lettre:
             return i
     return -1
#print(presente("v", "cheval"))

def mot_possible(mot, lettres) :
    len_mot=len(mot)
    c=0
    for i in mot :
        if presente(i,lettres)!=-1:
            indice_i=lettres.find(i)
            lettres=lettres[:indice_i]+lettres[indice_i+1:] #une fois la lettre existe on supprime dans lettres
            c+=1
    if c==len_mot :
        return True
    return False
#print(mot_possible("chapeau", "abcehpuva"))

def  mot_optimaux(dico, lettres)->list:
     lst_mot_max=[] #list va contenir tt les mot qui rendre true de la func mot_possible et qui sont les plus grands taille 
     lst_mot=[i for i in dico if mot_possible(i,lettres) ] 
     mot_max=max(lst_mot,key=len) #return le mot le plus longue dans la list
     lst_mot_max=mots_Nlettres(lst_mot,len(mot_max)) #reterun une list conient seulement les mot de longeur maximal
     #lst_mot_max=[i for i in lst_mot if len(i)==len(mot_max)]
     return lst_mot_max
    
print(mot_optimaux(dictionnaire("profs.txt"),"ibrstemartinveahim"))

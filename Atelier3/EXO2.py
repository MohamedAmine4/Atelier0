def  mots_Nlettres(lst_mot, n) :
    list_n_lettre=[mot for mot in lst_mot if len(mot)==n]
    return list_n_lettre

def test(mots_Nlettres): 
    print(mots_Nlettres)

lst=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"]
n=4
#test(mots_Nlettres(lst,n))
#startswith  and endswith

def commence_par(mot:str, prefixe:str)->bool: 
    """_summary_

    Args:
        mot (str): _description_
        prefixe (str): _description_

    Returns:
        bool: _description_
    """
    return mot.startswith(prefixe) 

#print(commence_par("adversaire","ad"))

def finit_par(mot, suffixe):
     return mot.endswith(suffixe)

def  finissent_par(lst_mot, suffixe) :
    return [mot for mot in lst_mot if finit_par(mot, suffixe)]

def  commencent_par(lst_mot, prefixe) :
    return [mot for mot in lst_mot if commence_par(mot, prefixe) ]

# print(commencent_par(["bonjour","bon","nosql"],"bon"))
def liste_mots(lst_mot, prefixe, suffixe, n) :
    
    lst= mots_Nlettres(lst_mot, n)
    lst=commencent_par(lst, prefixe)
    lst=finissent_par(lst, suffixe) 
    return lst

print(liste_mots(["bonjour","bonj","nosql"],"bon","our",7))

def  dictionnaire(fichier)->list: 
      # ouverture du fichier en lecture (r=read)
        mots=[]
        f=open(fichier,"r")
        c=f.readline() #lecture d'une ligne dans une chaine
        # de caractères
       # print("** Contenu du fichier **")
        while c!="" :
         #print(c)
         clean_mot=c.strip("\n") #pour supprimer le  \n dans le resultat
         mots.append(clean_mot)
         c=f.readline()
        #print("** fin **")
        return mots

#print(dictionnaire("profs.txt"))
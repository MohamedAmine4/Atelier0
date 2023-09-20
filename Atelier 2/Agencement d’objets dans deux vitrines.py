def emplacement(nbEmplacement: int, Objet: list):
    nbObjet = len(Objet)
    rep1 = []
    rep2 = []
    j=0
    if nbObjet / nbEmplacement <= 2:
        while j < nbObjet -1 :
            if Objet[j]==Objet[j+1]:
                    if Objet[j] not in rep1 :
                       rep1.append(Objet[j])
                    if Objet[j] not in rep2 :
                       rep2.append(Objet[j])
            j+=1        
        for i in Objet :
            if i not in rep1 :
                if len(rep1)<=nbEmplacement-1 :
                 rep1.append(i)
                elif i not in rep2 :
                  if len(rep2)<=nbEmplacement-1 :
                    rep2.append(i)
            else :
                 if len(rep2)<=3 and i not in rep2 :
                  rep2.append(i)
        if len(rep2) > nbEmplacement :         
         return "vaous avez dépasser le nombre des vitrines desponible "
        else :
         return(rep1,rep2)
    else:
        return "Le nombre d'emplacemment est limité"

print(emplacement(6, [1,1,1, 3, 4, 5, 5,8, 1,8,9]))

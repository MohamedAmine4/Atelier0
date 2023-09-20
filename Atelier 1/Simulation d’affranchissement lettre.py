import math
verte_prix=[1.16,2.32,4,6,7.5,10.5,0.5]
prioritaire_prix =[1.43,2.86,5.26,7.89,11.44,0.5]
ecopli_prix=[1.14,2.28,3.92,0.5]
lettre_choix=["VERTE","PRIORITAIRE","ECOPLI"]
poid_choix=[20,100,250,500,1000,3000]
zone_choix=["OM1","OM2"]

def get_value(poid ) :
    for i in poid_choix :
        if poid <= i :
            poid=i
            break
        elif poid > poid_choix[5] :
            poid=poid_choix[5]
        
def montant_affranchissement() :
    # affranchissement={
    #       'lettres':
    #       {'verte_prix':{1.16,2.32,4,6,7.5,10.5,0.5} ,'prioritaire_prix' :{1.43,2.86,5.26,7.89,11.44,0.5} ,'ecopli_prix':{1.14,2.28,3.92,0.5}
    #            },
    #       'poids':
    #           {20,100,250,500,1000,3000}
    #           }
    #saisir des valeurs  

    choix = []
    contrl = False
    while not contrl:
        lettre = input("Saisir la lettre parmi (Verte-Prioritaire-Ecopli) --> ").upper()
        poid = int(input("Saisir le poids en g --> "))
        zone = input("Saisir la zone de destination parmi (OM1-OM2) --> ").upper()

        if lettre in lettre_choix and  zone in zone_choix:
            # choix.append(lettre)
            # choix.append(poid)
            # choix.append(zone)
            contrl = True  # Sortir de la boucle car les valeurs sont valides
        else:
            print("Veuillez saisir des valeurs valides.")
    for poids in poid_choix :
             if poids ==poid :
                 r=poid_choix.index(poids) #r contient indice de poid chisit === indice de son prix
                 poid=33333
                 if lettre == "VERTE" :
                     prix= verte_prix[r]
                 elif lettre == "PRIORITAIRE" :
                     prix= prioritaire_prix[r]
                 else :
                     prix= ecopli_prix[r]
             elif poid < poids :
                #   for i in poid_choix :
                     c=0
                     c=poid    #c contient le poid reel
                     poid=poids    #poid contient maintenant le poid qui appartient a notre intervale
                     r=poid_choix.index(poids) #r contient indice de poid choisit === indice de son prix
                     poid=333333 #pour ne pas enter dans la boucle de for deuxiem fois
                     if zone == "OM1" :
                        if lettre == "VERTE" :
                            prix= verte_prix[r] + (math.ceil(c/10)* 0.05)
                        elif lettre == "PRIORITAIRE" :
                            prix= prioritaire_prix[r] + (c /10)* 0.05
                        else :
                            prix= ecopli_prix[r] + (c /10)* 0.05
                     else:
                       if lettre == "VERTE" :
                            prix= verte_prix[r] + (c /10)* 0.11
                       elif lettre == "PRIORITAIRE" :
                            prix= prioritaire_prix[r] + (c /10)* 0.11
                       elif lettre == "PRIORITAIRE" :
                            prix= ecopli_prix[r]+ (c /10)* 0.11
                 
             
                
                   
    print("le prix finale est "+str(prix)+"$")
    
                    
montant_affranchissement()
     


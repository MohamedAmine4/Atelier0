import random
"""
reponse = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()
if reponse != 'O' or reponse != 'N' :
        print("Je n'ai pas compris votre réponse")
if reponse == 'O':
    nom_j1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nom_j1, " nous allons jouer ensemble \n")
    nom_j2 = 'Machine'  
resultat_j1 = 0
round = 0
if reponse == 'N':
    nom_j1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nom_j1, " nous allons jouer ensemble")
    nom_j2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nom_j2, " nous allons jouer ensemble \n")
  """  
reponse = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()
i=0
while reponse != 'O' and reponse != 'N' :
         print("Je n'ai pas compris votre réponse")
         reponse = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()
         i+=1
         if i>=3 :
             break
         
if i < 3 :      
    nom_j1 = input("Quel est votre nom ? ")

    if reponse == 'O':      
                    print("Bienvenu ",nom_j1, " nous allons jouer ensemble \n")
                    nom_j2 = 'Machine'  
    else :
                    print("Bienvenu ",nom_j1, " nous allons jouer ensemble")
                    nom_j2 = input("Quel est le nom du deuxième joueur ?")
                    print("Bienvenu ",nom_j2, " nous allons jouer ensemble \n")
        
    resultat_j1 = 0
    resultat_j2 = 0
    round = 0
    aucun_choix = True
    item=0
    while aucun_choix == True:
        round += 1 
        item+=1
        CHOIX_Despo =["pierre","papier","ciseaux"]
        choix_j1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nom_j1))
        for i in CHOIX_Despo :
            if (choix_j1 == i ) :
                aucun_choix =False
        if item > 3 :
            break       
    if aucun_choix ==True :
          print("Je n'ai pas compris votre réponse")
    while aucun_choix==True :
            print("Joueur ", nom_j1)
            choix_j1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
            aucun_choix=False
            if choix_j1 != 'pierre' and choix_j1 != 'papier' and choix_j1 != 'ciseaux':
                aucun_choix = True
        
    if nom_j2 == 'Machine': 
            #Ici il faudrait plutôt vérifier que reponse == 'O' autrement
            #il y a un problème si le joueur 2 s'appelle Machine !
            choix_j2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]


    """
    c = True
    resultat_j2 = 0
    while c == True:
        round += 1 
        choix_j1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nom_j1))
        if choix_j1 != 'pierre' or choix_j1 != 'papier' or choix_j1 != 'ciseaux':
                    c1ok = False
                    print("Je n'ai pas compris votre réponse")
                    while c1ok == False :
                        print("Joueur ", nom_j1)
                        choix_j1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                        c1ok = True
                        if choix_j1 != 'pierre' or choix_j1 != 'papier' or choix_j1 != 'ciseaux':
                            c1ok = False

        if nom_j2 == 'Machine': 
            #Ici il faudrait plutôt vérifier que reponse == 'O' autrement
            #il y a un problème si le joueur 2 s'appelle Machine !
            choix_j2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]

    """
    if nom_j2 != 'Machine':
            print("Joueur", nom_j2)
            choix_j2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
            if choix_j2 != 'pierre' or choix_j2 != 'papier' or choix_j2 != 'ciseaux' :
                        aucun_choix = True
                        print("Je n'ai pas compris votre réponse")
                        while not aucun_choix :
                            print("Joueur ", nom_j2)
                            choix_j2 = input(" faîtes votre choix  parmi (pierre, papier, ciseaux): ")
                            aucun_choix = False
                            if choix_j2 != 'pierre' or choix_j2 != 'papier' or choix_j2 != 'ciseaux' :
                                        aucun_choix = True

    #On affiche les choix de chacun
    print("Si on récapitule :",nom_j1, choix_j1, "et", nom_j2, choix_j2,"\n")

        #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if choix_j1 == 'papier' and choix_j2 == 'papier' :
            Gagnant = "aucun de vous, vous être ex æquo"
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'pierre' and choix_j2 == 'papier' :
            Gagnant = nom_j2
            resultat_j2 = resultat_j2 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'pierre' and choix_j2 == 'pierre' :
            Gagnant = "aucun de vous, vous être ex æquo"
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'pierre' and choix_j2 == 'ciseaux' :
            Gagnant = nom_j1
            resultat_j1 = resultat_j1 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'papier' and choix_j2 == 'ciseaux' :
            Gagnant = nom_j2
            resultat_j2 = resultat_j2 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'papier' and choix_j2 == 'pierre' :
            Gagnant = nom_j1
            resultat_j1 = resultat_j1 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'ciseaux' and choix_j2 == 'pierre' :
            Gagnant = nom_j2
            resultat_j2 = resultat_j2 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")
    if choix_j1 == 'ciseaux' and choix_j2 == 'ciseaux' :
            Gagnant = "aucun de vous, vous être ex æquo"
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if choix_j1 == 'ciseaux' and choix_j2 == 'papier' :
            Gagnant = nom_j1
            resultat_j1 = resultat_j1 + 1
            print("le gagnant est",Gagnant)
            print("Les scores à l'issue de cette manche sont donc",nom_j1, resultat_j1, "et", nom_j2, resultat_j2, "\n")

    if round ==1 or round ==2 or round==3 or round==4:
            aucun_choix = True
    if round ==5:
            aucun_choix = False
            
    if round ==1 or round ==2 or round==3 or round==4:
            #On propose de c ou de s'arrêter 
            go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom_j1,nom_j2)).upper()
            if go == 'O':
                aucun_choix = False
            if go == 'N':
                aucun_choix = False
            if go != 'O' and go != 'N':
                aucun_choix = True
                print("Vous ne répondez pas à la question, on continue ")
    
            
    if aucun_choix == False :
        print("Merci d'avoir joué ! A bientôt")
else :
           print("vous avez depasser le nomre d'essaye A bientôt")
 
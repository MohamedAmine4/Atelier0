import random
def  places_lettre(ch : str, mot : str) -> list :
    indice=[]
    for i in range(len(mot)) :
      if mot[i]==ch :
         indice.append(i)
    return indice

#print( places_lettre('a','bonjour'))

def test(ch: str, mot : str):
    print(places_lettre(ch,mot))

# mot=input("saisir le mot  ")
# ch=input("saisir le lettre  ")  
#test(ch,mot)

def  outputStr(mot:str, lpos:list)-> str:
      mot2=[]
      taille=len(mot)
      mot2 = [mot[i] if i in lpos else "_" for i in range(taille)]
      # for i in range(len(mot))  :
      #         if i in lpos  :
      #           mot2.append(mot[i])
      #         else :
      #             mot2.append("_")
      
      return "".join(mot2)        
#print(outputStr("maman",[1,3]))

#rest a traiter si la lettre deja remplit il faut pas dir bravo 
###########################################################################################################################
def build_dict(lst: list) -> dict:
    dic={}
    for key in lst :
        taille=len(key)
        if taille in dic :
            dic[taille].append(key)
        else :
         dic[taille]=[key]        
    return dic
lst =['paris','londres','madrid','berlin','new-york',"oui","non"]
#print(build_dict(lst))
#############################################################################################################################""
def select_word(sorted_words:dict, word_len:int)->str :
    mot="not exitse"
    for key in sorted_words:
        if key==word_len:
            mot=random.choice(sorted_words[key])
    
    return mot
#print(select_word(build_dict(lst),3))

#################################################################################################################################""
def  runGame() :
    ##########################"
    lst =['paris','londres','madrid','berlin','new-york']
    taille=int(input("saisir le niveau de difficulté que tu vous : \n niveau 'easy' taille du mot < 7 \n niveau 'normal' 6 < taille du mot < 9 \n niveau 'hard' taille du mot > 8 \n"))
    mot=select_word(build_dict(lst),taille)
    ##########################"
   
    lst_len = len(lst)
   # iRand = random.randint(1, lst_len)
    #print(outputStr(lst[iRand],[]))
   # print(lst[iRand])
    print(mot)
    nbr_tentative=5
    list_indice=[]
    mot_actuel="________"
    while nbr_tentative!=0 and "_" in mot_actuel :      #len(list_indice) < len(lst[iRand])
        lettre=input("saisir la lettre : ")
       # indice_lettre=places_lettre(lettre,lst[iRand]) #return chaque fois une liste 
        indice_lettre=places_lettre(lettre,mot)
        #if lettre in lst[iRand] :
        if lettre in mot :
            list_indice+=indice_lettre
           # mot_actuel=outputStr(lst[iRand],list_indice)
            mot_actuel=outputStr(mot,list_indice)
            print("Bravo :) vous avez connais un lettre existe dans le mot : ",end='')
            print("voici votre mot : ",mot_actuel)
            
        else :
            nbr_tentative-=1
            print(":( votre lettre n'existe pas: ",end='')
            print("il vous reste {} tentative".format(nbr_tentative))
            #print("voici votre mot : ",outputStr(lst[iRand],list_indice))
            print("voici votre mot : ",outputStr(mot,list_indice))

    if nbr_tentative <= 5:
      for i in range(5,nbr_tentative,-1):   
          match i:
              case 5:
                  print("|---]")
              case 4:
                  print("| O")
              case 3:
                  print("| T")
              case 2:
                  print("|/ \\")
              case 1:
                  print("|______")

runGame()      
##################################################################################################################################""
def  build_list(fileName : str) -> list:
     
    #### lire un fichier
    file = open(fileName, "r",encoding="utf-8")
    list=[]
    content = file.readlines()
    for i in content :
        cleane_line = i.strip("\n\t")
        mot=cleane_line.lower()
        mot=cleane_line.split("\t")
        list.append(mot)
    file.close() 
    return list     

#print(build_list("capitales.txt"))


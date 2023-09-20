from max import val_max
import matplotlib.pyplot as plt
def histo(F :list)->list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    max_value = val_max(F) # Déterminer la valeur maximale dans F
    
    
    H = [0] * (max_value + 1) # Initialiser la liste H avec des zéros (+1 car ona commencet de zero)
    
    
    for i in F: # Compter les occurrences de chaque élément de F
        H[i] += 1
    return H

def est_injective(F :list)->bool :
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H=histo(F)
    
    for i in H :
        if i > 1 :
            return False
    return True

def est_surjective(F) :
    H=histo(F)
    
    for i in H :
        if i < 1 :
            return False
    return True
    
def est_bijective(F) :
    
    if est_surjective(F) and est_injective(F) :
        return True 
    return False

#print(histo([1,5,5,5,9,11,11,15,15,15]))
#print(est_bijective([6,5,6,7,4,2,1,5]))
#print(est_bijective([3,0,6,7,4,2,1,5]))

#                    QST2

def afficheHisto(F:list) :
    """_summary_

    Args:
        F (list): _description_
    """
    H=histo(F)
    MAXOCC=max(H) 
    
    for i in range(MAXOCC, -1, -1) :  #pour inverser le for 
         for j in range(len(H)) :
             if H[j]!=0 and H[j] > i:   
                 print(" #  ",end='')
             else :
                 print("    ",end='')
         print("\n")            
    for i in range(0,val_max(F)+1) : 
        print("| --", end='')
    print("|\n")    
    for i in range(0,val_max(F)+1) : 
        if i>=9: 
            print("  "+str(i),end='')
        else :  
          print("   "+str(i), end='')
       
        
def afficheHisto2(F:list) :
     
     plt.hist(F,edgecolor = 'white')
     plt.show()
 
            
afficheHisto([6,5,6,7,4,2,1,5])      
          

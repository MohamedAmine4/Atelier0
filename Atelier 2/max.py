def somme_Ver1(L) :
    s=0
    for i in range(0,len(L)) :
        s+=L[i]
    return s 

def somme_Ver2(L):
    s=0
    for i in L :
        s+=i
    return   s    
def somme_Ver3(L):
    Con=0
    i=0
    s=0
    while Con<len(L) :
        s+=L[i]
        i+=1
        Con+=1
    return  s


def test_exercice1():
    print("TEST SOMME")
    print("somme vide")
    print(somme_Ver1([]))
    print("Test somme 11111 ")
    print(somme_Ver2([1,10,100,1000,10000]))
    print("somme somme 11111")
    print(somme_Ver3([1,10,100,1000,10000]))
    
def moyenne(L) :
     if len(L)==0 :
         print("La liste est Vide")
     else :
         return somme_Ver1(L)/len(L)
    
def nb_sup_vers1(L,e) :
       cont=0  #conteur
       for i in range(0,len(L)) :
           if L[i]>e :
               cont+=1
       return cont
   
def nb_sup_vers2(L,e) :
       cont=0  #conteur
       for i in L :
           if i>e :
               cont+=1
       return cont   



def moy_sup(L,e) :
    List_Sup=[]
    for i in L :
           if i>e :
               List_Sup.append(i)
    return moyenne(List_Sup)
    

def val_max(L):
    max=L[0]
    for i in L :
        if i>max :
           max=i
    return max
    
def ind_max(L) :
    cont=-1
    for i in L :
        cont+=1
        if i==val_max(L) :
           return cont
       
         
#test_exercice1()
#print("la moyenne est ",moyenne([1,10,100,1000,10000]))
# print(nb_sup_vers1([1,10,100,1000,10000],2))
# print(nb_sup_vers2([1,10,100,1000,10000],2))
#print(moy_sup([1,10,100,1000,10000],2))
#print(val_max([1,10,100,1000,10000]))
#print(ind_max([1,10,100,1000,10000]))
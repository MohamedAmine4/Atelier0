def present(L :list,e :int)->bool:
    return e in L 
def present1 (L, e) :
    for i in range (0, len(L), 1) : 
     if (L[i] == e) : 
      return(True)
     
    return (False) 

#VERSION 2
def present2 (L, e) :
    b=False
    for i in range (0, len(L), 1) : 
     if (L[i] == e) : 
         b=True
    
    return (b)

#VERSION 3
def present3 (L, e) :
    for i in range (0, len(L), 1) : 
        b=(L[i] == e) 
        if b==True :
            return True
    return False    
#VERSION 4
def present4(L, e):
    b = False
    i = 0
    while i < len(L):  
        if L[i] == e:
            b = True
            return b
        i += 1
    return b

    
def test_present(present:callable) :
    if present([],5) :
        print ("ECHEC: test liste vide") 
    else :
        print  ("SUCCES : test liste vide")
    L=[3,4,5,6,7,8,9]
    
    if present(L,3) :
        print  ("SUCCES:test debut")
    else :
        print ( "ECHEC:test debut")
    if present(L,6) :
        print ( "SUCCES:test milieu")
    else :
        print  ("ECHEC:test milieu")
    if present(L,9) :
        print ( "SUCCES:test fin")
    else :
        print  ("ECHEC:test fin")
    if present(L,19) :
        print ( "SUCCES:test absence")
    else :
        print ( "ECHEC:test absence")   

#test_present(present4)
def pos(L,e):
    pos=[]
    for i in range(len(L)):
        if L[i]==e :
            pos.append(i)       
    return pos    


#VERSION 1
def pos1(L, e) :
    Lres = []
    for i in range (0, len(L), 1) :
     if (L[i] == e) :
      Lres += [i]
    return Lres

# VERSION 2
def pos2(L, e) :
    Lres =[]
    for i in range (0, len(L), 1) :
     if (L[i] == e) :
      Lres= i
    return Lres

 # VERSION 3
def pos3(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    for i in range (0, len(L), 1) :
     if (L[i] == e) :
      Lres.append(i)
    return Lres 

# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
     if (L[i] == e) :
      Lres[j]= i
      j += 1
    while 0 in Lres:
      Lres.remove(0)
    return Lres

def test_pos(pos:callable) :
    if pos([],5) :
        print ("ECHEC: test liste vide") 
    else :
        print  ("SUCCES : test liste vide")
    L=[3,4,5,6,7,8,9]
    
    if pos(L,3) :
        print  ("SUCCES:test debut")
    else :
        print ( "ECHEC:test debut")
    if pos(L,6) :
        print ( "SUCCES:test milieu")
    else :
        print  ("ECHEC:test milieu")
    if pos(L,9) :
        print ( "SUCCES:test fin")
    else :
        print  ("ECHEC:test fin")
    if pos(L,19) :
        print ( "SUCCES:test absence")
    else :
        print ( "ECHEC:test absence")
    
test_pos(pos4)  


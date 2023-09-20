def separation(L):
    LSEP=[]
    neg=[]
    pos=[]
    zero=[]
    for i in L :
        if i<0 :
         neg.append(i)
        elif i==0 :
            zero.append(i)
        else :
             pos.append(i)
    
    LSEP.extend(neg)
    LSEP.extend(zero)
    LSEP.extend(pos)
    return LSEP

print(separation([1,-1,0,9,-2,0]))
def full_name(str_arg:str)->str:
   taille=len(str_arg)
   list=[]
   r=str_arg.find(" ")
   for i in range(taille) :
       if i<r :
           list.append(str_arg[i].upper())
       elif i==r+1:
          list.append(str_arg[r+1].upper()) 
       else :
           list.append(str_arg[i])
    
   return  "".join(list)
#print(full_name("bisgambiglia Paul"))
def is_mail(str_arg:str)->(int,int) :
    r=str_arg.find("@")
    i_p=str_arg.find(".")
    if r==-1 :
        res=(0, 2)
    elif str_arg[r+1] =="." or str_arg[r:].count(".")==2:
        res=(0, 3)
    elif "." not in str_arg[r:]  :
        res=(0, 4)
    elif r==0 or str_arg[0]=="." or str_arg[i_p +1]=="." or str_arg[r-1]==".":     #@ d'indice 0 signifie le premier caractere dans email
        res=(0, 1)
    else :
     res=(1,1)   
    return res 
#print(is_mail("bisgambiglia@gmail.fr"))
def test(is_mail)->str :
        if is_mail==(0, 1) :
          print("le mail n’est pas valide, le corp n’est pas valide (bisgambiglia)"+str(is_mail))
        elif is_mail==(0, 2) :
         print("le mail n’est pas valide, il manque l’@"+str(is_mail))
        elif is_mail==(0,3):
            print(" le mail n’est pas valide, le domaine n’est pas valide (univ-corse)"+str(is_mail)) 
        elif is_mail==(0,4):
            print(" le mail n’est pas valide, il manque le ."+str(is_mail))
        else :
            print("le mail est valide"+str(is_mail))


#test(is_mail('bisgambiglia@univ-corse.fr'))

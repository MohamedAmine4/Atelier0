import math
def  discriminant(a :float,b :float,c:float)->float :
    return (b*b) -4*a*c

def  racine_unique(a :float,b: float)-> float :
   if a!=0 : 
      return -b/2*a
   else :
       return "Erreur il faute que a!=0"

def  racine_double(a :float,b:float,delta :float,num :int)-> float :
     if a!=0 :
       if num==1 :
            return round((-b+ (math.sqrt(delta)))/(2*a),2)
       else :
            return round((-b- (math.sqrt(delta)))/(2*a),2)
     else :
           return "Erreur il faute que a!=0"
         
def str_equation(a: float, b: float, c: float) -> str:
    if b == 0 :
        return f"{a}x² + {c} = 0"
    elif b == 0 and c==0 :
        return f"{a}x² = 0"
    else:
        return f"{a}x² + {b}x + {c} = 0"

def  solution_equation(a:float,b:float,c:float)->str :
    delta=discriminant(a,b,c)
    if delta<0 :
        res="Pas de racine réelle"
    elif delta>0 :
        if a!=0 :
          res="Deux racines : \n x1= "+str(racine_double(a,b,delta,1))+"\n x2= "+str( racine_double(a,b,delta,2))
        else :
            res="Erreur il faute que a!=0"
    else :
        res="racine unique = "+ str(racine_unique(a,b))
    return res 

def  equation(a:int,b:int,c:int)->str :
     print("Solution de l'equation "+str_equation(a,b,c))
     print(str(solution_equation(a,b,c)))

def test() :
 equation(2,-1,-6)
 equation(2,2,0)

test()
from ex2 import bissextile

def date_est_valide(jour :int,mois:int,annee:int)->bool :
   if annee > 0 and 1 <= mois <= 12:
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= jour <= 31
        elif mois == 2:
            return bissextile(annee)
        else:
            return 1 <= jour <= 30
   return False

print(date_est_valide(80,12,2009))
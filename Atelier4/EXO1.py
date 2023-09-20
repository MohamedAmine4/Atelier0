import random 

def  gen_list_random_int(inf=0,sup=10,nbr=10):
     random_numbers = [random.randint(inf, sup - 1) for i in range(nbr)]
     return random_numbers

random_list2 = gen_list_random_int(5, 15, 7)
#print(random_list2)
# from EXO6 import sort_list
# from EXO2 import mix_list
# def stupid_sort(lst_to_sort):
#     lst=sort_list(lst_to_sort)
#     lst_stupid=mix_list(lst_to_sort)    
#     while lst!=lst_stupid :
#        lst_stupid=mix_list(lst_to_sort)
#     return lst_stupid

#print(stupid_sort([0, 3, 2]))

def insertion_sort(lst):
    list_copy = list(lst)
    taille = len(list_copy)
    for i in range(1, taille):
        x = list_copy[i]
        j = i
        while j > 0 and list_copy[j - 1] > x:
            list_copy[j] = list_copy[j - 1]
            j -= 1
        list_copy[j] = x
    return list_copy

#print(insertion_sort([4, 3, 2,1,2]))

def selection_sort(lst_to_sort):
    lst_copy=list(lst_to_sort)
    taille=len(lst_copy)
    for i in range(0,taille-1):
        min=i
        for j in range(i+1,taille):
            if lst_copy[j]<lst_copy[min]:
                min=j
        if min!= i :
           lst_copy[i],lst_copy[min]=lst_copy[min],lst_copy[i]
    return lst_copy

#print(selection_sort([4,2, 3, 2,1,0,12,1,13]))

def tri_à_bulles(lst_to_sort):
    lst_copy=list(lst_to_sort)
    taille=len(lst_to_sort)
    for i in range(taille-1,1,-1):     #le truc ici c'est d'ajouter -1 pour reverser la boucle
        for j in range(0,i-1):
            if lst_copy[j+1]<lst_copy[j]:
                lst_copy[j+1],lst_copy[j]=lst_copy[j],lst_copy[j+1]
    return lst_copy
def tri_à_bulles_optimisé(lst_to_sort):
    lst_copy=list(lst_to_sort)
    taille=len(lst_copy)
    for i in range(taille-1,1,-1):
        list_triee=True
        for j in range(0,i-1):
            if lst_copy[j+1]<lst_copy[j]:
             lst_copy[j+1],lst_copy[j]=lst_copy[j],lst_copy[j+1]
             list_triee=False
        if list_triee:
            return lst_copy

#print(tri_à_bulles_optimisé([4,2, 3, 2,1,0,12,1,13]))
def fusion(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    elif lst1[0] <= lst2[0]:
        return [lst1[0]] + fusion(lst1[1:], lst2)
    else:
        return [lst2[0]] + fusion(lst1, lst2[1:])

def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    middle = len(list_to_sort) // 2
    lst1 = list_to_sort[:middle]
    lst2 = list_to_sort[middle:]

    return fusion(merge_sort(lst1), merge_sort(lst2))

#print(merge_sort([4, 2, 3, 2, 1, 0, 12, 1, 13]))
def radix_order_sort(lst_to_sort,ordre):
    
    

def radix_sort(lst_to_sort):
    






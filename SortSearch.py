from random import randint
def bubble_sort(a):
    for i in range (len(a) -1):
        swapped = False
        for j in range (len(a)-1):
            if a[j] > a [j +1]:
                swap = a[j]
                a[j] = a[j+1]
                a[j+1] = swap
                swapped = True
        if not swapped:
            break
        
def insertion_sort(a):
    for i in range(1 , len(a)):
        x = a[i]
        index_hole = i
        
        while index_hole > 0 and a[index_hole -1] > x:
            a[index_hole] = a[index_hole - 1]
            index_hole -= 1
            
        a[index_hole] = x
    
    
a = [randint(1,1000) for i in range(50)]
print(a)
insertion_sort(a)
print(a)

import random, time

def merge3(array, a1, a2, a3):
    i = 0 # 1st array pointer
    j = 0 # 2nd array pointer
    k = 0 # 3rd array pointer
    l = 0 # merged pointer

    #CASE a1, a2, a3 all populated
    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] <= a2[j] and a1[i] <= a3[k]:
            array[l] = a1[i]
            i = i + 1
        elif a2[j] <= a3[k] and a2[j] <= a1[i]:
            array[l] = a2[j]
            j = j + 1
        elif a3[k] <= a2[j] and a3[k] <= a1[i]:
            array[l] = a3[k]
            k = k + 1
        l = l + 1
    
    #CASE - a1 and a2 left 
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            array[l] = a1[i]
            i = i + 1
        else:
            array[l] = a2[j]
            j = j + 1
        l = l + 1
    
    #CASE - a2 and a3 left
    while j < len(a2) and k < len(a3):
        if a2[j] <= a3[k]:
            array[l] = a2[j]
            j = j + 1
        else:
            array[l] = a3[k]
            k = k + 1
        l = l + 1

    #CASE - a1 and a3 left
    while i < len(a1) and k < len(a3):
        if a1[i] <= a3[k]:
            array[l] = a1[i]
            i = i + 1
        else:
            array[l] = a3[k]
            k = k + 1
        l = l + 1

    #CASE a1 left
    while i < len(a1):
        array[l] = a1[i]
        i = i + 1
        l = l + 1

    #CASE a2 left
    while j < len(a2):
        array[l] = a2[j]
        j = j + 1
        l = l + 1
    
    #CASE a3 left
    while k < len(a3):
        array[l] = a3[k]
        k = k + 1
        l = l + 1

   

#def mergesort3(array, destarray, lo, hi):
def mergesort3(array):
    
    n = len(array)
    lo = 0
    m1 = int(n/3)
    m2 = int(m1*2)
    hi = n-1
    a1 = []
    a2 = []
    a3 = []
    if (n < 2):
        return
    elif (n == 2):
        v1 = array[0]
        v2 = array[1]
        if v1 > v2:
            array[0] = v2
            array[1] = v1
    else:

        x = lo
        for i in range(lo, m1):                   # populate
            value = array[x]
            a1.append(value)
            x = x + 1

        for j in range(m1, m2):                   # populate
            value = array[x]
            a2.append(value)
            x = x + 1

        for k in range(m2, n):              # populate
            value = array[x]
            a3.append(value)        
            x = x + 1

        #if (n%2) == 0:
        #    a3.append(array[x])

        mergesort3(a1)
        mergesort3(a2)
        mergesort3(a3)
        merge3(array, a1, a2, a3)
    


nvals = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
for n in nvals:
    array = []
    for i in range(0, n):
        array.append(random.uniform(0, 10000))
    start = time.time()
    mergesort3(array)
    end = time.time()
    print("\nn: ", n, "\ntime: ", end-start)
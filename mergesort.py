
def merge(array, left, right):
    i = 0
    j = 0
    k = 0

    while (i < len(left) and j < len(right)):
        if(left[i]<right[j]):
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1
        
        k = k+1
    
    while (i < len(left)):
        array[k] = left[i]
        i = i+1
        k = k+1
    
    while (i < len(right)):
        array[k] = right[j]
        j = j+1
        k = k+1


def mergesort(array):
    n = len(array)
    if (n<2):
        return
    
    mid = int(n/2)
    left = []
    right = []
    for i in range(0, mid):
        value = array[i]
        left.append(value)
    for j in range(mid, n):
        value = array[j]
        right.append(value)
    mergesort(left)
    mergesort(right)
    merge(array, left, right)

file = open("data.txt", "r")
lines = file.readlines()
for line in lines:
    master_n = int(line[0])
    array = []
    first_skipped = False
    temp_num = ""
    for char in line:
        if first_skipped:
            if not char == " " and not char == "\n":
                temp_num = temp_num + char
            else:
                if not temp_num == "":
                    array.append(int(temp_num))
                    temp_num = ""
        else:
            first_skipped = True
        
    if not temp_num == "":
        array.append(int(temp_num))
    
    first_skipped = False
    print("Given array is") 
    for i in range(master_n): 
        print(array[i], " ", end='')
    print()
    mergesort(array)
    print("Sorted array is") 
    for i in range(master_n): 
        print(array[i], " ", end='')
    print("\n")
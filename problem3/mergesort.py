# merge logic
def merge(array, left, right):
       i = 0 # left array ptr
       j = 0 # right array ptr
       k = 0 # merged array ptr

       while i < len(left) and j < len(right): # iterate through both l and r arrays
           if left[i] < right[j]:              # if left value smaller
               array[k] = left[i]              # put it into merged array
               i = i + 1                       # iterate left ptr
           else:
               array[k] = right[j]             # otherwise right ptr is smaller, put it into merged array
               j = j + 1                       # iterate right ptr
           k = k + 1                           # iterate merged ptr

       while i < len(left):                    # while we are still in the left array
           array[k] = left[i]                  # slap the rest of the values in the merged array. only reach here if we know it will be valid
           i = i + 1
           k = k + 1

       while j < len(right):                   # while we are still in the right array
           array[k] = right[j]                 # slap the rest of the values in the merged array. only reach here if we know it will be valid
           j = j + 1
           k = k + 1

# mergesort splitting
def mergesort(array):
    n = len(array)
    if (n < 2):
        return                                # we are done
    
    mid = int(n/2)                            # partition array into two
    left = []
    right = []
    for i in range(0, mid):                   # populate the two half arrays
        value = array[i]
        left.append(value)
    for j in range(mid, n):
        value = array[j]
        right.append(value)
    mergesort(left)                           # recur the left array, splitting until we hit base case of 2
    mergesort(right)                          # recur the right array, splitting until we hit base case of 2
    merge(array, left, right)                 # merge em all back, sorting along the way


# required file io
file = open("data.txt", "r")
lines = file.readlines()
file.close()
file = open("merge.txt", "w")
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
    print("init array") 
    for i in range(master_n): 
        print(array[i], " ", end='')
    print()
    mergesort(array)
    print("sorted array") 
    for i in range(master_n): 
        print(array[i], " ", end='')
        file.write(str(array[i]))
        file.write(' ')
    file.write("\n")
    print("\n")
file.close()
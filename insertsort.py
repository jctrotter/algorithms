# actual insertion
def insert(array, index):                       # insert array at given point
    try:
        while(array[index+1] < array[index]):
            x = array[index]                    # pop the values out and swap them
            y = array[index+1]
            array[index] = y
            array[index+1] = x
            index = index + 1
    except IndexError as e:                     # end of the array
        return

# insertion sort
def insertsort(array):
    for i in range(0, len(array)):              # iterate through array
        try:
            if array[i+1] < array[i]:           # if array not sorted
                insert(array, i)                # insert i into the list
                insertsort(array)               # start the sort over
                break
        except IndexError as e:
            return


# required file io and string parsing
file = open("data.txt", "r")
lines = file.readlines()
file.close()
file = open("insert.txt", "w")
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
    insertsort(array)
    print("Sorted array is") 
    for i in range(master_n): 
        print(array[i], " ", end='')
        file.write(str(array[i]))
        file.write(' ')
    file.write("\n")
    print("\n")
file.close()
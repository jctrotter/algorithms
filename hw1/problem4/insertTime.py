# actual insertion
import random, time
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
nvals = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
for n in nvals:
    for i in range(0, n):
        array = []    
        array.append(random.uniform(0, 10000))
    start = time.time()
    insertsort(array)
    end = time.time()
    print("\nn: ", n, "\ntime: ", end-start)

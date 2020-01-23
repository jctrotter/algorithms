# merge logic
import random, time
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
nvals = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000]
for n in nvals:
    for i in range(0, n):
        array = []    
        array.append(random.uniform(0, 10000))
    start = time.time()
    mergesort(array)
    end = time.time()
    print("\nn: ", n, "\ntime: ", end-start)

import time
import random



def recursive(W, n, wt, val):
    # W: Bag capacity
    # n: Object
    
    # Base case
    if n == 0 or W == 0:
        return 0
    
    if wt[n-1] > W:
        return recursive(W, n-1, wt, val)
    else:
        return max(val[n-1]+recursive(W-wt[n-1], n-1, wt, val), recursive(W, n-1, wt, val))

def dynamic(W, n, wt, val):
    # W: Bag capacity
    # n: Object

    # construct 2d array
    A = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # populate array
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                A[i][w] = 0
            elif wt[i-1] <= w: 
                A[i][w] = max(val[i-1] + A[i-1][w-wt[i-1]], A[i-1][w]) 
            else: 
                A[i][w] = A[i-1][w] 
  
    return A[n][W] 
  
init_n = [24,24,24,24,24,24,24,24]
init_W = [6,9,12,15,18,21,24,27]

wt = []
val = []
for x in range(0,len(init_n)):
    wt = []
    val = []
    for z in range(0, init_n[x]):
        wt.append(int(random.uniform(0,50)))
    for y in range(0, init_n[x]):
        tval = int(random.uniform(0,50))
        if tval < wt[y]:
            tval = tval + 1
        val.append(tval)

    d_start = time.time()
    d_value = dynamic(init_W[x], init_n[x], wt, val)
    d_end = time.time()
    d_time = round(d_end-d_start, 4)

    r_start = time.time()
    r_value = recursive(init_W[x], init_n[x], wt, val)
    r_end = time.time()
    r_time = round(r_end-r_start, 4) 
    print("n:",init_n[x], ", W:", init_W[x], ", r_time:", r_time, ", r_max:", r_value, ", d_time:", d_time, " , d_max:", d_value)
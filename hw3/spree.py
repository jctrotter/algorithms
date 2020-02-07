
max_values = []
def dynamic_spree(fam, usd, lbs):
    n = len(usd)
    fam_totals = []
    z = 0
    running_fam_sum = 0
    for S in fam:
        z = z+1
        A = [[0 for x in range(S+1)] for x in range(n+1)]
        holding = []
        for i in range(n+1):
            for s in range(S+1):
                if i == 0 or s == 0:
                    A[i][s] = 0
                elif lbs[i-1] <= s:
                    A[i][s] = max(usd[i-1]+A[i-1][s-lbs[i-1]],A[i-1][s])
                else:
                    A[i][s] = A[i-1][s]

        #find items
        p = n
        k = S
        #try:
        while not p <= 0 and not k <= 0:
            if not A[p][k] == A[p-1][k]: # TODO - take another look at this
                holding.append(p)
                p = p - 1
                k = k - lbs[i-1]
            else:
                p = p - 1
        #except Exception as e:
        #   pass
        fam_holding = str(z) + ": "
        for item in holding:
            fam_holding = fam_holding + str(item) + " "
        fam_totals.append(fam_holding)
        running_fam_sum = running_fam_sum + A[n][S]
        
    max_values.append(running_fam_sum)
    return fam_totals


# T is on first line of input file, T = number of test cases
# 2 - T
# 3 - N - number of items in test case 1
# 71 17 - test case 1 - P and W - price and weight for an object
# 44 23 - test case 2
# 31 24 - test case 3
# 1 - F - num family members
# 26 - dude carries 26 lbs
# 6 - Number of items in test case 2
# 64 26
# 85 22
# 52 4
# 99 18
# 39 13
# 54 9
# 4 - 4 family members F
# 23
# 20
# 20
# 36

fp = open("./hw3/shopping.txt")
line = int(fp.readline())
T = line # T - number of test cases

totals = []

for i in range(T):
    usd = []
    lbs = []
    fam = []
    N = int(fp.readline())
    for j in range(N):
        line = fp.readline()
        pw = line.split(" ")
        usd.append(int(pw[0]))
        lbs.append(int(pw[1]))
    F = int(fp.readline())
    for k in range(F):
        fam.append(int(fp.readline()))
        
    totals.append(dynamic_spree(fam, usd, lbs))

for l in range(T):
    print()
    print("Test case ", l+1)
    print("Total price: ", max_values[l])
    print("Member items: ")
    for member in totals[l]:
        print(member)
    
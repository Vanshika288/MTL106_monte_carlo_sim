"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def prb(alice_wins,bob_wins,L):
    x=0
    y=0
    if not (L[alice_wins][bob_wins]==-1):
        return L[alice_wins][bob_wins]
    if alice_wins>1:
        x = prb(alice_wins-1,bob_wins,L)
    if bob_wins>1:
        y = prb(alice_wins,bob_wins-1,L)
    L[alice_wins][bob_wins] =  mod_add(mod_multiply(x,mod_divide(bob_wins,bob_wins+alice_wins-1)) , mod_multiply(y,mod_divide(alice_wins,bob_wins+alice_wins-1)))
    return L[alice_wins][bob_wins]
    pass
def calc_prob(alice_wins, bob_wins):
    if alice_wins==1 and bob_wins==0:
        return 1
    if alice_wins==0 and bob_wins==1:
        return 0

    n = alice_wins+1
    m = bob_wins+1
    L = []
    for i in range(0,n):
        temp = []
        for j in range(0,m):
            temp.append(-1)
        L.append(temp)
    for i in range(2,n):
        L[i][0]=0
    for j in range(0,m):
        L[0][j]=0
    L[1][0]=1
    L[1][1]=1
    return prb(alice_wins,bob_wins,L)


# Problem 1b (Expectation)
def exp(alice_wins,bob_wins,ans,L):
    x=0
    y=0
    if not (L[alice_wins][bob_wins]==-1):
        return 1*L[alice_wins][bob_wins]
    if alice_wins>1:
        x = prb(alice_wins-1,bob_wins,L)
    if bob_wins>1:
        y = prb(alice_wins,bob_wins-1,L)
    L[alice_wins][bob_wins] =  mod_add(mod_multiply(x,mod_divide(bob_wins,bob_wins+alice_wins-1)) , mod_multiply(y,mod_divide(alice_wins,bob_wins+alice_wins-1)))
    ans[0]+=mod_add(mod_multiply(x,mod_divide(bob_wins,bob_wins+alice_wins-1)) , mod_multiply(-1*y,mod_divide(alice_wins,bob_wins+alice_wins-1)))
    return L[alice_wins][bob_wins]
def calc_expectation(t):
    n= t+1
    m = t+1
    L = []
    for i in range(0, n):
        temp = []
        for j in range(0, m):
            temp.append(-1)
        L.append(temp)
    for i in range(2, n):
        L[i][0] = 0
    for j in range(0, m):
        L[0][j] = 0
    L[1][0] = 1
    L[1][1] = 1
    prb(t, t, L)
    final_ans = 0
    for i in range(1, t):
        final_ans = mod_add(mod_multiply((2 * i - t), L[i][t - i]), final_ans)
    return final_ans



# Problem 1b (Variance)
def calc_variance(t):
    n = t + 1
    m = t + 1
    L = []
    for i in range(0, n):
        temp = []
        for j in range(0, m):
            temp.append(-1)
        L.append(temp)
    for i in range(2, n):
        L[i][0] = 0
    for j in range(0, m):
        L[0][j] = 0
    L[1][0] = 1
    L[1][1] = 1
    prb(t, t, L)
    final_ans=0
    for i in range(1, t):
        final_ans =mod_add(mod_multiply(((2*i-t)*(2*i-1)),L[i][t-i]),final_ans)
    return final_ans
    
print(calc_prob(97,46))
print(calc_expectation(46))
print(calc_variance(46))
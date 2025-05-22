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

# Problem 3b
def max_exp(na, nb , rounds,memo):
    if (na,nb,rounds) in memo:
        return memo[(na,nb,rounds)]
    if rounds==0:
        return [-1,0]
    p = max_exp(na,nb+1,rounds-1,memo)
    x = p[1]
    q = max_exp(na+1,nb,rounds-1,memo)
    y = q[1]
    r = max_exp(na+0.5,nb+0.5, rounds-1,memo)
    z = r[1]
    a = (127/110 + (nb)/(nb+na))/3 + ((127/110 + (nb)/(nb+na))/3)*y + ((3/10+6/11+na/(na+nb))/3)*x
    b = (3/10 + 1/3 +1/6 + 3/10 +1/4)/3 + ((3/10+1/3+3/10)/3)*y + ((7/10+1/3+1/5)/3)*x + ((1/3+1/2)/3)*z
    c = (6/11 + 1/5 +1/4 + 1/10 +2/5)/3 + ((6/11+1/5+1/10)/3)*y + ((5/11+3/10+1/10)/3)*x + ((1/2+4/5)/3)*z
    if a>b and a>c:
        memo[(na,nb,rounds)] = [0,a]
        return [0,a]
    if b>a and b>c:
        memo[(na,nb,rounds)] = [1,b]
        return [1,b]
    if c>a and c>b:
        memo[(na,nb,rounds)] = [2,c]
        return [2,c]
    
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive

    """

    memo = {}
    ans = max_exp(na,nb,tot_rounds,memo)
    exp = ans[1]
    strategy = ans[0]
    L=[]
    if strategy==0:
        return [1,0,0]
    elif strategy==1:
        return [0,1,0]
    else :
        return [0,0,1]
    pass

def expected_points(tot_rounds):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    memo={}
    # print(max_exp(1,1,tot_rounds,memo))
    return max_exp(1,1,tot_rounds-2,memo)[1]+1
    pass


print(expected_points(6))
'''
Given: Three positive integers k+ m, and n, representing a population containing k+m+n
 organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''

# solution

'''we need to define the probabilities of each pair
 
 let k = K (homozygous dominant)
 let m = mM(heterozygous dominant)
 let n = n (homozygous recessive)

 there are 5 possibilities that the outcome will have dominant allele

 1. KxK
 2. KxmM
 3. Kxn
 4. mMxmM
 5. mMxn
 '''

def dominant(k, m, n):
    total = k + m + n

    # probability of KxK
    pK = (k/total) * ((k-1)/(total-1))
    # probalilty of KxmM
    pKm = k/total * m/(total-1) * 2 # 2 ways to pick m
    #probability of Kxn
    pKn = k/total * n/(total-1) * 2 # 2 ways to pick n
    # probability of mMxmM
    pmM = (m/total) * ((m-1)/(total -1)) * 0.75 # because mM has 4 possible outcomes out of which 3 are dominant
    # probability of mMxn
    pMn = (m/total) * n/(total-1) * 2* 0.5 # because 2 ways to pick and mMxnn has 4 outcomes out of which 2 are dominant

    return pK + pKm + pKn + pmM + pMn

k, m, n = 16, 19, 17
print(dominant(k, m, n))

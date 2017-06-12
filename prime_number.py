def getPrime (num):
    notPrime=[]
    isPrime = []
    if type(num)!=int:
        raise TypeError
    for j in range(2,num):
        for i in range(2,j):
            if j % i == 0:
                notPrime.append(j)
    for i in range(2,num):
        if i not in notPrime:
            isPrime.append(i)
    return isPrime
print (getPrime(10))
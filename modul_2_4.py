numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes  = []      #  только простые числа
not_primes = []   #  все не простые числа

for i in numbers :
    is_prime =  True
    if i != 1:
        for j in range(2,i,1) :
            if  i % j == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(i)
        else:
            not_primes.append(i)


print('primes ', primes )
print('not_primes ', not_primes)
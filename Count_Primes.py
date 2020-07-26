num = 10

i = 2
x = 0
prime_factor = []
non_prime_factor = []

for i in range(2, num):
 for k in range(2, num):
  if ((i % k) == 0) and (i != k):
   print(i, ' is not a prime number')
   non_prime_factor.append(i)
   break
  if (i % k) != 1 and (i != k): 
   print(i, ' is a prime number')
   prime_factor.append(i)
   break
print('Prime numbers before:  ', num)   
print(prime_factor)
print('Non Prime numbers before:  ', num)
print(non_prime_factor)
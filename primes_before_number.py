#get primes before any number


num = 10
final = []


for i in range(1, num + 1):
   
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           final.append(i)
           
print(final)
    



 
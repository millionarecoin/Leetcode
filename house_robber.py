#house robber
nums = [1, 2, 3, 1]
#nums = [2,7,9,3,1, 5, 7, 8]
#nums = [2,7,9,3,1]
res = []
total = nums[0]
for i in range(len(nums) -2):
 #print('(i + 2):  ', (i + 2))
 #print('lenght:  ', len(nums))
 if (i % 2) == 0 and (i + 2) <=  len(nums):
  
  #print('numbers:  ', nums[i + 2])
  total = total + nums[i + 2]
  #print('total 1: ', total)
  res.append(total)
 


total = nums[1]
for j in range(len(nums) -1):
 #print('(i + 2):  ', (i + 2))
 #print('lenght:  ', len(nums))
 if (j % 2) == 1 and (j + 2) <  len(nums):
  print('j:  ', j)
  print('(j % 2) :  ', (j % 2) )
  print('numbers:  ', nums[j])
  total = total + nums[j + 2]
  #print('total 1: ', total)
  res.append(total)


  
  
res.sort
print(max(res))
 
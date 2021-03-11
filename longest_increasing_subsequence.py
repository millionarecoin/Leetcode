#longest increasing subsequence
nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
res = []
highest = max(nums)
for i in range(len(nums) -1):
 if nums[i] < nums[i + 1]:
  res.append(nums[i])

if highest in res:
 print(test)
else:
 res.append(highest)
 
print(res)
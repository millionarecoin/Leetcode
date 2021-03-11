#subarray sum equals k
#nums = [1, 1, 1, 2, 2]
nums = [1, 2, 3]

count = 0
target = 3
for i in range(len(nums) -1):
 #for j in range(i + 1, len(nums)):
  if nums[i] + nums[i + 1] == target:
   count = count + 1
  if i > 0:
   if nums[i + 1] == target:
    count = count + 1

  if i == 0:
   if nums[i] == target:
    count = count + 1

   
print('total possible combinations:  ', count)
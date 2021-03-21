#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

 

#Example 1:

#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]

nums = [0, 1, 0, 3, 12]

print('length of nums:  ', len(nums))
count = 0
for i in range(len(nums) -1):
 print('i:  ', i)
 
 if nums[i] == 0:
  count = count + 1
  
  


 
for i in range(0, count):
 nums.remove(0)
 nums.append(0)
 
print(nums)
  
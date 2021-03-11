nums = [2, 7, 7, 11, 15, 15, 17, 17, 7, 11, 17, 2]
duplicate = []
reverse = []
all_duplicates = []
remove_all_duplicates = []
sum = 0
total = 0
print('length of nums:  ', len(nums))

for i in range(len(nums) -1):
 total = sum + int(i)
 #print("total:  ",total)
 #print("sum:  ", sum)
 print("i:  ", nums[i])
 print("i + 1:  ", nums[i + 1])
 if nums[i] == nums[i + 1]:
  duplicate.append(nums[i])
 reverse.insert(0, nums[i + 1])
for i in nums: 
 if i not in all_duplicates: 
  all_duplicates.append(i) 
 
reverse.insert(len(nums), nums[0]) 

nums.sort()
x = set(nums)
for i in x:
 if (nums.count(i)) > 1:
  remove_all_duplicates.append(i)



print('duplicates list')
print(duplicate)
print('reverse array')
print(reverse)
print('all duplicates gone')
print(all_duplicates)
print('non duplicate rows only')
print('remove all duplicates')
print(remove_all_duplicates)
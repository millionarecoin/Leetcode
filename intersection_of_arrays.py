#intersection of two arrays

#two sum
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
res = []
remove_all_duplicates1 = []
remove_all_duplicates2 = []
#target = 9


nums1.sort()
x = set(nums1)
for l in x:
 if (nums1.count(l)) > 1:
  remove_all_duplicates1.append(l)

nums2.sort()
y = set(nums2)
for k in y:
 if (nums2.count(k)) > 1:
  remove_all_duplicates2.append(k)
  
  
for i in range(len(remove_all_duplicates1)):
 for j in range(len(remove_all_duplicates2)):
  if remove_all_duplicates1[i] == remove_all_duplicates2[j]: 
   res.append(remove_all_duplicates1[i])
   
print(res)
  
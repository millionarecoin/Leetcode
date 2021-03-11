#group anagrams
# Python3 code to demonstrate
# Grouping Anagrams
# using defaultdict() + sorted() + values()
from collections import defaultdict
 
# initializing list
test_list = ['lump', 'eat',  'me',  'tea', 'em', 'plum']
 
# printing original list
print("The original list : " + str(test_list))
 
# using defaultdict() + sorted() + values()
# Grouping Anagrams
temp = defaultdict(list)
for ele in test_list:
    print('ele:  ', ele)
    print('temp[str(sorted(ele))]:  ', temp[str(sorted(ele))])
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())
 
# print result
print("The grouped Anagrams : " + str(res))
#Given two strings s and t, check if s is a subsequence of t.

#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

#Example 1:

#Input: s = "abc", t = "ahbgdc"
#Output: true
#Example 2:

#Input: s = "axc", t = "ahbgdc"
#Output: false


s = 'aec'
t = 'abcde'
output  = []
for i in range(0, len(s)):
 result = t.find(s[i])
 if result >= 0:
  output.append(result)
#print(result)
print('output:  ', output)
output_sort = output.copy()
output_sort.sort()
print('output sort:  ', output_sort)

if len(output) == len(s) and output == output_sort:
 print('s is part of t')
 
 
#first non repeating character
s = "lavereetcode"
res = []
for i in range(0, len(s) -1):
 for j in range(i + 1, len(s)):
  if s[i] == s[j]:
   print('position:  ', i -1)
   res.append(i - 1)
   
res.sort
print("1st position:  ", res[0])
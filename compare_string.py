s1 = 'mary'
s2 = 'armmy'
output = ''
if len(s1) == len(s2):
 for i in range(len(s1)):
  for j in range(len(s2)):
 
  #print('s1[i]:  ', s1[i])
   #print('s2[j]:  ', s2[j])
   if s1[i] == s2[j]:
    output = output + s1[i]


if output == s1:
 print('both strings are anagrams')
else:
 print('both strings are not anagrams')
  
#17. Letter Combinations of a Phone Number


#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

#A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

a = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
#num = input('input a number:  ')
num = 23
num = str(num)
result = []
output = ''
final = ''
total_output = []
for i in range(len(num)):
 #print('num[i]:  ', num[i])
 if int(num[i]) > 1:
  j = int(num[i]) - 2
  #print(a[j])
  result.append(a[j])
 if int(num[i]) == 1:
  #result.append(1)
 
 if int(num[i]) == 0:
  #result.append(0)
 
 
print(result)

for i in range(len(result) -1):
 output = result[i]
 output_next = result[i + 1]
 for j in range(len(output)):
  for k in range(len(output_next)):
   final = output[j] + output_next[k]
   total_output.append(final)
   
   #print(final)
   
print(total_output)
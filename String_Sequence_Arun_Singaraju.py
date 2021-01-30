#1. Requirements
#- Get a list of sequence
#- Print out the sequence and its occurrences
#- The string will be more than 1 and not more than 20 in size
#- The input should be Alphabet A-Z
#- No special characters allowed
#- No numbers allowed
#- No blank allowed
##2. Read in input string
#3. PyTest as Unit Test
#4. Example: AABBBBBBZZDACCAA --> A2B6Z2D1A1C2A2
 
 
val = input("Enter your value: ") 
#print(val) 
if (len(val) > 20) or (len(val) < 1):
 print('please enter a value less than 20 characters')
count = 1
final_output = ''
#print('should print A only:  ', val[2])
for i in range(0, len(val) -1):
 #print('val[i]:  ]', val[i])
 val_ascii = ord(val[i])
 #print('ascii: ', val_ascii)
 #print('val[i + 1]:  ]', val[i + 1])
 val_ascii_last = ord(val[i + 1])
 #print('ascii_last:  ', val_ascii_last)
  
 if (val_ascii > 64 and val_ascii < 91) and (val_ascii_last > 64 and val_ascii_last < 91):
  while val[i] == val[i + 1]:
   count = count + 1
   letter = val[i]
   #print('val[i]:  ',  val[i])
   #print('val[i+1]:  ',  val[i+1])
   #print('letter:  ', letter)
   #print('count:  ', count)
   #print('checking last value', i + 1)
   #print('checking length', len(val))
   if (i + 2) == len(val):
    final_output = final_output + letter + str(count)
   break
  else:
   #print('else condition val[i]:  ',  val[i])
   #print('else condition val[i+1]:  ',  val[i + 1])
   #print('count in else condition:  ', count)
   final_output = final_output + letter + str(count)
   count = 1 
   if (i + 2) == len(val):
    final_output = final_output + val[i + 1] + str(count)
  #print('breaking while loop:  ', letter)
  
 else:
  print('pleaser enter a valid string which does not have special characters or lower case letters')
  final_output = ''
  break
if final_output != '':
 print('final_output:  ', final_output)  

  
 
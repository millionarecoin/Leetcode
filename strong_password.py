#strong password checker
#A password is considered strong if the below conditions are all met:

#It has at least 6 characters and at most 20 characters.
#It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
#It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
#Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

#In one step, you can:

#Insert one character to password,
#Delete one character from password, or
#Replace one character of password with another character.


val = input("Enter your password: ") 
count = 1
final_output = ''
#print(val) 
if (len(val) > 5) or (len(val) < 21):
 for i in range(0, len(val) -1):
  val_ascii = ord(val[i])
  #print('val[i]:  ', val[i])
  #print('val_ascii:  ', val_ascii)
  val_ascii_last = ord(val[i + 1])
  #print('val[i + 1]:  ', val[i + 1])
  #print('val_ascii last:  ', val_ascii_last)
  if ((val_ascii > 64 and val_ascii < 91) and (val_ascii_last > 64 and val_ascii_last < 91)) or ((val_ascii > 96 and val_ascii < 123) and (val_ascii_last > 96 and val_ascii_last < 123)) or ((val_ascii > 47 and val_ascii < 57) and (val_ascii_last > 47 and val_ascii_last < 57)):
   while val[i] == val[i + 1]:
    count = count + 1
    letter = val[i]
    if count > 2:
     print('You cannot have 3 repeating characters')
    break
     
    if (i + 2) == len(val):
     final_output = final_output + letter + str(count)
    break
   else:
    if count > 2:
     print('You cannot have 3 repeating characters')
    break
    final_output = final_output + letter + str(count)
    count = 1 
    if (i + 2) == len(val):
     final_output = final_output + val[i + 1] + str(count)
    
    
  else:
   print('Enter password which contains at least one lowercase letter, at least one uppercase letter, and at least one digit')
   final_output = ''
  break
 else:
  print('Enter password at least 6 characters and at most 20 characters')
  final_output = ''
 
if final_output != '':
 print('Your password is good final_output:  ', final_output)  
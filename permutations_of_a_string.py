#permutations of a string
#val = input("Enter your string: ") 
val = 'abcd'
remove_dups = ''

if val is not None: 
 val = str(val)
else:
 #print('string is empty')
 exit

#for i in range(0, len(val) -1):
 #print('string parameter:  ', val[i]) 
# i = i + 1
 
# Python code to demonstrate  
# to find all permutation of 
# a given string 
  
# Initialising string 
ini_str = "abcd"
  
# Printing initial string 
print("Initial string", ini_str) 
  
# Finding all permuatation 
result = [] 
  
def permute(data, i, length):  
    print('i:  ', i)
    print('length:  ', length)
    if i == length:  
        result.append(''.join(data) ) 
        print('test')
    else:  
        for j in range(i, length):  
            # swap 
            print('data[i]', data[i])
            print('data[j]', data[j])
            print('data:  before', data)
            data[i], data[j] = data[j], data[i]  
            print('data:  after', data)
            permute(data, i + 1, length)  
            data[i], data[j] = data[j], data[i]   

print('list of string:  ', list(ini_str))
permute(list(ini_str), 0, len(ini_str)) 

  
# Printing result 
print("Resultant permutations", str(result)) 
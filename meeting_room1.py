#There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
#What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


#Example 1:

#Input:
#N = 6
#S[] = {1,3,0,5,8,5}
#F[] = {2,4,6,7,9,9}
#Output: 
#4
#Explanation:
#Four meetings can be held with
#given start and end timings.


start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
start_backup = start.copy()
finish_backup = finish.copy()
count = 0
for i in range(len(start)):
 if  i > 0 and start[i]  < finish[i -1] and i < len(start_backup):
  if start_backup[i]  < finish_backup[i -1]: 
   start_backup.pop(i)
   finish_backup.pop(i)
 
if start_backup[len(start_backup) -1]  < finish_backup[len(start_backup) -2]:
 start_backup.pop(i -1)
 finish_backup.pop(i - 1)
 
 
print('start backup output', start_backup)  
print('finish backup output', finish_backup)  

print('maximum number:  ', len(start_backup))
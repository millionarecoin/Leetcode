#subset of a list
l = [1, 2, 3]
base = []
lists = [base]
for i in range(len(l)):
 orig = lists[:]
 new = l[i]
 print('new:  ', new)
 print('orig:  ', orig)
 print('lists:  ', lists)
 for j in range(len(lists)):
  lists[j] = lists[j] + [new]
 lists = orig + lists
print(lists)
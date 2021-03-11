# Linked list
class LinkedList:
 def __init__(self)"
  self.head = None
  
 def __repr__(self):
  node = self.head
  nodes = []
  while node is not None:
   nodes.append(node.data)
   node = node.next
  nodes.append("None")
  return " -->  ".join(nodes)
  
 def traverse_list(self):
  if self.head is None:
   print("List has no element")
   return
  else:
   n = self.head
   print("n:  ", n)
   while n is not None:
    print(n.item, " ")
    n = n.ref
  

class Node:
 def __init__(self, data):
  self.item = data
  self.next = None
  self.ref = None
  
 def  __repr__(self):
  return self.data
  
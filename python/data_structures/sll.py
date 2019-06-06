class SLNode:
  def __init__(self, val):
    self.value = val
    self.next = None
  
  def __repr__(self):
    return f'{self.value}'

class SList:
  def __init__(self):
    self.head = None

  def add_to_front(self, val):
    node = SLNode(val)
    node.next = self.head
    self.head = node
    return self

  def add_to_back(self, val):
    if self.head == None:
      self.add_to_front(val)
      return self
    new_node = SLNode(val)
    runner = self.head
    while runner.next != None:
      runner = runner.next
    runner.next = new_node
    return self

  def remove_from_front(self):
    remove_from_list = self.head
    self.head = self.head.next
    return remove_from_list

  def remove_from_back(self):
    runner = self.head
    while runner.next.next != None: 
      runner = runner.next 
      
    runner.next = None
    
  def remove_val(self, val):
    runner = self.head
    while runner.value != val:
      prev = runner
      runner = runner.next
    prev.next = runner.next
    return self 
  
  def counter(self):
    counter = 1
    runner = self.head
    while runner.next != None:
      runner = runner.next
      counter += 1
    return counter

  def insert_at(self, val, n):
    count = self.counter()
    if n == 1:
      self.add_to_front(val)
    elif n == self.counter():
      self.add_to_back(val)
    else:
      runner = self.head
      count = 1
      while runner.next != None and count != n:
        prev = runner
        runner = runner.next
        count+=1
        if count == n:
          new_node = SLNode(val)
          new_node.next = runner
          prev.next = new_node

  def print_values(self):
    runner = self.head
    
    while runner != None: 
      print(runner)
      runner = runner.next
    return self

  def __repr__(self):
    return f'{self.head}'



new_list = SList()
# new_list.add_to_front('test')
# new_list.add_to_front('test1')
# print(new_list)
# new_list.add_to_back('test2')

new_list.add_to_front('a').add_to_back('b').add_to_back('c').add_to_back('d').add_to_back('e').add_to_back('f').add_to_back('g')
print('------- Original remove from front -----------')
new_list.print_values()
new_list.remove_from_front()
print('------- After remove from front -----------')
new_list.print_values()
new_list.remove_from_back()
print('------- After remove from last -----------')
new_list.print_values()
print('------- After remove val from last -----------')
new_list.remove_val('e')
new_list.print_values()
print('------- After insert at front -----------')
new_list.insert_at('z', 1)
new_list.print_values()
print('------- After insert at end -----------')
new_list.insert_at('k', 5)
new_list.print_values()
print('------- After insert at in the middle -----------')
new_list.insert_at('p', 4)
new_list.print_values()
print(new_list.counter())
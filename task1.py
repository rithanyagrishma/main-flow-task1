#list
list1 = [3, 7, 11, 2, 8]
print("Original list:", list1)
#add
list1.append(9)
print("List after adding an element:", list1)
#del
list1.remove(2)
print("List after removing an element:", list1)
#modify
list1[2] = 15
print("List after modifying an element:", list1)

#dictionary
dict1 = {'x': 6, 'y': 12, 'z': 14}
print("\nOriginal dictionary:", dict1)
#add
dict1['w'] = 7
print("Dictionary after adding an element:", dict1)
#delete
del dict1['y']
print("Dictionary after removing an element:", dict1)
#modify
dict1['z'] = 25
print("Dictionary after modifying an element:", dict1)

#set
set1 = {4, 12, 15, 18, 3}
print("\nOriginal set:", set1)
#add
set1.add(8)
print("Set after adding an element:", set1)
#delete
set1.remove(12)
print("Set after removing an element:", set1)
#modify
set1.discard(15)
set1.add(20)
print("Set after modifying an element:", set1)

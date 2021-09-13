# Lists
# same as array in other languages
# Lists are mutalble

mylist = [1, 2, 3, 4]
print(mylist)
mylist = [1, "String", True, [1, 2, 3, 4]]
print(mylist)

# Length of the list
print(len(mylist))

mylist = ['a', 'b', 'c', 'd', 'e']
print(mylist[0])
print(mylist[1])
print(mylist[-1])
print(mylist[1:])
print(mylist[:3])


# Reassignment at specific index
mylist = ['a', 'b', 'c', 'd', 'e']
print('before reassignment:')
print(mylist)
mylist[0] = 'NEW ITEM'
print('after reassignment:')
print(mylist)
print()

# Appending item to the end
mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append('NEW ITEM')
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append(['x', 'y', 'z'])
print(mylist)

# extending list
mylist = ['a', 'b', 'c', 'd', 'e']
mylist.extend(['x', 'y', 'z'])
print(mylist)

# Pop method of a list
# work as LIFO queue

mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop()
print(mylist)
print(item)
print()
item = mylist.pop(0)
print(item)

mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.reverse()
print(mylist)

mylist = [66, 4, 42, 33, 16]
item = mylist.sort()
print(mylist)
print()

# Nested list
mylist = [1, 2, ['x', 'y', 'z']]
print(mylist)
print(mylist[2])
print(mylist[2][2])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# List Comprehension
first_column = [row[0] for row in matrix]
print(first_column)

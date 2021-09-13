# Strings used to hold text information
# String are sequence of characters, meaning they can be indexed using bracket notation

# Basics

'hello'
"hello"

"I'm Ziad"

# Indexing

mystring = 'abcdefg h'

print(mystring)
print(mystring[0])
print(mystring[-1])
print(mystring[3])
print(mystring[2:])
print(mystring[4:])
# Note that up to but not including index 3
print(mystring[:3])
# cde
print(mystring[2:5])
# steps
print(mystring[::1])
print(mystring[::2])
# Strings are immutable, meaning item assignment to specific index is not allowed
# for example mystring[0] = 'X' is not allowed

# Basic Methods
print(mystring.upper())
print(mystring.capitalize())
print(mystring.split())
print(mystring.split('e'))

# Print Formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)
x = "Item One: {} Item Two: {}".format("dog", "cat")
print(x)
x = "Item One: {x} Item Two: {y}".format(x="dog", y="cat")
print(x)
x = "Item One: {y} Item Two: {x}".format(x="dog", y="cat")
print(x)
x = "Item One: {x} Item Two: {x}".format(x="dog", y="cat")
print(x)

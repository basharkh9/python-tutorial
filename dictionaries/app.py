# Same as Hash Table in other languages
# Allow us to create map of key-value pairs
# order is not retained

mystuff = {'key1': 123, 'key2': 'value2', 'key3': {'123': [1, 2, 'Grabe Me']}}
print(mystuff['key1'])
print(mystuff['key2'])
print(mystuff['key3']['123'][2])
print(mystuff['key3']['123'][2].upper())

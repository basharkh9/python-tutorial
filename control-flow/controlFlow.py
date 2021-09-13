if 1 < 2:
    print('Yes')


if 1 < 2:
    print('First Block')
    if 2 < 3:
        print('Second Block')

print()

if 1 > 2:
    print('if ran')
elif 3 == 3:
    print('elif ran')
else:
    print('else ran')


seq = [1, 2, 3, 4, 6, 7, 8, 9]

for item in seq:
    print(item)

print()

dict = {"Bashar": 1, "Ziad": 2, "Khaled": 3}

for key in dict:
    print(dict[key])

print()
for key in dict:
    print(key)
    print(dict[key])


mypairs = [(1, 2), (3, 4), (5, 6)]

for item in mypairs:
    print(item)

print()

for (tup1, tup2) in mypairs:
    print(tup1)
    print(tup2)

print()

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i+1

x = [1, 2, 3, 4]

out1 = []
for num in x:
    out1.append(num**2)
print(out1)
print()

out2 = [num**2 for num in x]
print(out2)

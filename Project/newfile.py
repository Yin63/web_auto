
name = "Jan"
age = 23
like = "basketball"

str_1 = '''
my name is {0}
my age is {1} 
I like {2}'''.format(name, age, like)

print(str_1)

print(like[3])

print(like[3:6:1])

print(like[::2])

print(type(age))

name_1 = isinstance(name, str)
print(name_1)

print(len(str_1))

print(str_1.replace("basketball", "running"))
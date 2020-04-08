""" Example 1 """
if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
    1 + 2
# result: 3

# 1 + "two"  # Now this is type checked, and a TypeError is raised
# result: TypeError: unsupported operand type(s) for +: 'int' and 'str'


""" Example 2 """
thing = "Hello"
print(type(thing))
# result: <class 'str'>

thing = 28.1
print(type(thing))
# result: <class 'float'>

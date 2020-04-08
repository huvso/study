import sys

N = 1000
print(sys.getsizeof(['aaaa', 1]))
print(sys.getsizeof(['aaaa', 'asdfasdfasdfasdf']))
assert sys.getsizeof(['aaaa', 1]) == sys.getsizeof(['aaaa', 'asdfasdfasdfasdf'])

test_lst_int = [i for i in range(0, N)]
test_lst_tuple = [(f"k{i}", i) for i in range(0, N)]
test_dict = {f"k{i}":i for i in range(0, N)}

print(f"sys.getsizeof(test_lst): {sys.getsizeof(test_lst_int)}")
print(f"sys.getsizeof(test_lst): {sys.getsizeof(test_lst_tuple)}")
print(f"sys.getsizeof(test_dict): {sys.getsizeof(test_dict)}")

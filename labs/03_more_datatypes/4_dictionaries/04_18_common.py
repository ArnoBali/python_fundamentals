'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}


'''

_dict1 = {"a": 1, "b": 2, "c": 3}
_dict2 = {"a": 2, "c": 4, "d": 2}
'''
a = _dict1.items()
b = _dict2.items()
print(b)


dict = {}

for key, value in _dict1:
    dict[key] = _dict1(value)+_dict2(value)

print(dict)
'''

dict_new = _dict1

for key, value in _dict2.items():
    if _dict1[key] == _dict2(key):
        _dict1[key] = value + _dict2(key)

print(dict_new)


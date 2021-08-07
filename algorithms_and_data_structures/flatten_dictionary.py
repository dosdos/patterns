def _flatten_helper(partial_dict, path):
    if isinstance(partial_dict, str) or isinstance(partial_dict, int):
        return partial_dict
    curr_dict = dict()

    for k in partial_dict.keys():
        if k is None or k == '':
            curr_dict = _flatten_helper(partial_dict[k], path)
        curr_path = f'{path}.{k}' if path else str(k)
        curr_val = partial_dict[k]
        if isinstance(curr_val, str) or isinstance(curr_val, int):
            curr_dict[curr_path] = curr_val
        else:
            new_dict = _flatten_helper(curr_val, curr_path)
            curr_dict.update(new_dict) if new_dict else curr_dict
    return curr_dict


def flatten_dictionary(dictionary):
    return _flatten_helper(dictionary, '')


d = {"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}
print(flatten_dictionary(d))
d = {"": {"a": "1"}, "b": "3"}
print(flatten_dictionary(d))
d = {'e': '1', 'd': '3'}
print(flatten_dictionary(d))
d = {"Key1": "1", "Key2": {"a": "2", "b": "3", "c": {"d": "3", "e": "1"}}}
print(flatten_dictionary(d))

"""
[[5, 1, 7, 6, 9, 8, 2, 3, 4],
 [2, 8, 9, 1, 3, 4, 7, 5, 6],
 [3, 4, 6, 2, 7, 5, 8, 9, 1],
 [6, 7, 2, 8, 4, 9, 3, 1, 5],
 [1, 3, 8, 5, 2, 6, 9, 4, 7],
 [9, 5, 4, 7, 1, 3, 6, 8, 2],
 [4, 9, 5, 3, 6, 2, 1, 7, 8],
 [7, 2, 3, 4, 8, 1, 5, 6, 9],
 [8, 6, 1, 9, 5, 7, 4, 2, 3]]
"""

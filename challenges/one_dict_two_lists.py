keys_str = ["name", "age", "city"]
values_str = ["Alice", "thirty", "New York"]

zipped_dict_str = dict(zip(keys_str, values_str)) # Zip is 0(1) and compiles in C

keys_int = [1,2,3]
values_int = [6,5,4]
zipped_dict_int = dict(zip(keys_int, values_int))

# Doing it as a list means it preserves duplicates

list_1 = [1,1,1,1,5,6,6,7]
list_2 = [2,2,2,6,58,6,8,3]

zipped_list = list(zip(list_1, list_2))

# tuples are faster than lists but that means they aren't changeable
list_1 = [1,1,1,1,5,6,6,7]
list_2 = [2,2,2,6,58,6,8,3]

zipped_tuple = tuple(zip(list_1, list_2))

# sort the zipped list

sorted_zipped_list = sorted(zipped_list, key=lambda x: (x[0], x[1]))

# sort the dictionary by key
sorted_zipped_dict_str_by_key = dict(sorted(zipped_dict_str.items(), reverse=True))
# sort the dictionary by value
sorted_zipped_dict_int_by_value = dict(sorted(zipped_dict_int.items(), key=lambda item: item[1]))

# str and int dict
str_int_dict = dict(zip(keys_str, values_int))
# sort by value
sorted_int_dict_str = dict(sorted(str_int_dict.items(), key=lambda x: x[1], reverse=True))
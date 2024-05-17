'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''



size=5
alphabeta = 'abcdefghijklmnopqrstuvwxyz'
size_alpha = alphabeta[:size]
working_alpha = size_alpha[::-1]
mid_string = size-1
length = ((size-1)*2)+1
width = (len('-'.join(size_alpha[1:]))*2)+3
half_width = int((width-1)/2)
for i in range(size):
    middle_char = working_alpha[i]
    lil_alpha = working_alpha[:i]
    chars_to_left = i
    if chars_to_left > 0:
        middle_string_i = lil_alpha + middle_char + lil_alpha[::-1]
        middle_string_with_dashes = '-'.join(middle_string_i)
    else:
        middle_string_with_dashes = middle_char
    added_half_width = int((width - len(middle_string_with_dashes))/2)
    print(f'{"-"*(added_half_width if length >1 else 0)}{middle_string_with_dashes}{"-"*(added_half_width if length >1 else 0)}')
for i in range(1,size):
    middle = len(middle_string_i) // 2
    middle_string = middle_string_i[:middle-i] + middle_string_i[middle+i:]
    middle_string_with_dashes = '-'.join(middle_string)
    added_half_width = int((width - len(middle_string_with_dashes))/2)
    print(f'{"-"*added_half_width}{middle_string_with_dashes}{"-"*added_half_width}')
        
'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''
number = 17
width = len(bin(number)[2:])
for i in range(1, number+1):
    print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))
# width = len(bin(number)[2:])
# for i in range(1, number):
#     print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].rjust(width)} {bin(i)[2:].rjust(width)}")
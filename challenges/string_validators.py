## built in 
# str.isalnum() checks to see if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# str.isalpha() checks to see if all the characters of a string are alphabetical (a-z and A-Z).
# str.isdigit() checks to see if all the characters of a string are digits (0-9).
# str.islower() checks to see if all the characters of a string are lowercase characters (a-z).
# str.isupper() checks to see if all the characters of a string are uppercase characters (A-Z).
s = 'qA2'
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
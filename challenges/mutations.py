string = 'abracadabra'
position = 5
character = 'k'

string_list = list(string)
string_list[position] = character
string = ''.join(string_list)
print(string)
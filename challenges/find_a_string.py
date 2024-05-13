string = 'TestCaseTestCase'
sub_string = 'CaseT'

sub_start = sub_string[0]
found = 0
for i in range(len(string)):
    if string[i] == sub_start and i+(len(sub_string)-1) <= len(string):
        new_string = []
        for ii in range(len(sub_string)):
            try:
                new_string.append(string[i+ii])
            except:
                new_string = []
        new_string = ''.join(new_string)
        if new_string == sub_string:
            found+=1
print(found)
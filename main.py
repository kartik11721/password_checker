import re

print('''\n-----!! Your Password Must Have !!-----
1. Minimum 8 characters.
2. The alphabets must be between [a-z]
3. At least one alphabet should be of Upper Case [A-Z]
4. At least 1 number or digit between [0-9].
5. At least 1 character from [ _ or @ or $ ].\n''')

password = input('Enter a password : ')
invalid = False
print('\n')

if (len(password)<8):
    invalid = True
    print('- password is too short')
if not re.search("[a-z]", password):
    invalid = True
    print('- atleast 1 lower case character is required')
if not re.search("[A-Z]", password):
    invalid = True
    print('- atleast 1 upper case character is required')
if not re.search("[0-9]", password):
    invalid = True
    print('- atleast 1 number [0-9] is required')
if not re.search("[_@$]", password):
    invalid = True
    print('- atleast 1 special character i.e _, @, $ is required')
if re.search("\s", password):
    invalid = True
    print('- password can not contain spaces')
if invalid == False:
    print("Valid Password")
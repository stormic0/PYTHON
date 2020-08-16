import re


email = input()
if re.search(r'.+\@.+\.\w{2,3}', email):
    print('OK')
else:
    print('WRONG')

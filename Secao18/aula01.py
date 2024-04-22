# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html
# https://github.com/luizomf/regexp-python
# findall    search    sub    compile

import re

string = 'Este é um teste de expressões regulares, teste'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'Abcd', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub(r'Abcd', string))

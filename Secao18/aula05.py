# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
import re

# from pprint import pprint


TEXTO = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
        '''

# print(re.findall(r'<([pdiv]{1,3})>.+?<\/\1>', TEXTO))
# tags = re.findall(r'(<([pdiv]{1,3})>.+?<\/\2>)', TEXTO)
# tags = re.findall(r'(<([pdiv]{1,3})>(.+?)<\/\2>)', TEXTO)
# tags = re.findall(r'<([pdiv]{1,3})>(?:.+?)<\/\1>', TEXTO)
# pprint(tags)

# for tag in tags:
#     um, dois, tres = tag
#     print(tres)

# cpf = '215.985.665-45'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([pdiv]{1,3})>(.+?)<\/\1>', TEXTO)
# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(.+?)<\/(?P=tag)>', TEXTO)
# pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS "\3" COISAS \4', TEXTO))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1\4', TEXTO))

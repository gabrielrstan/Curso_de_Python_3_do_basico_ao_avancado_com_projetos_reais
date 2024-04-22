# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
import re

TEXTO = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>
        '''

print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', TEXTO))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', TEXTO))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', TEXTO))

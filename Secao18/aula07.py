# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda
# \B -> não borda

from re import I, findall

TEXTO = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos
 atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de queijo
 nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu
 famoso pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
# print(findall(r'[a-z]+', TEXTO, flags=re.I))
# print(findall(r'[a-zA-Z]+', TEXTO))
# print(findall(r'[a-zA-Z0-9]+', TEXTO))
# print(findall(r'\w+', TEXTO, flags=re.A))
# print(findall(r'[a-zA-Z0-9À-ú]+', TEXTO))
# print(findall(r'\w+', TEXTO))
# print(findall(r'\W+', TEXTO))
# print(findall(r'\d+', TEXTO))
# print(findall(r'\D+', TEXTO))
# print(findall(r'\s+', TEXTO))
# print(findall(r'\S+', TEXTO))
# print(findall(r'\be\w+', TEXTO, flags=re.I))
# print(findall(r'\w+e\b', TEXTO, flags=re.I))
# print(findall(r'\b\w{4}\b', TEXTO, flags=re.I))
print(findall(r'flo\B', TEXTO, flags=I))

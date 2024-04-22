# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n


from re import I, S, findall  # , M

TEXTO = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

# print(findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', TEXTO, flags=M))

TEXTO2 = '''O João gosta de folia
E adora ser amado'''

print(findall(r'^o.*o$', TEXTO2, flags=I | S))

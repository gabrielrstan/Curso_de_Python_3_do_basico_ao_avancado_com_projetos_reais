"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Gabriel' #iteravel
# iteratador = iter(texto) #iterator

# while True:
#     try:
#         print(next(iteratador))
    
#     except StopIteration:
        # break
for letra in texto:
    print(letra)
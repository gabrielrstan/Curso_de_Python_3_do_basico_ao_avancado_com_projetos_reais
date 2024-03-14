"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
cpf = input('Informe o CPF: ')
cpf_corpo = cpf[:10]
cpf_validacao = cpf[10:]
# print(cpf_corpo)
# print(cpf_validacao)
# print(len(cpf))


if len(cpf) >= 11:
    try:
        cpf_corpo_int = int(cpf_corpo)
        cpf_validacao_int = int(cpf_validacao)
    except:
        print("Digite apenas numeros")
    
    soma = 0    
    cont = 11
    for i in range(len(cpf_corpo)):
        soma += int(cpf_corpo[i]) * cont
        cont -= 1
    mult = soma * 10
    resto = mult % 11
    val2 = 0 if resto > 9 else resto

else:
    print('Digite valores correspondentes aos numeros de um CPF')
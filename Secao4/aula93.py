# Try, except, else e finally
# (Parte 2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b
try:
    a = 18
    b = 0
    # print(b[0])
    # print('linha 1'[1000])
    c = a / b
    print('linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não esta definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError') 
    print('MSG: ', error) 
    print('Name: ', error.__class__.__name__) 
except Exception:
    print('Erro desconhecido')

print('Continuar')
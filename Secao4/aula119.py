# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

todo = []
descartado = []

while True:
    print('Comandos: listar, desfazer, refazer')
    entrada = input("Digite uma tarefa ou comando: ")
    if entrada.lower() == 'listar':
        print('TAREFAS:')
        for item in todo:
            print(item)
    elif entrada.lower() == 'desfazer':
        if len(todo) == 0 or None:
            print('Nada a desfazer')
        else:
            descartado.append(todo[-1])
            todo.pop(-1)
            print('TAREFAS:')
            for item in todo:
                print(item)
    elif entrada.lower() == 'refazer':
        if len(descartado) == 0 or None:
            print('Nada a refazer')
        else:
            todo.append(descartado[-1])
            descartado.pop(-1)
            print('TAREFAS:')
            for item in todo:
                print(item)
    else:
        todo.append(entrada)

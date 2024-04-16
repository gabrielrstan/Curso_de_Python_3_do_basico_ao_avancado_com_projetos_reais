# https://www.youtube.com/watch?v=2f_5LRQV3k0

# def execute_command(command):
#     if command == 'ls':
#         print('$ listing files')
#     elif command == 'cd':
#         print('$ changing directory')
#     else:
#         print('$ command not found')

#     print('... rest of the code')


# execute_command('ls')

# def execute_command(command: str):
#     match command:
#         case 'ls':
#             print('$ listing files')
#         case 'cd':
#             print('$ changing directory')
#         case _:
#             print('$ command not found')


# execute_command('rm')


# def execute_command(command):
#     match command.split():
#         case ['ls', path, *_]:
#             print('$ listing files from', path)
#         case ['cd', path]:
#             print('$ changing directory', path)
#         case _:
#             print('$ command not found')


# execute_command("ls /home")

# def execute_command(command):
#     match command.split():
#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing files from', directory)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not found')


# execute_command('ls /home/ /Users /etc')

# def execute_command(command):
#     match command.split():
#         case ['ls', *directories, '--force']:
#             for directory in directories:
#                 print('$ listing files FORCED', directory)
#         case ['ls', *directories]:
#             for directory in directories:
#                 print('$ listing files', directory)
#         case ['cd', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not found')


# execute_command('ls /home/ /Users /etc --force')
# execute_command('ls /home/ /Users /etc')


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories]:
#             for directory in directories:
#                 print('$ listing directory from', directory)
#         case ['cd' | 'change', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not found')


# execute_command('ls /home/ /users /etc')
# execute_command('list /home/ /users /etc')
# execute_command('cd /home/')
# execute_command('change /home/')

# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list', *directories] if len(directories) > 1:
#             for directory in directories:
#                 print('$ listing ALL directory from', directory)
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])
#         case ['cd' | 'change', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not found')


# execute_command('ls /home/ /users /etc')
# execute_command('ls /home')


# def execute_command(command):
#     match command.split():
#         case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:  # noqa:E501
#             for directory in directories:
#                 print('$ listing ALL directory from', directory)
#             print(f'{the_command=}, {the_list=}')
#         case ['ls' | 'list', *directories] if len(directories) <= 1:
#             print('$ listing ONE directory from', directories[0])
#         case ['cd' | 'change', path]:
#             print('$ changing directory to', path)
#         case _:
#             print('$ command not found')


# execute_command('ls /home/ /users /etc')
# execute_command('ls /home')


# def execute_command(command):
#     match command:
#         case {'command': 'ls', 'directories': [_, *_]}:
#             for directory in command['directories']:
#                 print('$ listing ALL directories from', directory)
#         case _:
#             print('$ command not found')


# execute_command({'command': 'ls', 'directories': ['/home', '/var/']})

from dataclasses import dataclass


@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command: Command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing directory to', directory)
        case _:
            print('$ command not found')


execute_command(Command(command='ls', directories=['/home', '/var/']))
execute_command(Command(command='cd', directories=['/user']))

from time import sleep
from threading import Thread


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá mundo 1', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 2))
# t3.start()

t4 = Thread(target=vai_demorar, args=('Olá mundo 4', 10))
t4.start()
t4.join()

# for i in range(20):
#     print(i)
#     sleep(.5)

# while t4.is_alive():
#     print('Esperando a thread.')
#     sleep(2)

print('Thread acabou')

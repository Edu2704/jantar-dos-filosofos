from Filosofo import Filosofo
from threading import Semaphore
from random import randint
from Interface import Interface

nomes = ["Friedrich Nietzsche", "Crisipo", "Thomas Hobbes", "Epicteto", "John Locke"]

garfos = [Semaphore(1) for i in range(5)]

filosofos = [Filosofo(nomes[i], garfos[i % 5], garfos [(i + 1) % 5])for i in range(5)]

inicio = randint(0, 4)

for i in range(5):
    filosofos[inicio%5].start()
    inicio += 1 


interface = Interface(filosofos)



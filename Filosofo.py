from threading import Thread
from time import sleep

class Filosofo(Thread):
    estado = 0 
    def __init__(self, nome, garfoEsq, garfoDir):
        Thread.__init__(self)
        self.nome = nome
        self.garfoEsq = garfoEsq
        self.garfoDir = garfoDir
    
    def run(self):
        print(f"{self.nome} está faminto")
        self.estado = 1
        sleep(2)
        self.comer()
    
    def pensar(self):
        print(f"{self.nome} está pensando")
        self.estado = 1
        sleep(2)
        print(f"{self.nome} está faminto")
        self.estado = 3
        self.comer()
 

    def comer(self):
        g1, g2 = self.garfoEsq, self.garfoDir

        try:
            g1.acquire()
            g2.acquire()
            print(f"{self.nome} está comendo")
            self.estado = 2
            sleep(2)
            print(f"{self.nome} terminou de comer")
            g1.release()
            g2.release()

            self.pensar()
        except:
            pass


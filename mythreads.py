from threading import Lock, Thread
from time import sleep

#Com classes --|
class MeuThread(Thread):
    def __init__(self, texto) :
        self.texto = texto
        super().__init__()
    
    def run(self):
        print(self.texto)

t1 = MeuThread('Thread test')
t1.start()


#Com funções --|
def vai_demorar(texto: str, tempo: int):
    sleep(tempo)
    print(texto)


class Ingressos:

    def __init__(self, estoque: int):
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):

        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    threads_compra = []
    for i in range(1,15):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads_compra.append(t)
        t.start()
    """
    Ao chamar o método t.join(), onde t é uma instância de uma thread,
    a thread principal irá pausar sua execução
    até que a thread t seja concluída. """
    
    for t in threads_compra:
        t.join()
    
    total_estoque = Thread(target=vai_demorar, args = (f"Estoque final: {ingressos.estoque}", 5))
    total_estoque.start()   

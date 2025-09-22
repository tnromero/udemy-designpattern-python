from abc import ABCMeta, abstractmethod

class Comando(metaclass=ABCMeta):

    def __init__(self, recv):
        self.recv = recv
    
    @abstractmethod
    def executar(self):
        pass

class ComandoConcreto(Comando):

    def __init__(self, recv):
        super().__init__(recv)
    
    def executar(self):
        self.recv.acao()

class Receiver:

    def acao(self):
        print('Acao do Receiver')
    
class Invoker:

    def comando(self, cmd: Comando):
        self.cmd = cmd
    
    def executar(self):
        self.cmd.executar()

if __name__ == '__main__':
    recv = Receiver()
    cmd = ComandoConcreto(recv)

    invoker = Invoker()
    invoker.comando(cmd)
    invoker.executar()
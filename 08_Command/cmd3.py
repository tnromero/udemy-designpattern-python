from abc import ABCMeta, abstractmethod

# Command
class Ordem(metaclass=ABCMeta):
    @abstractmethod
    def executar(self):
        pass

# Receiver
class MercadoAcao:

    def comprar(self):
        print('Voce comprara acoes...')
    
    def vender(self):
        print('Voce vendera acoes...')

# Comando Concreto
class OrdemCompra(Ordem):

    def __init__(self, mercado_acao: MercadoAcao):
        self.mercado_acao = mercado_acao
    
    def executar(self):
        self.mercado_acao.comprar()

# Comando Concreto
class OrdemVenda(Ordem):

    def __init__(self, mercado_acao: MercadoAcao):
        self.mercado_acao = mercado_acao
    
    def executar(self):
        self.mercado_acao.vender()


# Chamador/Invoker
class Agente:

    def __init__(self):
        self.__fila_ordens = []

    def adicionar_ordem_na_fila(self, ordem: Ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()

if __name__ == '__main__':
    # Cliente
    mercado_acao = MercadoAcao()
    ordem_compra = OrdemCompra(mercado_acao)
    ordem_venda = OrdemVenda(mercado_acao)

    # Chamador/Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)
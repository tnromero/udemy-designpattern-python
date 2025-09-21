from abc import ABCMeta, abstractmethod

class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass
    
    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def intinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()

class ViagemVeneza(Viagem):

    def ida(self):
        print('Viagem de avião...')
    
    def dia1(self):
        print('Visita à Basílica de são Marcos')

    def dia2(self):
        print('Visita ao Palácio Doge')
    
    def dia3(self):
        print('Aproveita a comida próximo à Ponte Rialto')

    def retorno(self):
        print('Viagem de avião...')

class ViagemMalvinas(Viagem):

    def ida(self):
        print('Viagem de ônibus...')
    
    def dia1(self):
        print('Aprecisar a vida marinha de Banana Reef')

    def dia2(self):
        print('Praticar esportes aquáticos')
    
    def dia3(self):
        print('Relaxar na praia e aproveitar o sol')

    def retorno(self):
        print('Viagem de avião...')

class GeekTravel:

    def preparar_viagem(self):

        opcao = input('Qual local de viagem deseja fazer: [Veneza, Malvinas]: ')

        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
        else:
            print('Opção inválida')
            return
        
        self.viagem.intinerario()

geek_travel = GeekTravel()
geek_travel.preparar_viagem()
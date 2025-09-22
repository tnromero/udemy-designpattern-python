from abc import ABCMeta, abstractmethod
from typing import List


# Interface Observer
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass


# Assunto / Tópico
class AgenciaNoticia:

    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None

    def inscrever(self, inscrito: TipoInscricao):
        self.__inscritos.append(inscrito)

    def desinscrever(self, inscrito: TipoInscricao = None) -> TipoInscricao:
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)

    def notificiar_todos(self):
        for inscrito in self.__inscritos:
            inscrito.notificar()

    def adicionar_noticia(self, noticia: str):
        self.__ultima_noticia = noticia

    def mostrar_noticia(self) -> str:
        return f"Urgente: {self.__ultima_noticia}"

    def inscritos(self) -> List[str]:
        return [type(valor).__name__ for valor in self.__inscritos]


# Observador A
class InscritosSMS(TipoInscricao):

    def __init__(self, agencia_noticia: AgenciaNoticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


# Observador A
class InscritosEmail(TipoInscricao):

    def __init__(self, agencia_noticia: AgenciaNoticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


# Observador N
class InscritosOutroMeio(TipoInscricao):

    def __init__(self, agencia_noticia: AgenciaNoticia):
        self.agencia_noticia = agencia_noticia
        self.agencia_noticia.inscrever(self)

    def notificar(self):
        print(f"{type(self).__name__} {self.agencia_noticia.mostrar_noticia()}")


# Cliente

if __name__ == "__main__":
    agencia_noticia = AgenciaNoticia()

    InscritosSMS(agencia_noticia)
    InscritosEmail(agencia_noticia)
    InscritosOutroMeio(agencia_noticia)

    print(f"Inscritos: {agencia_noticia.inscritos()}")

    agencia_noticia.adicionar_noticia("Novo curso na Geek University")
    agencia_noticia.notificiar_todos()

    print(f"Descadastrado: {type(agencia_noticia.desinscrever()).__name__}")
    print(f"Inscritos: {agencia_noticia.inscritos()}")

    agencia_noticia.adicionar_noticia("Design Patterns em Python!")
    agencia_noticia.notificiar_todos()

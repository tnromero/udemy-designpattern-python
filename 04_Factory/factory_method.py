from abc import ABCMeta, abstractmethod

class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass

class SessaoPessoal(Secao):

    def __repr__(self):
        return 'Seção Pessoal'

class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Seção Álbum'

class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Seção Projeto'

class SecaoPublicacao(Secao):

    def __repr__(self):
        return 'Seção Publicação'

#####

class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes
    
    def add_secao(self, secao):
        self.secoes.append(secao)

class Linkedin(Perfil):

    def criar_perfil(self):
        self.add_secao(SessaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao())

class Facebook(Perfil):

    def criar_perfil(self):
        self.add_secao(SessaoPessoal())
        self.add_secao(SecaoAlbum())

#####

if __name__ == '__main__':
    rede_social = input('Digite a rede social [Linkedin ou Facebook]: ')

    perfil = eval(rede_social)()
    print(f'Criando perfil em {type(perfil).__name__}')
    print(f'Seções do perfil: {perfil.get_secoes()}')
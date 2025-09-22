class Instalador:

    def __init__(self, fonte: str, destino: str):
        self.opcoes = []
        self.destino = destino
        self.fonte = fonte

    def preferencias(self, escolha):
        self.opcoes.append(escolha)
    
    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f'Copiando os binários de se {self.fonte} para {self.destino}')
            else:
                print('Operacao finalizada')

if __name__ == '__main__':
    # Iniciar o instalador
    instalador = Instalador('python3.9.1.gzip', '/usr/bin/')

    # O usuário escolhe isntalar apenas o Python
    instalador.preferencias({'python': True})
    instalador.preferencias({'java': False})

    # Execute
    instalador.executar()


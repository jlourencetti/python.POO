
from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    
    def get_ano_nascimento(self):
        print(f'{self.ano_atual - self.idade} ano de nascimento de {self.nome}')
        return 


pessoa_1 = Pessoa('Juliano', 38)
pessoa_2 = Pessoa('Roberta', 37)

pessoa_1.comer('Maçã')
pessoa_1.parar_comer()
pessoa_1.falar('Carro')
pessoa_1.get_ano_nascimento()
pessoa_2.get_ano_nascimento()

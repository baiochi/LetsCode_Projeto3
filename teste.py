#first file

from datatime import datetime.date as dtd
from datatime import datetime.time as dtt

class Cliente(object):
    def __init__(self, nome):
        self.cliente = nome

    def disponivel(self, nome):
       print(nome.estoque)

    def alugar(self, loja):
        try:
            quantidade = int(input('Quantidade de Bicicletas que deseja alugar: '))
            if quantidade > loja.estoque:
                raise ValueError
                
            familiar = input('É um aluguel familiar? ')
            data 
            
        except ValueError:
            print('msg erro')
            self.alugar(loja)
                        
    
    def devolver(self, horaDevolucao, quantidade, familiar):
        pass
    


class Loja(object):
    def __init__(self, nome, endereco, estoque):
        self.loja = nome
        self.endereco = endereco
        self.estoque = estoque

    



# COMPRA DE BICICLETAS

lojaMatriz = Loja('Bicicletas Paraiso', 'Rua Nascer do sol', 5)
cliente = Cliente('jose')
cliente.disponivel(lojaMatriz)

    
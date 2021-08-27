#first file

from datetime import datetime.date as dtd
from datetime import datetime.time as dtt

class Cliente(object):
    # Ver as bicicletas disponíveis na Loja;
    # Alugar bicicletas por hora (R$5/hora);
    # Alugar bicicletas por dia (R$25/dia);
    # Alugar bicicletas por semana (R$100/semana)
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.

    def __init__(self, nome):
        self.cliente = nome

    def disponivel(self, loja):
       print(loja.estoque)

    def alugar(self, loja):
        try:
            quantidade = int(input('Quantidade de Bicicletas que deseja alugar: '))
            if quantidade > loja.estoque:
                raise ValueError
                
            familiar = input('É um aluguel familiar? ')
            # data 
            
        except ValueError:
            print('msg erro')
            self.alugar(loja)
                        
    
    def devolver(self, horaDevolucao, quantidade, familiar):
        pass
    
class Loja(object):
    def __init__(self):
        self.estoque = 100
    
        # Calcular a conta quando o cliente decidir devolver a bicicleta;
        # Mostrar o estoque de bicicletas;
        # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    
        
# COMPRA DE BICICLETAS

lojaMatriz = Loja('Bicicletas Paraiso', 'Rua Nascer do sol', 5)
cliente = Cliente('jose')
cliente.disponivel(lojaMatriz)

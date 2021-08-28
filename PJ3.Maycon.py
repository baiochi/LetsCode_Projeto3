!pip install datetime
import time
from datetime import date


class Cliente(object):
    def __init__(self, nome):
        self.cliente = nome
    
    # Ver as bicicletas disponíveis na Loja;
    def disponivel(self, loja):
       print(f'Quantidade de bicicletas disponiveis: {loja.estoque}')

    # Alugar bicicletas:
    #   por hora (R$5/hora);
    #   por dia (R$25/dia);
    #   por semana (R$100/semana)
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.

    def alugar(self, loja):
        try:
            self.quantidadeAlugada = int(input('Informe a quantidade de bicicletas que deseja alugar: '))
            if self.quantidadeAlugada > loja.estoque:
                raise ValueError
            self.dataInicial = datetime.today()
            self.horaInicial = int(input('Informe a hora do aluguel: '))  
        except ValueError:
            print('Você deseja alugar {} bicicletas, mas a loja só tem {}'.format(self.quantidadeAlugada, loja.estoque))
            self.alugar(loja)               
    
    def devolver(self, loja):
        try:
            self.quantidadeDevolvida = int(input('Informe a quantidade de bicicletas que deseja devolver: '))
            if self.quantidadeDevolvida > self.quantidadeAlugada:
                raise ValueError
            self.dataFinal = datetime.today()
            self.horaFinal = int(input('Informe a hora da devolução: '))
        except ValueError:
            print('Você alugou: {} bicicletas, e deseja devolver {}. informe um valor valido'.format(self.quantidadeAlugada, self.quantidadeDevolvida)

    
class Loja(object):
    def __init__(self):
        self.estoque = 100
    
        # Calcular a conta quando o cliente decidir devolver a bicicleta;
        # Mostrar o estoque de bicicletas;
        # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    
        
# COMPRA DE BICICLETAS

Matriz = Loja()
cliente = Cliente('jose')
cliente.disponivel(lojaMatriz)

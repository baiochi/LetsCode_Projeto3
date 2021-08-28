from datetime import date
from datetime import time

"""
Métodos do Cliente:
- Ver as bicicletas disponíveis na Loja;
- Alugar bicicletas por hora (R$5/hora);
- Alugar bicicletas por dia (R$25/dia);
- Alugar bicicletas por semana (R$100/semana)
- Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) 
com 30% de desconto no valor total.
"""

class Cliente(object):

    def __init__(self) -> None:
        self.modeloAluguel = ''

    # 1 - Ver as bicicletas disponíveis na Loja;
    def verBiciletas(self, loja):
        return loja.estoque

    #- Alugar bicicletas por hora (R$5/hora), dia (R$25/dia), semana (R$100/semana)
    def alugarBicicleta(self, loja, quantidade, modeloAluguel):
        try:
            if quantidade > loja.estoque:
                raise ValueError('Estoque insuficiente.')
            if modeloAluguel in ['dia', 'hora', 'semana']:
                self.modeloAluguel = modeloAluguel
                print(f'Aluguel por R${loja.tabelaPrecos[modeloAluguel]}/{modeloAluguel}')
            else:
                raise Exception('Modelo de alguel inválido.')
        except ValueError:
            print('Modelo de alguel inválido')


    # 5 - Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos (de qualquer tipo) 
    # com 30% de desconto no valor total.


"""
Loja pode:
- Calcular a conta quando o cliente decidir devolver a bicicleta;
- Mostrar o estoque de bicicletas;
- Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
"""

class Loja(object):

    def __init__(self, estoque):
        self.estoque = estoque
        self.tabelaPrecos ={
            'hora' : 5,
            'dia' : 25,
            'semana' : 100
        }
    
    # - Mostrar o estoque de bicicletas;
    def mostrarEstoque(self):
        return self.estoque

    # - Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta(self, cliente):

        pass

    #- Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    def receberPedido():
        pass

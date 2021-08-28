from datetime import datetime as dt
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
        self.qtdeBicicletas = 0
        self.promocaoFamilia = False
        self.dataAluguel = dt.today()

    # Ver as bicicletas disponíveis na Loja;
    def verBiciletas(self, loja):
        return loja.estoque

    # Alugar bicicletas por hora (R$5/hora), dia (R$25/dia), semana (R$100/semana)
    # Opcional: promoção que pode incluir de 3 a 5 aluguéis com 30% de desconto no valor total.
    def alugarBicicleta(self, loja, quantidade, modeloAluguel, promocaoFamilia = False):
        try:
            # Verificar o estoque
            if quantidade > loja.estoque:
                raise ValueError('Estoque insuficiente.')
            # Validar o modelo do aluguel
            if modeloAluguel not in ['dia', 'hora', 'semana']:
                raise Exception('Modelo de alguel inválido.')
            # Validar da promoção
            if promocaoFamilia and not 3 <= quantidade <= 5:
                self.promocaoFamilia = False # reseta a varíável para evitar bug em chamadas futuras
                raise Exception('Quantidade inválida para validar a promoção.')

            loja.aumentarEstoque(quantidade)
            self.qtdeBicicletas = quantidade # atualiza quantidade de bicicletas que o cliente alugou
            self.modeloAluguel = modeloAluguel # define o modelo do empréstimo
            self.dataAluguel = dt.today() # registra a data/horário do aluguel
            print(f'{quantidade} bicileta(s) alugada(s) por R${loja.tabelaPrecos[modeloAluguel]}/{modeloAluguel}\
                 as {self.dataAluguel.strftime("%H:%M:%S")} no dia {self.dataAluguel.strftime("%d/%m/%y")}') #log

        except ValueError:
            print('Estoque insuficiente.')
        except Exception:
            print('Dado inválido.')

"""
Loja pode:
- Calcular a conta quando o cliente decidir devolver a bicicleta;
- Mostrar o estoque de bicicletas;
- Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
"""

class Loja(object):

    def __init__(self, estoque):
        self.estoque = estoque
        self.tabelaPrecos = {
            'hora' : 5,
            'dia' : 25,
            'semana' : 100
        }
    
    # Mostrar o estoque de bicicletas;
    def mostrarEstoque(self):
        return self.estoque

    # Adiciona mais bicicletas ao estoque
    def aumentarEstoque(self, estoque):
        self.estoque += estoque

    # Remove bicicletas do estoque
    def diminuirEstoque(self, estoque):
        self.estoque -= estoque

    # - Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta(self, cliente):
        if cliente.modeloAluguel == 'hora':
            # Calcular a hora
            tempoAluguel = cliente.dataAluguel


        if cliente.modeloAluguel == 'dia':
            pass
        if cliente.modeloAluguel == 'semana':
            pass
        pass

    #- Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    def receberPedido():
        pass


loja01 = Loja()

loja01.tabelaPrecos
loja01.alterarEstoque(100)



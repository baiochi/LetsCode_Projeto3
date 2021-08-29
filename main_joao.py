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

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    # Retorna o nome do cliente
    def getNome(self):
        return self.nome
    # Retorna o CPF do cliente
    def getCPF(self):
        return self.cpf

    # Como o cliente ficou praticamente sem atributos, podemos adicionar outras variáveis,
    # por exemplo, CPF (atuando como ID), telefone, endereco etc...

"""
Loja pode:
- Calcular a conta quando o cliente decidir devolver a bicicleta;
- Mostrar o estoque de bicicletas;
- Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
"""

class Loja(object):

    def __init__(self, estoque):
        self.estoque = estoque
        # dados da tabela de preco são usados para calcular o custo do aluguel e definir modelo do aluguel
        self.tabelaPrecos = {
            'hora' : 5,
            'dia' : 25,
            'semana' : 100
        } 
        # recebe dicionario: cliente, quantidade, modeloAluguel, dataAluguel, promocaoFamilia
        self.historicoAluguel = []

    
    # Mostrar o estoque de bicicletas;
    def mostrarEstoque(self):
        return self.estoque

    # aumentarEstoque() e diminuirEstoque() removidos, pois ficaram sem uso

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta(self, cliente):
        # extrair o dicionário referente ao aluguel do cliente:
        # versao "normal":
        for item in self.historicoAluguel:
            if item['client'].getName() == cliente.getName():
                aluguel = item
        print(aluguel['client'].getName())
        # versao list comprehension
        #aluguelLc = [aluguel for aluguel in self.historicoAluguel if aluguel['client'].getName() == cliente.getName()]
        #print(aluguelLc[0]['client'].getName())

        if aluguel['modeloAluguel'] == 'hora':
            dataAtual = dt.now()
            # calcula os minutos
            minutos = dataAtual.minute - aluguel['dataAluguel'].minute
            if minutos < 0: minutos += 60 # evita deixar os minutos em negativos
            # calcula as horas
            horas = dataAtual.hour - aluguel['dataAluguel'].hour
            # soma final, computando os minutos excedentes
            tempoAluguel = (horas + (minutos/60)).__round__()
            # calcula o valor
            valorAluguel = tempoAluguel * 5
            # log
            print(f'hora da devolucao: {dataAtual.strftime("%H:%M:%S")}, \
                hora do aluguel: {aluguel["dataAluguel"].strftime("%H:%M:%S")}')
            return valorAluguel

        if aluguel['modeloAluguel'] == 'dia':
            dataAtual = dt.now()
            tempoAluguel = dataAtual.day - aluguel['dataAluguel'].day
            valorAluguel = tempoAluguel * 25
            print(f'Data da devolucao: {dataAtual.strftime("%d/%m/%y")}, \
                data do aluguel: {aluguel["dataAluguel"].strftime("%d/%m/%y")}') #log
            return valorAluguel

        if aluguel['modeloAluguel'] == 'semana':
            dataAtual = dt.now()
            tempoAluguel = (dataAtual.day - aluguel['dataAluguel'].day)/7
            tempoAluguel = tempoAluguel // 1 # arredonda o número
            valorAluguel = tempoAluguel * 100
            print(f'Data da devolucao: {dataAtual.strftime("%d/%m/%y")}, \
                data do aluguel: {aluguel["dataAluguel"].strftime("%d/%m/%y")}') #log
            return valorAluguel
        pass

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    def receberPedido(self, cliente, quantidade, modeloAluguel, promocaoFamilia = False):
        try:
            # Verificar o estoque
            if quantidade > self.estoque:
                raise ValueError('Estoque insuficiente.')
            # Validar o modelo do aluguel (tabelaPrecos.keys() = ['hora', 'dia', 'semana'])
            if modeloAluguel not in self.tabelaPrecos.keys():
                raise ValueError('Modelo de alguel inválido.')
            # Validar da promoção
            if promocaoFamilia and not 3 <= quantidade <= 5:
                self.promocaoFamilia = False # reseta a varíável para evitar bug em chamadas futuras
                raise Exception('Quantidade inválida para validar a promoção.')
            
            # monta o dicionario referente ao aluguel
            aluguel = {
                'cliente': cliente,
                'quantidade': quantidade,
                'modeloAluguel': modeloAluguel,
                'dataAluguel': dt.today(),
                'promocaoFamilia': promocaoFamilia
            }

            # diminue o estoque
            self.estoque -= quantidade
            # amazena os dados do aluguel
            self.historicoAluguel.append(aluguel) 
            # log
            print(f'{quantidade} bicileta(s) alugada(s) por R${self.tabelaPrecos[modeloAluguel]}/{modeloAluguel}\
                 as {self.dataAluguel.strftime("%H:%M:%S")} no dia {self.dataAluguel.strftime("%d/%m/%y")}')

        except ValueError:
            print('Estoque insuficiente.')
        except Exception:
            print('Dado inválido.')


loja01 = Loja()

loja01.tabelaPrecos
loja01.alterarEstoque(100)



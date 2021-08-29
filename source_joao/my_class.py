from datetime import datetime as dt
from datetime import time
import math

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
    
    # método mágico que representa a classe
    def __repr__(self):
        # verifica a existencia dos atributos da classe
        if(hasattr(self, 'nome') and hasattr(self, 'cpf')):
            return f'Dados do Cliente\nNome: {self.nome}; CPF: {self.cpf}'
        else:
            return 'Dados inválido dos cliente.'

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
        # recebe dicionario: cliente, quantidade, modeloAluguel, dataAluguel, promocaoFamilia
        self.historicoAluguel = []
        # armazena clientes cadastrados
        self.cadastroClientes = []
        # dados da tabela de preco são usados para calcular o custo do aluguel e definir modelo do aluguel
        self.tabelaPrecos = {
            'hora' : 5,
            'dia' : 25,
            'semana' : 100
        } 
        
    # método mágico que representa a classe
    def __repr__(self):
        # verifica a existencia dos atributos da classe
        if(hasattr(self, 'estoque') and hasattr(self, 'tabelaPrecos') and hasattr(self, 'historicoAluguel')):
            return f'Dados da loja\nEstoque: {self.estoque}\nTabela de Preços: {self.tabelaPrecos}\n'
            # Histórico dos Aluguéis: {self.historicoAluguel}   <- melhorar a formatacao do dicionario
                
        else:
            return 'Dados inválidos da Loja.'

    # cadastrar cliente
    def cadastraCliente(self, cliente):
        # verificar se cliente já existe
        #for item in self.cadastroClientes:
        #    if cliente.getCPF() == item.getCPF():
        #        print(item)
        if [item for item in self.cadastroClientes if cliente.getCPF() == item.getCPF()]:
            raise ValueError('Cliente já cadastrado.')

        self.cadastroClientes.append(cliente)

    # Mostrar o estoque de bicicletas;
    def mostrarEstoque(self):
        return self.estoque
    
    # Finaliza o aluguel, atualizando o estoque e retornando o valor da conta
    def devolverBicicletas(self, cliente):
        # extrair o dicionário referente ao aluguel do cliente:
        # versao "normal":
        for item in self.historicoAluguel:
            if item['cliente'].getNome() == cliente.getNome():
                aluguel = item
        #print(aluguel['client'].getNome())
        
        # versao list comprehension
        #aluguel = [aluguel for aluguel in self.historicoAluguel if aluguel['client'].getNome() == cliente.getNome()]
        #print(aluguel[0]['client'].getNome())

        # atualiza o estoque
        self.estoque += aluguel['quantidade']
        # faz a chama do método e retorna o valor do aluguel
        return self.calcularConta(aluguel)

    # Faz o cálculo de acordo com a modalidade e tempo do aluguel
    def calcularConta(self, aluguel):
        # extrai a data atual
        dataAtual = dt.now()

        # Calculo para a modalidade R$5/hora
        if aluguel['modeloAluguel'] == 'hora':
            # calcula os minutos
            minutos = dataAtual.minute - aluguel['dataAluguel'].minute
            if minutos < 0: minutos += 60 # evita deixar os minutos em negativos
            # calcula as horas
            horas = dataAtual.hour - aluguel['dataAluguel'].hour
            # soma final, computando os minutos excedentes
            tempoAluguel = (horas + (minutos/60)).__round__()
            # calcula o valor
            valorAluguel = tempoAluguel * aluguel['quantidade'] * self.tabelaPrecos['hora'] # 5
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # log
            print(f'[log] Cliente: {aluguel["cliente"].getNome()}, Hora da devolucao: {dataAtual.strftime("%H:%M:%S")},',
                f'Hora do aluguel: {aluguel["dataAluguel"].strftime("%H:%M:%S")}')
            return valorAluguel

        # Calculo para a modalidade R$25/dia
        elif aluguel['modeloAluguel'] == 'dia':
            # calculo do dia
            tempoAluguel = dataAtual.day - aluguel['dataAluguel'].day
            ### falta validar o resultado de dia negativo, e.g. 29/08 - 30/07
            valorAluguel = tempoAluguel * aluguel['quantidade'] * self.tabelaPrecos['dia'] # 25
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # log
            print(f'[log] Cliente: {aluguel["cliente"].getNome()}, Data da devolucao: {dataAtual.strftime("%d/%m/%y")},',
                f' Data do aluguel: {aluguel["dataAluguel"].strftime("%d/%m/%y")}') #log
            return valorAluguel

        # Calculo para a modalidade R$100/hora
        elif aluguel['modeloAluguel'] == 'semana':
            # calculo da semana com base em 7 dias corridos
            tempoAluguel = (dataAtual.day - aluguel['dataAluguel'].day) / 7
            # arredonda o número para cima
            tempoAluguel = math.ceil(tempoAluguel) 
            valorAluguel = tempoAluguel * aluguel['quantidade'] * self.tabelaPrecos['semana'] # 100
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # log
            print(f'[log] Cliente: {aluguel["cliente"].getNome()}, Data da devolucao: {dataAtual.strftime("%d/%m/%y")},',
                f'Data do aluguel: {aluguel["dataAluguel"].strftime("%d/%m/%y")}') #log
            return valorAluguel

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    # Dois últimos parâmetros reservados para teste
    def receberPedido(self, cliente, quantidade, modeloAluguel,\
        promocaoFamilia = False, debug = False, dataTeste = dt.today()):
        #try:
        # Verificar o estoque
        if quantidade > self.estoque:
            raise ValueError('Estoque insuficiente.')
        # Validar o modelo do aluguel (tabelaPrecos.keys() = ['hora', 'dia', 'semana'])
        if modeloAluguel not in self.tabelaPrecos.keys():
            raise NameError('Modelo de alguel inválido.')
        # Validar da promoção
        if promocaoFamilia and not 3 <= quantidade <= 5:
            self.promocaoFamilia = False # reseta a varíável para evitar bug em chamadas futuras
            raise TypeError('Quantidade inválida para validar a promoção.')
        
        # monta o dicionario referente ao aluguel
        if debug:
            aluguel = {
                'cliente': cliente,
                'quantidade': quantidade,
                'modeloAluguel': modeloAluguel,
                'dataAluguel': dataTeste,
                'promocaoFamilia': promocaoFamilia
            }
        else:
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
        print(f'[log] {quantidade} bicileta(s) alugada(s) por R${self.tabelaPrecos[modeloAluguel]}/{modeloAluguel}',
                f'as {aluguel["dataAluguel"].strftime("%H:%M:%S")}',
                f'no dia {aluguel["dataAluguel"].strftime("%d/%m/%y")}')

        """except ValueError:
            print('Estoque insuficiente!\n')
        except NameError:
            print('Modelo de alguel inválido!\n')
        except TypeError:
            print('Promoção não aplicável!\n')"""



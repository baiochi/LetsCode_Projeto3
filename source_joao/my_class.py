from datetime import datetime as dt
from datetime import time
import datetime
import math

# cores para visualizar melhor os logs
COLORS = {
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
}
def colorText(text):
    for color in COLORS: text = text.replace("[[" + color + "]]", COLORS[color])
    return text

# transforma objeto datetime.datime em timedelta e calcula os valores de semana, dia, hora, minutos, segundos
# retorna em um diconario
def formatarData(dataAluguel, dataRetorno):
    dataAluguelDelta = datetime.timedelta(
        days=dataAluguel.day,
        hours=dataAluguel.hour,
        minutes=dataAluguel.minute,
        seconds=dataAluguel.second
    )

    dataRetornoDelta = datetime.timedelta(
        days=dataRetorno.day,
        hours=dataRetorno.hour,
        minutes=dataRetorno.minute,
        seconds=dataRetorno.second
    )

    tempoDelta = dataRetornoDelta - dataAluguelDelta

    totalSeconds = tempoDelta.total_seconds()

    segundos = totalSeconds % 60                     # verifica se sobrou segundos
    resto = segundos                                 # armazena os segundos que sobraram
    minutos = ((totalSeconds - resto) / 60) % 60     # remove os segundos, e calcula se sobrou minutos
    resto += minutos*60                              # armazena os minutos que sobraram
    horas = ((totalSeconds - resto) / 3600) % 24     # remove os minutos, e calcula se sobrou horas
    resto += horas*3600                              # armazena as horas que sobraram
    dias = ((totalSeconds - resto) / 86400) % 7     # remove as horas, e calcula se sobrou dias
    resto += dias*86400                              # armazena os dias que sobraram
    semanas = ((totalSeconds - resto) / 604800)

    return {
        'semanas' : semanas, 
        'dias' : dias, 
        'horas' : horas, 
        'minutos' : minutos, 
        'segundos' : segundos
    }

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
        """
        Estrutura do dicionário aluguel = {
            'cliente' : Cliente(),
            'quantidade' : int,
            'modeloAluguel': str,       ['hora','dia','semana']
            'dataAluguel': datetime
            }
        """
        self.historicoAluguel = []
        # armazena clientes cadastrados, lista vai receber objetos Cliente()
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
            raise ValueError(f'Cliente {cliente.getNome()} já cadastrado.')
        # registra o cliente na lista cadastroClientes
        self.cadastroClientes.append(cliente)
        #log
        print(colorText(f'[[yellow]][log cadastraCliente][[white]]\nCliente {cliente.getNome()} cadastrado com sucesso.'))

    # Mostrar o estoque de bicicletas;
    def mostrarEstoque(self):
        return self.estoque

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    # Dois últimos parâmetros reservados para teste
    def receberPedido(self, cliente, quantidade, modeloAluguel,\
        promocaoFamilia = False, dataAluguel = dt.now()):
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
        aluguel = {
                'cliente': cliente,
                'quantidade': quantidade,
                'modeloAluguel': modeloAluguel,
                'dataAluguel': dataAluguel,
                'promocaoFamilia': promocaoFamilia
            }

        # diminue o estoque
        self.estoque -= quantidade
        # amazena os dados do aluguel
        self.historicoAluguel.append(aluguel) 
        # log
        print(colorText(f'[[yellow]][log receberPedido][[white]]\n {quantidade} bicileta(s) alugada(s) por R${self.tabelaPrecos[modeloAluguel]}/{modeloAluguel}'),
                f'as {aluguel["dataAluguel"].strftime("%H:%M:%S")}',
                f'no dia {aluguel["dataAluguel"].strftime("%d/%m/%y")}',
                f'\nEstoque atual: {self.mostrarEstoque()}', sep='')
        
        """except NameError:
            print('Modelo de alguel inválido!\n')
        except TypeError:
            print('Promoção não aplicável!\n')
        except ValueError:
            print('Estoque insuficiente!')"""

    # Finaliza o aluguel, atualizando o estoque e retornando o valor da conta
    def devolverBicicletas(self, cliente):
        # extrair o dicionário referente ao aluguel do cliente:
        for dicionario in self.historicoAluguel:
            if dicionario['cliente'].getNome() == cliente.getNome():
                aluguel = dicionario

        # atualiza o estoque
        self.estoque += aluguel['quantidade']
        print(colorText(f'[[yellow]][log devolverBicicletas][[white]]\nQuantidade de bicicletas retornadas ao estoque:{aluguel["quantidade"]}'),
              f'\nEstoque atual: {self.mostrarEstoque()}', sep='')
        # faz a chama do método e retorna o valor do aluguel
        return self.calcularConta(aluguel)

    # Faz o cálculo de acordo com a modalidade e tempo do aluguel
    def calcularConta(self, aluguel, dataRetorno = dt.now()):

        # retorna os dados com a data calculada
        dataCalculada = formatarData(dataAluguel = aluguel['dataAluguel'] , dataRetorno = dataRetorno)

        # Calculo para a modalidade R$5/hora
        if aluguel['modeloAluguel'] == 'hora':
            
            # calcula o valor
            valorAluguel = dataCalculada['horas'] * aluguel['quantidade'] * self.tabelaPrecos['hora'] # 5
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # tratamento de tolerancia/multa, adiciona o valor de 1 hora, nao aplicando a promocao
            if dataCalculada['minutos'] > 15:
                valorAluguel += 5

        # Calculo para a modalidade R$25/dia
        elif aluguel['modeloAluguel'] == 'dia':

            # calculo do dia
            valorAluguel = dataCalculada['dias'] * aluguel['quantidade'] * self.tabelaPrecos['dia'] # 25
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # tratamento de tolerancia/multa, passada 3 horas, adiciona multa a cada hora, nao aplicando a promocao
            if dataCalculada['horas'] > 3:
                valorAluguel += dataCalculada['horas'] * self.tabelaPrecos['hora']

        # Calculo para a modalidade R$100/hora
        elif aluguel['modeloAluguel'] == 'semana':
            # calculo da semana
            valorAluguel = dataCalculada['semanas'] * aluguel['quantidade'] * self.tabelaPrecos['semana'] # 100
            # validação da promoção (desconto 30%)
            if aluguel['promocaoFamilia']: valorAluguel *= 0.7
            # aplica multa por dia excedente, sendo R$25/dia, nao se aplica na promocao
            if dataCalculada['dias'] > 0:
                valorAluguel += dataCalculada['dias'] * self.tabelaPrecos['dia']
        
        # log
        print(
        colorText(f'[[yellow]][log calcularConta][[white]]\nCliente: {aluguel["cliente"].getNome()};\nHora da devolucao: {dataRetorno.strftime("%H:%M:%S")};\n'),
        f'Hora do aluguel: {aluguel["dataAluguel"].strftime("%H:%M:%S")};\n',
        f'Valor do aluguel: R$ {valorAluguel}', sep='')
        return valorAluguel




#print(aluguel['client'].getNome())

#conferir cliente: versao list comprehension 
#aluguel = [aluguel for aluguel in self.historicoAluguel if aluguel['client'].getNome() == cliente.getNome()]
#print(aluguel[0]['client'].getNome())

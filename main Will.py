from datetime import date as dtd
from datetime import time as dtt

class Loja (object):
    
    def __init__ (self, estoque):
        self.estoque = estoque
    
    # Mostrar o estoque de bicicletas para o Cliente;
    def mostrarEstoque (self):
        return self.estoque

    # Alterar a quantidade do estoque.
    def alterarEstoque (self, baixa):
        self.estoque -= baixa

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a disponibilidade do estoque.
    def receberPedido (self, pedido):
        self.estoqueAtual = loja.mostrarEstoque()
        self.pedido = pedido

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta (self, opcaoDesejada, pedido):
        self.opcaoDesejada = opcaoDesejada
        self.pedido = pedido

class Cliente (object):
    
    def __init__ (self, carteira):
        self.carteira = carteira

    # Alugar bicicletas por hora (R$5/hora);
    def alugarHora (self, periodo):
        self.periodo = periodo
    
    # Alugar bicicletas por dia (R$25/dia);
    def alugarDia (self, periodo):
        self.periodo = periodo

    # Alugar bicicletas por semana (R$100/semana)
    def alugarSemana (self, periodo):
        self.periodo = periodo
    
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.
    def alugarFamilia (self, quantidade, tipoAluguel, periodo):
        self.quantidade = quantidade
        self.tipoAluguel = tipoAluguel
        self.periodo = periodo

# Função para validar a entrada de dados do input do cliente:
# Argumentos: entrada
# Retorna: entrada
def validaEntrada(entrada):
    _opcoes = ('0', '1', '2', '3', '4', 'E')
    while entrada not in _opcoes:
        entrada = input('\nOpção inválida! Qual o plano que você deseja contratar? ').upper()
    return entrada

# Função do menu do cliente:
# Argumentos: entrada
# Retorna: 
def menuEntradas(entrada):
    if entrada == 'E':
        print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.')
        entrada = validaEntrada(input('\nQual o plano que você deseja contratar? ').upper())
        menuEntradas(entrada)
        return entrada

    elif entrada == '0': # Está printando "None".
        print('\nÉ uma pena... Mas aguardamos você numa próxima!')
        
    # Plano Hora
    elif entrada == '1':
        print('\nO plano \"Dar uma voltinha\" foi selecionado!')
        qtdHoras = input('Por quantas horas você deseja alugar? ')
        cliente.alugarHora(qtdHoras)
        return entrada

    # Plano Dia
    elif entrada == '2':
        print('\nO plano Diário foi selecionado!')
        qtdDias = input('Por quantos dias você deseja alugar? ')
        cliente.alugarDia(qtdDias)
        return entrada

    # Plano Semana
    elif entrada == '3':
        print('\nO plano Semanal foi selecionado!')
        qtdSemanas = input('Por quantas semanas você deseja alugar? ')
        cliente.alugarSemana(qtdSemanas)
        return entrada

    # Plano Família
    else: # opcao == '4'
        print('\nO plano Família foi selecionado!')
        qtdBicicletas = input('Quantas bicicletas você deseja alugar? ')
        while qtdBicicletas not in ('3','4','5'):
            qtdBicicletas = input('Digite um valor entre 3 e 5! Quantas bicicletas você deseja alugar? ')
        plano = input(f'Em qual dos planos você deseja alugar {qtdBicicletas} bicicletas? ')
        while plano not in ('1','2','3'):
            print('Valor Inválido! Digite 1, 2 ou 3 correspondente ao plano desejado.')
            plano = input(f'Em qual dos planos você deseja alugar {qtdBicicletas} bicicletas? ')
        preenche = ""
        if plano == '1':
            preenche = 'quantas horas'
        elif plano == '2':
            preenche = 'quantos dias'
        else:
            preenche = 'quantas semanas'
        tempo = input(f'Por {preenche} você deseja alugar {qtdBicicletas} bicicletas? ')
        cliente.alugarFamilia(qtdBicicletas, plano, tempo)
        return entrada, qtdBicicletas, plano, tempo


# Init classes
cliente = Cliente(1000)
loja = Loja(100)

print('Bem vindo à Locadora de Bicicletas LTDA!')
print('Aqui temos uma variedade de planos para o aluguel de bicicletas, que são:')
print('1 - Plano \"Dar uma voltinha\" - R$ 5,00 por hora;')
print('2 - Plano Diário - R$ 25,00 por dia;')
print('3 - Plano Semanal - R$ 100,00 por semana e;')
print('4 - Plano Família, que consiste em alugar de 3 a 5 bicicletas nos planos')
print('    anteriores e que dá 30% de desconto no valor total do pedido!\n')

print('Digite o valor de 1 a 4 conforme o plano desejado,')
print('digite \"E\" para visualizar a quantidade de biciletas em estoque')
print('ou digite 0 para cancelar.')

opcao = validaEntrada(input('\nQual o plano que você deseja contratar? ').upper())
pedidoCliente = (menuEntradas(opcao))

# Log
print(f'A opção do cliente foi: {pedidoCliente}')

print('\nFim do programa.')

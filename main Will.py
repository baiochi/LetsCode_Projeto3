from datetime import date as dtd
from datetime import time as dtt

class Loja (object):
    
    def __init__ (self, estoque):
        self.estoque = estoque
    
    # Mostrar o estoque de bicicletas para o Cliente;
    def mostrarEstoque (self):
        return self.estoque

    # Alterar a quantidade do estoque.
    def alterarEstoque (self, estoque):
        self.estoque = estoque

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a disponibilidade do estoque.
    def receberPedido (self, estoqueAtual, pedido):
        self.estoqueAtual = estoqueAtual
        self.pedido = pedido

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta (self, opcaoDesejada, pedido):
        self.opcaoDesejada = opcaoDesejada
        self.pedido = pedido

class Cliente (object): # alterado parametro Loja para object, não é necessário ela ser herdada
    
    def __init__ (self):
        self.carteira = 1000

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
    def alugarFamilia (self, quantidade, *opcaoDesejada):
        pass

# Inicializacao das class

cliente = Cliente()
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

opcao = input('\nQual o plano que você deseja contratar? ').upper()
# Tupla para selecionar as opções de alguel que o cliente vai ter.
_opcoes = ('0', '1', '2', '3', '4', 'E')

while opcao not in _opcoes:
    opcao = input('\nOpção inválida! Qual o plano que você deseja contratar? ').upper()

if opcao == 'E':
    print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.')
    opcao = input('\nQual o plano que você deseja contratar? ').upper()

# alterei os números para string pois no input ele não estava lendo int
#
elif opcao == '0':
    print('\nÉ uma pena... Mas aguardamos você numa próxima!')

# Plano Hora
elif opcao == '1':
    print('\nO plano \"Dar uma voltinha\" foi selecionado!')
    qtdHoras = input('Por quantas horas você deseja alugar? ')
    cliente.alugarHora(qtdHoras)

# Plano Dia
elif opcao == '2':
    print('\nO plano Diário foi selecionado!')
    qtdDias = input('Por quantos dias você deseja alugar? ')
    cliente.alugarDia(qtdDias)

# Plano Semana
elif opcao == '3':
    print('\nO plano Semanal foi selecionado!')
    qtdSemanas = input('Por quantas semanas você deseja alugar? ')
    cliente.alugarSemana(qtdSemanas)

elif opcao == '4': #acho que se mantesse o else, qualquer outra coisa digitada entraria aqui
    print('\nO plano Família foi selecionado!')

else:
    print('\nOpção inválida!')

print('\nFim do programa.')
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
    def receberPedido (self, periodo, *quantPlano):
        pass

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta (self):
        pass

class Cliente (object):
    
    def __init__ (self, carteira):
        self.carteira = carteira

    # Ver as bicicletas disponíveis na Loja;
    def checarEstoque (self):
        print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.')
        self.opcao = validaEntrada(input('\nQual o plano que você deseja contratar? ').upper())
        menuEntradas(self.opcao)
        return self.opcao
    
    # Alugar bicicletas por hora (R$5/hora);
    def alugarHora (self):
        self.periodo = input('Por quantas horas você deseja alugar? ')
        print(f'Selecionado {self.periodo} hora(s)!')
        return self.periodo
    
    # Alugar bicicletas por dia (R$25/dia);
    def alugarDia (self):
        self.periodo = input('Por quantos dias você deseja alugar? ')
        print(f'Selecionado {self.periodo} dia(s)!')
        return self.periodo

    # Alugar bicicletas por semana (R$100/semana)
    def alugarSemana (self):
        self.periodo = input('Por quantas semanas você deseja alugar? ')
        print(f'Selecionado {self.periodo} semana(s)!')
        return self.periodo
    
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.
    def alugarFamilia (self):
        self.qtdBicicletas = input('Quantas bicicletas você deseja alugar? ')
        while self.qtdBicicletas not in ('3','4','5'):
            self.qtdBicicletas = input('Digite um valor entre 3 e 5! Quantas bicicletas você deseja alugar? ')
        
        self.plano = input(f'Em qual dos planos você deseja alugar {self.qtdBicicletas} bicicletas? ')
        while self.plano not in ('1','2','3'):
            print('Valor Inválido! Digite 1, 2 ou 3 correspondente ao plano desejado.')
            self.plano = input(f'Em qual dos planos você deseja alugar {self.qtdBicicletas} bicicletas? ')
        
        preenche = ""
        if self.plano == '1':
            preenche = 'quantas horas'
        elif self.plano == '2':
            preenche = 'quantos dias'
        else:
            preenche = 'quantas semanas'
        self.periodo = input(f'Por {preenche} você deseja alugar {self.qtdBicicletas} bicicletas? ')
        
        preenche2 = ""
        if self.plano == '1':
            preenche2 = 'hora(s)'
        elif self.plano == '2':
            preenche2 = 'dia(s)'
        else:
            preenche2 = 'semana(s)'
        print(f'Selecionado alugar {self.qtdBicicletas} bicicletas no Plano {self.plano} por {self.periodo} {preenche2}!')
        return self.periodo, self.qtdBicicletas, self.plano

'''
Função para validar a entrada de dados do input do cliente:
Argumentos: entrada
Retorna: entrada
'''
def validaEntrada(entrada):
    _opcoes = ('0', '1', '2', '3', '4', 'E')
    while entrada not in _opcoes:
        entrada = input('\nOpção inválida! Qual o plano que você deseja contratar? ').upper()
    return entrada

'''
Função do menu: chama os devidos métodos de cada Classe de acordo com as escolhas do cliente.
Argumentos: entrada
Retorna: None.
'''
def menuEntradas(entrada):
    if entrada == 'E':
        print('\nConferir o estoque disponível foi selecionado!')
        cliente.checarEstoque()

    elif entrada == '0':
        print('\nÉ uma pena... Mas aguardamos você numa próxima!')
        
    # Plano Hora
    elif entrada == '1':
        print('\nO plano Passeio foi selecionado!')
        cliente.alugarHora()
        
    # Plano Dia
    elif entrada == '2':
        print('\nO plano Diário foi selecionado!')
        cliente.alugarDia()
        
    # Plano Semana
    elif entrada == '3':
        print('\nO plano Semanal foi selecionado!')
        cliente.alugarSemana()
        
    # Plano Família
    else: # opcao == '4'
        print('\nO plano Família foi selecionado!')
        cliente.alugarFamilia()


# Init classes
cliente = Cliente(1000)
loja = Loja(100)

print('Bem vindo à Locadora de Bicicletas LTDA!')
print('Aqui temos uma variedade de planos para o aluguel de bicicletas, que são:\n')

print('1 - Plano Passeio - R$ 5,00 por hora;')
print('2 - Plano Diário - R$ 25,00 por dia;')
print('3 - Plano Semanal - R$ 100,00 por semana e;')
print('4 - Plano Família, que consiste em alugar de 3 a 5 bicicletas nos planos')
print('    anteriores e que dá 30% de desconto no valor total do pedido!\n')

print('Digite o valor de 1 a 4 conforme o plano desejado,')
print('digite \"E\" para visualizar a quantidade de biciletas em estoque')
print('ou digite 0 para cancelar.')

opcao = validaEntrada(input('\nQual o plano que você deseja contratar? ').upper())
menuEntradas(opcao)

print('\n##### LOG #####:')
print(f'Cliente - alugarHora está retornando: {cliente.alugarHora}.')
print(f'Cliente - alugarDia está retornando: {cliente.alugarDia}.')
print(f'Cliente - alugarSemana está retornando: {cliente.alugarSemana}.')
print(f'Cliente - alugarFamilia está retornando: {cliente.alugarFamilia}.')

print('\nFim do programa.')

class Loja (object):
    
    def __init__ (self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
    
    # Mostrar o estoque de bicicletas para o Cliente;
    def mostrarEstoque (self):
        return self.estoque

    # Alterar a quantidade do estoque.
    def alterarEstoque (self, baixa):
        self.estoque -= baixa

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a disponibilidade do estoque.
    def receberPedido (self, periodo, quantidade, plano, desconto):
        self.periodo = int(periodo)
        self.quantidade = int(quantidade)
        self.plano = plano
        self.desconto = desconto

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta (self):
        if self.plano == '1':
            if self.desconto:
                total = (self.periodo * self.quantidade * 5) * 0,7
            else:
                total = self.periodo * self.quantidade * 5
        elif self.plano == "2":
            if self.desconto:
                total = (self.periodo * self.quantidade * 25) * 0,7
            else:
                total = self.periodo * self.quantidade * 25
        else:
            if self.desconto:
                total = (self.periodo * self.quantidade * 100) * 0,7
            else:
                total = self.periodo * self.quantidade * 100

class Cliente (object):
    
    def __init__ (self, carteira):
        self.carteira = carteira

    # Alugar bicicletas por hora (R$5/hora);
    def alugarHora (self, periodo):
        self.periodo = periodo
        self.quantidade = 1
        self.plano = 1
        self.desconto = False
    
    # Alugar bicicletas por dia (R$25/dia);
    def alugarDia (self, periodo):
        self.periodo = periodo
        self.quantidade = 1
        self.plano = 2
        self.desconto = False

    # Alugar bicicletas por semana (R$100/semana)
    def alugarSemana (self, periodo):
        self.periodo = periodo
        self.quantidade = 1
        self.plano = 3
        self.desconto = False
    
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.
    def alugarFamilia (self, periodo, quantidade, plano):
        self.periodo = periodo
        self.quantidade = quantidade
        self.plano = plano
        self.desconto = True

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
        print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.')
        entrada = validaEntrada(input('\nQual o plano que você deseja contratar? ').upper())
        menuEntradas(entrada)

    elif entrada == '0':
        print('\nÉ uma pena... Mas aguardamos você numa próxima!')
        
    # Plano Hora
    elif entrada == '1':
        print('\nO plano Passeio foi selecionado!')
        qtdHoras = input('Por quantas horas você deseja alugar? ')
        print(f'Selecionado {qtdHoras} hora(s)!')
        cliente.alugarHora(qtdHoras)

    # Plano Dia
    elif entrada == '2':
        print('\nO plano Diário foi selecionado!')
        qtdDias = input('Por quantos dias você deseja alugar? ')
        print(f'Selecionado {qtdDias} dia(s)!')
        cliente.alugarDia(qtdDias)
        
    # Plano Semana
    elif entrada == '3':
        print('\nO plano Semanal foi selecionado!')
        qtdSemanas = input('Por quantas semanas você deseja alugar? ')
        print(f'Selecionado {qtdSemanas} semana(s)!')
        cliente.alugarSemana(qtdSemanas)
        
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
        periodo = input(f'Por {preenche} você deseja alugar {qtdBicicletas} bicicletas? ')
        
        preenche2 = ""
        if plano == '1':
            preenche2 = 'hora(s)'
        elif plano == '2':
            preenche2 = 'dia(s)'
        else:
            preenche2 = 'semana(s)'
        print(f'Selecionado alugar {qtdBicicletas} bicicletas no Plano {plano} por {periodo} {preenche2}!')
        cliente.alugarFamilia(periodo, qtdBicicletas, plano)

# Init classes
cliente = Cliente(200)
loja = Loja(100, 500)

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
print(f'Cliente - está retornando: Quant. Bicicletas - {cliente.quantidade}, Plano - {cliente.plano} e Período - {cliente.periodo}.')

print('\nFim do programa.')

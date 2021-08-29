from datetime import datetime as dt

class Loja (object):
    
    def __init__ (self, estoque, caixa):
        self.estoque = estoque
        self.caixa = caixa
        self.locacoes = {}
    
    # Mostrar o estoque de bicicletas para o Cliente;
    def mostrarEstoque (self):
        return self.estoque

    # Alterar a quantidade do estoque.
    def alterarEstoque (self, quantidade):
        self.estoque -= quantidade

    # Receber pedidos de aluguéis por hora, diários ou semanais validando a disponibilidade do estoque.
    def receberPedido (self, quantidade):
        if self.estoque >= quantidade:
            return True
        else:
            return False

    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calcularConta (self, listaPedido):
        self.listaPedido = listaPedido
        self.quantidadeLoc = self.listaPedido[0]
        self.diaLoc = self.listaPedido[1]
        self.horaLoc = self.listaPedido[2]
        self.minutosLoc = self.listaPedido[3]
        self.desconto = self.listaPedido[4] # <= Bool
        self.quantidadeDev = self.listaPedido[5]
        self.diaDev = self.listaPedido[6]
        self.horaDev = self.listaPedido[7]
        self.minutosDev = self.listaPedido[8]

class Cliente (object):
    def __init__ (self, carteira):
        self.carteira = carteira

'''
Função para validar a entrada de dados do input do operador da loja:
Argumentos: entrada
Retorna: entrada
'''
def validaEntrada(entrada):
    _opcoes = ('T', 'E', 'C','L', 'D', 'END')
    while entrada not in _opcoes:
        entrada = input('\nOpção inválida! Digite a opção desejada: ').upper()
    return entrada
'''
Função para limitar a a entrada de dados do input do operador da loja:
Argumentos: entrada
Retorna: entrada
'''
def opcoesSistema():
    print('Digite \"T\" para visualizar a tabela de preços;')
    print('Digite \"E\" para visualizar o estoque disponível;')
    print('Digite \"C\" para visualizar os clientes com locações ativas;')
    print('Digite \"L\" para fazer uma nova locação;')
    print('Digite \"D\" para registrar uma devolução;')
    print('Digite \"end\" para encerrar o sistema.')
    opcao = input('Digite a opção desejada: ').upper()
    return opcao

# Init classes
loja = Loja (100, 500)
cliente = Cliente (200)
print('###### Sistema da Locadora de Bicicletas LTDA #####\n')
entrada = validaEntrada(opcoesSistema())

while entrada != 'END':
    if entrada == 'T':
        print('\nConferir a tabela de preços foi selecionado!')
        print('Preço locação por hora: R$ 5,00')
        print('Preço locação por dia: R$ 25,00')
        print('Preço locação por semana: R$ 100,00')
        print('Preço locação família: locar de 3 a 5 bicicletas com desconto de 30%')
        print('em qualquer uma das modalidades de locação anteriores.\n')
        entrada = validaEntrada(opcoesSistema())

    elif entrada == 'E':
        print('\nConferir o estoque disponível foi selecionado!')
        print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.\n')
        entrada = validaEntrada(opcoesSistema())

    elif entrada == 'C':
        print('\nConferir o clientes com locações ativas foi selecionado!')
        print(f'{loja.locacoes.items()}\n')
        entrada = validaEntrada(opcoesSistema())

    elif entrada == "L":
        nomeCliente = input('\nDigite o nome do cliente: ').upper()
        quantLocacao = int(input('Quantas bicicletas o cliente vai alugar? ')) # Try / Except: qualquer coisa que não seja int.
        loja.receberPedido(quantLocacao)
        if loja.receberPedido(quantLocacao):
            dataLocacao = dt.today()
            loja.locacoes[nomeCliente] = {
            'quantidadeLoc': quantLocacao,
            'diaLoc': dataLocacao.day,
            'horaLoc': dataLocacao.hour,
            'minutosLoc': dataLocacao.minute
            }
            loja.alterarEstoque(quantLocacao)
            if quantLocacao in (3, 4, 5):
                loja.locacoes[nomeCliente]['desconto'] = True
            else:
                loja.locacoes[nomeCliente]['desconto'] = False
            print(f'Locação registrada para o cliente {nomeCliente.capitalize()} de {quantLocacao} bicicletas na data de \
                {dataLocacao.day}/{dataLocacao.month}/{dataLocacao.year} às {dataLocacao.hour} hora(s) e {dataLocacao.minute} minuto(s).\n')
        else:
             print(f'Estoque insuficiente! Estoque atual: {loja.mostrarEstoque()}')

        entrada = validaEntrada(opcoesSistema())
    
    else: #devolucao
        nomeCliente = input('\nDigite o nome do cliente: ').upper()
        # Confere se o cliente está no cadastro de locatários
        if nomeCliente in loja.locacoes.keys():
            print(f'Cliente Selecionado: {nomeCliente.capitalize()}: {loja.locacoes[nomeCliente]}.') 
            quantDevolucao = int(input('Quantas bicicletas o cliente vai devolver? '))
            dataDevolucao = input('Qual a data da devolução (Digitar em DD/MM/AAAA)? ').split('/')
            horarioDevolucao = input('Qual o horário da devolução (Digitar em HH:MM)? ').split(':')
            diaDevolucao = dataDevolucao[0]
            horaDevolucao = horarioDevolucao[0]
            minutoDevolucao = horarioDevolucao[1]
            loja.locacoes[nomeCliente]['quantidadeDev'] = quantDevolucao
            loja.locacoes[nomeCliente]['diaDev'] = diaDevolucao
            loja.locacoes[nomeCliente]['horaDev'] = horaDevolucao
            loja.locacoes[nomeCliente]['minutosDev'] = minutoDevolucao
            loja.listaPedido = loja.locacoes[nomeCliente].values()

            print('\n##### LOG #####') # apagar
            print(f'Data devolução: {dataDevolucao}')
            print(f'Dia devolução: {diaDevolucao}')
            print(f'Hora devolução: {horaDevolucao}')
            print(f'Minutos devolução: {minutoDevolucao}')
            print(f'Type Dia devolução: {type(diaDevolucao)}')
            print(f'Type Hora devolução: {type(horaDevolucao)}')
            print(f'Type Minutos devolução: {type(minutoDevolucao)}')
            print(f'Loja - Pedido com dados de devolução - {loja.listaPedido}')
            print(f'Loja - quantidadeLoc - {loja.quantidadeLoc}')
            print(f'Loja - Type quantidadeLoc - {type(loja.quantidadeLoc)}\n')
            
            entrada = validaEntrada(opcoesSistema())

        else:
            print('O Cliente selecionado não consta na base de dados.\n')
            entrada = validaEntrada(opcoesSistema())

print('\nFim do programa.')

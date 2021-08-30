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
        self.quantidadeLoc = listaPedido[0]
        self.desconto = listaPedido[6]
        self.quantidadeDev = listaPedido[7]

        # Recebe a lista "listaDev" e monta as datas no formato datetime conforme os índices
        self.dataLoc = dt(listaPedido[3], listaPedido[2], listaPedido[1], listaPedido[4], listaPedido[5])
        self.dataDev = dt(int(listaPedido[10]), int(listaPedido[9]), int(listaPedido[8]), int(listaPedido[11]), int(listaPedido[12]))
        self.dataDif = self.dataDev - self.dataLoc

        # Faz o cálculo do total a pagar com base em transformar o total do timedelta "self.datadif" em segundos 
        self.totalSemanas = self.dataDif.total_seconds() // 604800  # 604800 segundos em uma semana
        self.sobra = self.dataDif.total_seconds() - self.totalSemanas * 604800
        self.totalDias =  self.sobra // 86400  # 86400 segundos em um dia
        self.sobra = self.sobra - self.totalDias * 86400
        self.totalHoras = self.sobra // 3600  # 3600 segundos em uma hora
        self.sobra = self.sobra - self.totalHoras * 3600
        self.totalMinutos = self.sobra // 60  # 60 segundos em um minuto

        if self.totalMinutos > 15: # 15min de tolerância, senão conta uma hora a mais.
            self.totalHoras += 1
            valorTotal = (self.totalSemanas * 100 + self.totalDias * 25 + self.totalHoras * 5) * self.quantidadeLoc
        else:
            valorTotal = (self.totalSemanas * 100 + self.totalDias * 25 + self.totalHoras * 5) * self.quantidadeLoc

        if self.desconto:
            valorTotal = valorTotal * 0.7
        else:
            valorTotal
        
        return valorTotal

class Cliente (object):
    def __init__ (self, carteira):
        self.carteira = carteira

'''
Função para validar a entrada de dados do input do operador da loja:
Argumentos: entrada
Retorna: entrada
'''
def validaEntrada(entrada):
    _opcoes = ('T', 'E', 'CX', 'C','L', 'D', 'END')
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
    print('Digite \"CX\" para visualizar o valor em caixa;')
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

    elif entrada == 'CX':
        print('\nConferir o valor em caixa foi selecionado!')
        print( f'O valor atual do caixa é de R$ {loja.caixa}\n')
        entrada = validaEntrada(opcoesSistema())

    elif entrada == 'C':
        print('\nConferir o clientes com locações ativas foi selecionado!')
        if not loja.locacoes:
            print('Não há locações registradas.\n')
        else:
            print(f'{loja.locacoes.items()}\n')
        entrada = validaEntrada(opcoesSistema())

    elif entrada == "L":
        nomeCliente = input('\nDigite o nome do cliente: ').upper()
        quantLocacao = int(input('Quantas bicicletas o cliente vai alugar? ')) # <= Try / Except: qualquer coisa que não seja int.
        loja.receberPedido(quantLocacao)
        if loja.receberPedido(quantLocacao):
            dataLocacao = dt.today()
            loja.locacoes[nomeCliente] = {
            'quantidadeLoc': quantLocacao,
            'diaLoc': dataLocacao.day,
            'mesLoc': dataLocacao.month,
            'anoLoc': dataLocacao.year,
            'horaLoc': dataLocacao.hour,
            'minutosLoc': dataLocacao.minute
            }
            loja.alterarEstoque(quantLocacao)
            if quantLocacao in (3, 4, 5):
                loja.locacoes[nomeCliente]['desconto'] = True
            else:
                loja.locacoes[nomeCliente]['desconto'] = False
            print(f'Locação registrada para o cliente {nomeCliente.capitalize()} de {quantLocacao} bicicletas na data de {dataLocacao.day}/{dataLocacao.month}/{dataLocacao.year} às {dataLocacao.hour} hora(s) e {dataLocacao.minute} minuto(s).\n')
        else:
             print(f'Estoque insuficiente! Estoque atual: {loja.mostrarEstoque()}')

        entrada = validaEntrada(opcoesSistema())
    
    else: # Devolução
        nomeCliente = input('\nDigite o nome do cliente: ').upper()
       
        # Confere se o cliente está no cadastro de locatários
        if nomeCliente in loja.locacoes.keys():
            print(f'Cliente Selecionado: {nomeCliente.capitalize()}: {loja.locacoes[nomeCliente]}.') 
            quantDevolucao = int(input('Quantas bicicletas o cliente vai devolver? '))  # <= Try/Except digitar algo não int
            
            # Assegura que o cliente não devolva mais ou menos bicicletas do que alugou.
            if quantDevolucao == loja.locacoes[nomeCliente]['quantidadeLoc']:
                dataDevolucao = input('Qual a data da devolução (Digitar em DD/MM/AAAA)? ').split('/')  # <= Try/Except digitar algo errado
                horarioDevolucao = input('Qual o horário da devolução (Digitar em HH:MM)? ').split(':')  # <= Try/Except digitar algo errado
                diaDevolucao = dataDevolucao[0]
                mesDevolucao = dataDevolucao[1]
                anoDevolucao = dataDevolucao[2]
                horaDevolucao = horarioDevolucao[0]
                minutoDevolucao = horarioDevolucao[1]

                # Atribuição de todos os valores necessários para o cálculo do datetime
                loja.locacoes[nomeCliente]['quantidadeDev'] = quantDevolucao
                loja.locacoes[nomeCliente]['diaDev'] = diaDevolucao
                loja.locacoes[nomeCliente]['mesDev'] = mesDevolucao
                loja.locacoes[nomeCliente]['anoDev'] = anoDevolucao
                loja.locacoes[nomeCliente]['horaDev'] = horaDevolucao
                loja.locacoes[nomeCliente]['minutosDev'] = minutoDevolucao
                
                # Lista para formação dos datetimes:
                listaDev = []
                for i in loja.locacoes[nomeCliente].values():
                    listaDev.append(i)

                # Retorno do valor a pagar e confirmação de pagamento 
                print(f'\nValor a receber: R$ {loja.calcularConta(listaDev)}\n')
                recebido = input('O cliente pagou a conta? (Digite S/N) \n').upper()
                while recebido not in ('S','N'):
                    recebido = input('Entrada inválida! O cliente pagou a conta? (Digite S/N) \n').upper()
                    while recebido != 'S':
                        recebido = input('Cobre o cliente! O cliente pagou a conta? (Digite S/N) \n').upper()
                
                # Update do caixa / carteira cliente
                loja.caixa += loja.calcularConta(listaDev)
                cliente.carteira -= loja.calcularConta(listaDev)

                # Devolução ao estoque e delete do cliente nas locações ativas
                loja.alterarEstoque(quantDevolucao*-1)
                loja.locacoes[nomeCliente].clear()
                
                entrada = validaEntrada(opcoesSistema())
            
            else:
                print(f'A quantidade devolvida está incorreta, repita a operação. Quantidade locada: {loja.locacoes[nomeCliente]["quantidadeLoc"]} | Quantidade devolvida: {quantDevolucao}\n')    
                entrada = validaEntrada(opcoesSistema())

        else:
            print('O Cliente selecionado não consta na base de dados.\n')
            entrada = validaEntrada(opcoesSistema())

print('\nFim do programa.')

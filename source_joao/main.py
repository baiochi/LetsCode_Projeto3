from my_class import Cliente, Loja
from datetime import datetime as dt


"""
classe Cliente:
    atributos:
    - nome: str
    - cpf: str
    métodos:
    - getNome() : retorna o atributo 'nome'
    - getCPF() : retorna o atributo 'cpf'

classe Loja:
    atributos:
    - estoque: int
    - historicoAluguel: lista de dicionários 'aluguel'
        aluguel = {
            'cliente' : Cliente(),
            'quantidade' : int,
            'modeloAluguel': str,       opcoes('hora','dia','semana')
            'dataAluguel': datetime
        }
    - cadastroCliente: lista de objetos Cliente()
    - tabelaPrecos: dicionário = {
                'hora' : 5,
                'dia' : 25,
                'semana' : 100
        }

    métodos:
    - cadastraCliente(cliente = Cliente()): recebe objeto Cliente() e armazena na lista cadastroCliente
    - mostrarEstoque(): retorna o estoque
    - receberPedido(cliente = Cliente(), quantidade = int, modeloAluguel = str, promocaoFamilia = bool):
        recebe o objeto Cliente(), a quantidade de bicicletas, o modelo do aluguel ('hora','dia','semana') e True caso for promocao
        aluguel é armazenado na lista historicoAluguel e diminui o valor do estoque
    - devolverBicicletas(cliente = Cliente()): usa o objeto Cliente() para buscar na base historicoAluguel, diminue o valor do estoque
        retorno faz a chamada do método calcularConta()
    - calcularConta(aluguel): recebe um dicionário contendo as informacoes referentes ao aluguel e retorna o valor total

"""

'''
Função para validar a entrada de dados do input do operador da loja:
Argumentos: entrada
Retorna: entrada
'''
def validaEntrada(entrada):
    _opcoes = ('T', 'E', 'C', 'O', 'END')
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
    print('Digite \"O\" para executar as operações de locação e devolução;')
    print('Digite \"end\" para encerrar o sistema.')
    opcao = input('Digite a opção desejada: ').upper()
    return opcao

# incializando as classes
cliente1 = Cliente('Joao', '123.456.789-00')
cliente2 = Cliente('Maycon', '321.654.987-00')
cliente3 = Cliente('Will', '001.002.003-42')
loja = Loja(10)

# if referente as opções do Menu:
entrada = validaEntrada(opcoesSistema())

while entrada != 'END':
    if entrada == 'T':
        print('\nConferir a tabela de preços foi selecionado!')
        print(f'Preço locação por hora: R$ {loja.tabelaPrecos["hora"]}')
        print(f'Preço locação por dia: R$ {loja.tabelaPrecos["dia"]}')
        print(f'Preço locação por semana: R$ {loja.tabelaPrecos["semana"]}')
        print(f'Preço locação família: locar de 3 a 5 bicicletas com desconto de 30%')
        print(f'em qualquer uma das modalidades de locação anteriores.\n')
        entrada = validaEntrada(opcoesSistema())
    
    elif entrada == 'E':
        print('\nConferir o estoque disponível foi selecionado!')
        print(f'O estoque atual é de {loja.mostrarEstoque()} biciletas disponíveis.\n')
        entrada = validaEntrada(opcoesSistema())
    
    elif entrada == 'C':
        if not loja.cadastroClientes:
            print('Não há locações registradas.\n')
        else:
            print(f'{loja.cadastroClientes}\n')
        entrada = validaEntrada(opcoesSistema())

    else:
        # cliente 1 faz um pedido de 2 biciletas na modalidade hora
        print(f'Cliente {cliente1.getNome()} faz pedido de 2 bicicletas na modalidade HORA')
        loja.receberPedido(cliente = cliente1, quantidade = 2, modeloAluguel = 'hora')
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        # cliente 1 dá uma de john armless para pegar a promocao, deve retornar erro
        print(f'Cliente {cliente1.getNome()} faz pedido de 2 bicicletas na modalidade HORA, tenta desconto')
        loja.receberPedido(cliente = cliente1, quantidade = 2, modeloAluguel = 'hora', promocaoFamilia=True)
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        # cliente 2 faz pedido 4 bicicletas na modalidade semana, com desconto familia
        print(f'Cliente {cliente2.getNome()} faz pedido de 4 bicicletas na modalidade SEMANA, tenta desconto')
        loja.receberPedido(cliente = cliente2, quantidade = 4, modeloAluguel = 'semana', promocaoFamilia=True,\
            dataAluguel = dt(day=19, month=8, year=2021))
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        # cliente 3 faz pedido 5 bicicletas na modalidade dia, sem desconto familia, deve retornar erro
        # (estourar o estoque)
        print(f'Cliente {cliente3.getNome()} faz pedido de 5 bicicletas na modalidade DIA')
        loja.receberPedido(cliente = cliente3, quantidade = 5, modeloAluguel = 'dia')

        # cliente 3 faz pedido 3 bicicletas na modalidade dia, sem desconto familia
        loja.receberPedido(cliente = cliente3, quantidade = 3, modeloAluguel = 'dia', \
            dataAluguel = dt(day=25, month=8, year=2021))
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        # cliente 3 retorna as bicicletas
        print(f'Cliente {cliente3.getNome()} finalizando o aluguel...')
        print(f'O valor da conta ficou em R$ {loja.devolverBicicletas(cliente=cliente3)}')
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        # cliente 2 retorna as bicicletas
        print(f'Cliente {cliente2.getNome()} finalizando o aluguel...')
        print(f'O valor da conta ficou em R$ {loja.devolverBicicletas(cliente=cliente2)}')
        print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

        #testando método mágico __repr__
        print(cliente1)
        print(loja)
        
        entrada = validaEntrada(opcoesSistema())
        
print('end.')

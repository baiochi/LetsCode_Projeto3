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
# incializando as classes
cliente1 = Cliente('Joao', '123.456.789-00')
cliente2 = Cliente('Maycon', '321.654.987-00')
cliente3 = Cliente('Will', '001.002.003-42')
loja = Loja(10)

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
print('end.')

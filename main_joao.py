from class_joao import Cliente, Loja
from datetime import datetime as dt

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
    debug = True, dataTeste = dt(day=19, month=8, year=2021))
print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

# cliente 3 faz pedido 5 bicicletas na modalidade dia, sem desconto familia, deve retornar erro
# (estourar o estoque)
print(f'Cliente {cliente3.getNome()} faz pedido de 5 bicicletas na modalidade DIA')
loja.receberPedido(cliente = cliente3, quantidade = 5, modeloAluguel = 'dia')

# cliente 3 faz pedido 3 bicicletas na modalidade dia, sem desconto familia
loja.receberPedido(cliente = cliente3, quantidade = 3, modeloAluguel = 'dia', \
    debug = True, dataTeste = dt(day=25, month=8, year=2021))
print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

# cliente 3 retorna as bicicletas
print(f'Cliente {cliente3.getNome()} finalizando o aluguel...')
print(f'O valor da conta ficou em R$ {loja.devolverBicicletas(cliente=cliente3)}')
print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

# cliente 2 retorna as bicicletas
print(f'Cliente {cliente2.getNome()} finalizando o aluguel...')
print(f'O valor da conta ficou em R$ {loja.devolverBicicletas(cliente=cliente2)}')
print(f'Estoque atual da loja: {loja.mostrarEstoque()}\n')

# ambiente de testes unitários
import unittest
import math
from my_class import Cliente, Loja
from datetime import datetime as dt

"""
Consulta rápida, apagar ao final.

Method	                Equivalent to
.assertEqual(a, b)	    a == b
.assertTrue(x)	        bool(x) is True
.assertFalse(x)	        bool(x) is False
.assertIs(a, b)	        a is b
.assertIsNone(x)	    x is None
.assertIn(a, b)	        a in b
.assertIsInstance(a, b)	isinstance(a, b)

.assertRaises(): usado para tratar erros esperados já definidos dentro da classe
""" 
"""
Possíveis testes:
- Validar nome (é str?)
- Validar cpf
- Validar outros atributos caso forem adicionados

Exemplos inicializacao:
Cliente(nome = 'Joao', cpf = '123.456.789-00')
Cliente(nome = 'Maycon', cpf = '321.654.987-00')
Cliente(nome = 'Will', cpf = '001.002.003-42')
"""

class ClienteTests(unittest.TestCase):

    # definir os valores dos atributos para teste
    def setUp(self):
        self.cliente = Cliente(nome = 'joao', cpf = '123.456.789-00')


"""
Possíveis testes:
- Pedir quantidade superior ao estoque
- Tenta aplicar a promocao com quantidade menor que 3 ou maior que 5
- Tentar devolver o aluguel antes do tempo programado (programa aceita ou dá erro?)
- Testar cálculo de possível resultado negativo na devolucao, e.g.
    1) Data início 17:55, data retorno 19:15. Minutos finais - Minutos iniciais terá resultado negativo?
    2) Data início 29/08, data retorno 03/09. Dias finais - dias iniciais terá resultado negativo?
- Loja recebe modalidade de aluguel inválido, e.g. "quinzenal"
-

Exemplos inicializacao:
Loja(estoque = 10)
"""
class LojaTests(unittest.TestCase):

    # definir os valores dos atributos para teste
    def setUp(self):
        self.loja = Loja(estoque = 10)
    
    def testeCadastrarCliente(self): #OK
        print("Testando o cadastro de cliente:")
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        self.assertIsNotNone(self.loja.cadastroClientes) # verifica se a lista está vazia

    def testeCadastrarClienteDuplicado(self): #OK
        print("Testando o cadastro de cliente em duplicata:")
        # adiciona o cliente pela primeira vez
        self.loja.cadastraCliente(Cliente(nome = 'joao', cpf = '123.456.789-00'))

        # passa no teste se acontecer o erro esperado dentro do método cadastraCliente()
        with self.assertRaises(ValueError):
            # tenta adicionar pela segunda vez
            self.loja.cadastraCliente(Cliente(nome = 'joao', cpf = '123.456.789-00'))
    
    def testeRecebePedido(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # faz o pedido
        self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 1, modeloAluguel = 'hora')
        # verifica se o histórico de aluguel está vazio
        self.assertIsNotNone(self.loja.historicoAluguel)
        # raise TypeError('Quantidade inválida para validar a promoção.')
        pass

    def testeVerificarEstoqueDiminuiu(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # faz o pedido
        self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 5, modeloAluguel = 'hora')
        # verifica se o estoque foi atualizado
        self.assertEqual(self.loja.estoque, 5)

    def testeVerificarEstoqueAumentou(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # faz o pedido
        self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 5, modeloAluguel = 'hora')
        # cliente devolve o pedido
        self.loja.devolverBicicletas(cliente = self.loja.cadastroClientes[0])
        # verifica se o estoque foi atualizado
        self.assertEqual(self.loja.estoque, 10)

    def testeRecebePedidoSemEstoque(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # faz o pedido sem o estoque necessario
        with self.assertRaises(ValueError):
            self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 3650, modeloAluguel = 'hora')

    def testeModeloAluguelInvalido(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # tenta usar a modalidade do aluguel em minutos
        with self.assertRaises(NameError):
            self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 5, modeloAluguel = 'minutos')

    def testeRecebePedidoPromocaoInvalida(self): #OK
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # tenta dar o migué da promocao
        with self.assertRaises(TypeError):
            self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 1, \
                modeloAluguel = 'hora', promocaoFamilia = True)

    def testecalcularContaHora(self): # OK
        
        # já testa os dois casos, com ou sem promocao
        for promocao in (False, True):
            quantidade = 3
            modeloAluguel = 'hora'
            dataAluguel = dt(2021,8,29, 12, 15, 0)  #12:15:00
            dataAtual = dt(2021,8,29, 15, 15, 0)    #15:15:00
            aluguel = {
                    'cliente': Cliente(nome = 'joao', cpf = '123.456.789-00'),
                    'quantidade': quantidade,
                    'modeloAluguel': modeloAluguel,
                    'dataAluguel': dataAluguel,
                    'promocaoFamilia': promocao
                }
            valorTestado = self.loja.calcularConta(aluguel = aluguel, debug = True, dataAtual = dataAtual)
            # 3 biciletas * 3 horas * 5 reais/hora
            valorEsperado = quantidade * (dataAtual.hour - dataAluguel.hour) * 5
            # aplica a promocao se true
            if promocao: valorEsperado *= 0.7
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado) 

    def testecalcularContaDia(self, promocao = False): # OK

        # já testa os dois casos, com ou sem promocao
        for promocao in (False, True):
            quantidade = 3
            modeloAluguel = 'dia'
            dataAluguel = dt(2021,8,28, 15, 15, 0)  #28/08/2021
            dataAtual = dt(2021,8,30, 12, 15, 0)    #30/08/2021
            aluguel = {
                    'cliente': Cliente(nome = 'joao', cpf = '123.456.789-00'),
                    'quantidade': quantidade,
                    'modeloAluguel': modeloAluguel,
                    'dataAluguel': dataAluguel, 
                    'promocaoFamilia': promocao
                }
            
            valorTestado = self.loja.calcularConta(aluguel = aluguel, debug = True, dataAtual = dataAtual) #30/08/2021
            # 3 biciletas * 2 dias * 25 reais/dia
            valorEsperado = quantidade * (dataAtual.day - dataAluguel.day) * 25
            # aplica a promocao se true
            if promocao: valorEsperado *= 0.7
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado) 

    def testecalcularContaSemana(self, promocao = False): # OK

        # já testa os dois casos, com ou sem promocao
        for promocao in (False, True):
            quantidade = 3
            modeloAluguel = 'semana'
            dataAluguel = dt(2021,9,11, 15, 15, 0)  #11/09/2021
            dataAtual = dt(2021,8,29, 12, 15, 0)    #29/08/2021
            aluguel = {
                    'cliente': Cliente(nome = 'joao', cpf = '123.456.789-00'),
                    'quantidade': quantidade,
                    'modeloAluguel': modeloAluguel,
                    'dataAluguel': dataAluguel,  #11/09/2021
                    'promocaoFamilia': promocao
                }
            
            valorTestado = self.loja.calcularConta(aluguel = aluguel, debug = True, dataAtual = dataAtual) #29/08/2021
            # 3 biciletas * 2,5 semanas * 100 reais/semana
            valorEsperado = quantidade * math.ceil((dataAtual.day - dataAluguel.day)/7) * 100
            # aplica a promocao se true
            if promocao: valorEsperado *= 0.7
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado) 

    def testeRecebePedidoInvalido(self):
        pass

    def testeDevolverBicicletas(self):
        pass


# Este método executa todos os testes das classes anteriores
if __name__ == '__main__':
    unittest.main()
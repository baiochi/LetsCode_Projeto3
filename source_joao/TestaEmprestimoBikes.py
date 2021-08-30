# ambiente de testes unitários
import unittest
import math
from my_class import *
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
        print(colorText("[[cyan]]\nTestando o cadastro de cliente:[[white]]\n"))
        self.loja.cadastraCliente(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        self.assertIsNotNone(self.loja.cadastroClientes) # verifica se a lista está vazia

        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeCadastrarClienteDuplicado(self): #OK
        print(colorText("[[cyan]]\nTestando o cadastro de cliente em duplicata:[[white]]\n"))
        # adiciona o cliente pela primeira vez
        self.loja.cadastraCliente(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # passa no teste se acontecer o erro esperado dentro do método cadastraCliente()
        with self.assertRaises(ValueError):
            # tenta adicionar pela segunda vez
            self.loja.cadastraCliente(Cliente(nome = 'joao', cpf = '123.456.789-00'))
            
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeRecebePedido(self): #OK
        print(colorText("[[cyan]]\nTestando receber o pedido:[[white]]\n"))
        # faz o pedido
        self.loja.receberPedido(cliente = Cliente(nome = 'joao', cpf = '123.456.789-00'), quantidade = 1, modeloAluguel = 'hora')
        # verifica se o histórico de aluguel está vazio
        self.assertIsNotNone(self.loja.historicoAluguel)
        
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeVerificarEstoqueDiminuiu(self): #OK
        print(colorText("[[cyan]]\nTestando verificar se o estoque diminuiu após receber pedido:[[white]]\n"))
        # faz o pedido
        self.loja.receberPedido(cliente = Cliente(nome = 'joao', cpf = '123.456.789-00'), quantidade = 5, modeloAluguel = 'hora')
        # verifica se o estoque foi atualizado
        self.assertEqual(self.loja.estoque, 5)
        
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeVerificarEstoqueAumentou(self): #OK
        print(colorText("[[cyan]]\nTestando verificar se o estoque aumentou após devolucao:[[white]]\n"))
        # adiciona o cliente
        self.loja.cadastroClientes.append(Cliente(nome = 'joao', cpf = '123.456.789-00'))
        # faz o pedido
        self.loja.receberPedido(cliente = self.loja.cadastroClientes[0], quantidade = 5, modeloAluguel = 'hora')
        # cliente devolve o pedido
        self.loja.devolverBicicletas(cliente = self.loja.cadastroClientes[0])
        # verifica se o estoque foi atualizado
        self.assertEqual(self.loja.estoque, 10)
        
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeRecebePedidoSemEstoque(self): #OK
        print(colorText("[[cyan]]\nTestando receber pedidos sem o estoque:[[white]]\n"))
        # faz o pedido sem o estoque necessario
        with self.assertRaises(ValueError):
            self.loja.receberPedido(cliente = Cliente(nome = 'joao', cpf = '123.456.789-00'), quantidade = 3650, modeloAluguel = 'hora')
            
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeModeloAluguelInvalido(self): #OK
        print(colorText("[[cyan]]\nTestando receber pedido com modelo de aluguel inválido:[[white]]\n"))
        # tenta usar a modalidade do aluguel em minutos
        with self.assertRaises(NameError):
            self.loja.receberPedido(cliente = Cliente(nome = 'joao', cpf = '123.456.789-00'), quantidade = 5, modeloAluguel = 'minutos')
            
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testeRecebePedidoPromocaoInvalida(self): #OK
        print(colorText("[[cyan]]\nTestando receber pedido com promocao inválida:[[white]]\n"))
        # tenta dar o migué da promocao
        with self.assertRaises(TypeError):
            self.loja.receberPedido(cliente = Cliente(nome = 'joao', cpf = '123.456.789-00'), quantidade = 1, \
                modeloAluguel = 'hora', promocaoFamilia = True)
                
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testecalcularContaHora(self): # OK
        print(colorText("[[cyan]]\nTestando calculo da conta na modalidade Hora:[[white]]\n"))
        dataAluguel = dt(2021,8,29, 12, 15, 0)      #12:15:00
        dataRetorno = dt(2021,8,29, 15, 15, 0)      #15:15:00

        # já testa os dois casos, com ou sem promocao
        for index, promocao, nome in (0, False, 'Maria'), (1,True, 'José'):
            #faz o pedido
            self.loja.receberPedido(cliente = Cliente(nome = nome, cpf = '123'), quantidade = 3, \
                modeloAluguel = 'hora', promocaoFamilia = promocao, dataAluguel= dataAluguel)
            # chamada para calcular o valor testado
            valorTestado = self.loja.calcularConta(aluguel = self.loja.historicoAluguel[index], dataRetorno = dataRetorno)

            # calculando o valor para comprar
            dataCalculada = formatarData(dataAluguel = dataAluguel, dataRetorno = dataRetorno)
            valorEsperado = dataCalculada['horas'] * self.loja.historicoAluguel[index]['quantidade'] * self.loja.tabelaPrecos['hora']
            # validação da promoção (desconto 30%)
            if self.loja.historicoAluguel[index]['promocaoFamilia']: valorEsperado *= 0.7
            # tratamento de tolerancia/multa, adiciona o valor de 1 hora, nao aplicando a promocao
            if dataCalculada['minutos'] > 15:
                valorEsperado += 5
            
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado)
            
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testecalcularContaDia(self): # OK
        print(colorText("[[cyan]]\nTestando calculo da conta na modalidade Dia:[[white]]\n"))

        dataAluguel = dt(2021,8,28, 15, 15, 0)      #28/08/2021
        dataRetorno = dt(2021,8,30, 12, 15, 0)      #30/08/2021

        # já testa os dois casos, com ou sem promocao
        for index, promocao, nome in (0, False, 'Maria'),(1,True, 'José'):
            #faz o pedido
            self.loja.receberPedido(cliente = Cliente(nome = nome, cpf = '123'), quantidade = 3, \
                modeloAluguel = 'dia', promocaoFamilia = promocao, dataAluguel= dataAluguel)
            # chamada para calcular o valor testado
            valorTestado = self.loja.calcularConta(aluguel = self.loja.historicoAluguel[index], dataRetorno = dataRetorno)
            
            # calculando o valor para comprar
            dataCalculada = formatarData(dataAluguel = dataAluguel, dataRetorno = dataRetorno)
            valorEsperado = dataCalculada['dias'] * self.loja.historicoAluguel[index]['quantidade'] * self.loja.tabelaPrecos['dia']
            # validação da promoção (desconto 30%)
            if self.loja.historicoAluguel[index]['promocaoFamilia']: valorEsperado *= 0.7
            # tratamento de tolerancia/multa, passada 3 horas, adiciona multa a cada hora, nao aplicando a promocao
            if dataCalculada['horas'] > 3:
                valorEsperado += dataCalculada['horas'] * self.loja.tabelaPrecos['hora']
            
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado) 
            
        print(colorText("[[green]]Sucesso![[white]]\n"))

    def testecalcularContaSemana(self): # OK
        print(colorText("[[cyan]]\nTestando calculo da conta na modalidade Semana:[[white]]\n"))
        
        dataAluguel = dt(2021,9,11, 15, 15, 0)      #11/09/2021
        dataRetorno = dt(2021,8,29, 12, 15, 0)      #29/08/2021

        # já testa os dois casos, com ou sem promocao
        for index, promocao, nome in (0, False, 'Maria'),(1,True, 'José'):
            #faz o pedido
            self.loja.receberPedido(cliente = Cliente(nome = nome, cpf = '123'), quantidade = 3, \
                modeloAluguel = 'semana', promocaoFamilia = promocao, dataAluguel= dataAluguel)
            # chamada para calcular o valor testado
            valorTestado = self.loja.calcularConta(aluguel = self.loja.historicoAluguel[index], dataRetorno = dataRetorno)
            
            # calculando o valor para comprar
            dataCalculada = formatarData(dataAluguel = dataAluguel, dataRetorno = dataRetorno)
            valorEsperado = dataCalculada['semanas'] * self.loja.historicoAluguel[index]['quantidade'] * self.loja.tabelaPrecos['semana']
            # validação da promoção (desconto 30%)
            if self.loja.historicoAluguel[index]['promocaoFamilia']: valorEsperado *= 0.7
            if dataCalculada['dias'] > 0:
                valorEsperado += dataCalculada['dias'] * self.loja.tabelaPrecos['dia']
            # verifica se o valor foi calculado corretamente
            self.assertEqual(valorTestado, valorEsperado)
            
        print(colorText("[[green]]Sucesso![[white]]\n"))


# Este método executa todos os testes das classes anteriores
if __name__ == '__main__':
    unittest.main()
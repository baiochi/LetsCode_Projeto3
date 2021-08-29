# ambiente de testes unitários
import unittest
from class_joao import Cliente, Loja
from datetime import datetime as dt

"""
Possíveis testes:
- Validar nome (é str?)
- Validar cpf
- Validar outros atributos caso forem adicionados
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
"""
class LojaTests(unittest.TestCase):

    # definir os valores dos atributos para teste
    def setUp(self):
        self.loja = Loja(estoque = 10)



# Este método executa todos os testes das classes anteriores
if __name__ == '__main__':
    unittest.main()
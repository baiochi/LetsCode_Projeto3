from datetime import date as dtd
from datetime import time as dtt

class Cliente (object):
    def __init__ (self, carteira):
        self.carteira = 1000

    # Ver as bicicletas disponíveis na Loja; 
    def checarEstoque (self):
        pass
    
    # Alugar bicicletas por hora (R$5/hora);
    def aluguelHora (self):
        pass
    
    # Alugar bicicletas por dia (R$25/dia);
    def aluguelDia (self):
        pass

    # Alugar bicicletas por semana (R$100/semana)
    def aluguelSemana (self):
        pass
    
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.
    def aluguelFamilia (self):
        pass


class Loja (object):
    def __init__ (self):
        self.estoque = 100
    
    # Mostrar o estoque de bicicletas;
    def mostraEstoque (self, estoque):
        print(f'O estoque atual é de {estoque} bicicleta(s).')
        return estoque
    
    # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    def recebePedido (self):
        pass
    
    # Calcular a conta quando o cliente decidir devolver a bicicleta;
    def calculaConta (self):
        pass

# Tupla para selecionar as opções de alguel que o cliente vai ter.
opcoes = (1, 2, 3, 4)

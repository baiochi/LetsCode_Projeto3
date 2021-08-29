import datetime

class Cliente(object):
    def __init__(self, nome):
        self.cliente = nome
    
    # Ver as bicicletas disponíveis na Loja;
    def disponivel(self, loja):
       print(f'Quantidade de bicicletas disponiveis: {loja.estoque}')

    # Alugar bicicletas:
    #   por hora (R$5/hora);
    #   por dia (R$25/dia);
    #   por semana (R$100/semana)
    # Aluguel para família, uma promoção que pode incluir de 3 a 5 empréstimos
    # (de qualquer tipo) com 30% de desconto no valor total.

    def alugar(self, loja):
        try: 
            self.quantidadeAlugada = int(input('Informe a quantidade de bicicletas que deseja alugar: '))
            if self.quantidadeAlugada > loja.estoque:
                raise ValueError
            mes = int(input('Informe o mês do aluguel: '))
            dia = int(input('Informe o dia do aluguel: '))
            self.dataInicial = datetime.date(2021, mes, dia)
            hora = int(input('Informe a hora Inicial: '))
            self.horaInicial = datetime.time(hora, 0)  
        except ValueError:
            print('Você deseja alugar {} bicicletas, mas a loja só tem {}'.format(self.quantidadeAlugada, loja.estoque))
            self.alugar(loja)               
    
    def devolver(self, loja):
        try:
            self.quantidadeDevolvida = int(input('Informe a quantidade de bicicletas que deseja devolver: '))
            if self.quantidadeDevolvida > self.quantidadeAlugada:
                raise ValueError
            mes = int(input('Informe o mês da devolução: '))
            dia = int(input('Informe o dia da devolução: '))
            self.dataFinal = datetime.date(2021, mes, dia)
            self.horaFinal = int(input('Informe a hora da devolução: '))
            loja.conta('informar parametros necessarios')
        except ValueError:
            print('Você alugou: {} bicicletas, e deseja devolver {}. informe um valor valido'.format(self.quantidadeAlugada, self.quantidadeDevolvida)

    
class Loja(object):
    def __init__(self):
        self.estoque = 100
    
    def conta(self, cliente):
        horas = cliente.horaFinal - cliente.horaInicial
        dias = cliente.dataFinal - cliente.dataInicial
        dias += horas // 24
        if horas > 5:
            dias += 1
        semanas = dias // 7
            

    

        quantidade = cliente.quantidadeDevolvida
        valorAPagar = 
        # Calcular a conta quando o cliente decidir devolver a bicicleta;
        # Mostrar o estoque de bicicletas;
        # Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.
    
        
# Simulação de alugueis:


Matriz = Loja()
cliente1 = Cliente('jose')
cliente.disponivel(Matriz)

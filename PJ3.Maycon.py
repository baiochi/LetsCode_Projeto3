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
            self.horaInicial = int(input('Informe a hora Inicial: '))
            self.dataInicial = datetime.datetime(2021, mes, dia)
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
            self.horaFinal = int(input('Informe a hora da devolução: '))
            self.dataFinal = datetime.datetime(2021, mes, dia)
            loja.conta(cliente)
            self.quantidadeAlugada -= self.quantidadeDevolvida
        except ValueError:
            print('Você alugou: {} bicicletas, e deseja devolver {}. informe um valor valido'.format(self.quantidadeAlugada, self.quantidadeDevolvida)





class Loja(object):


    def __init__(self):
        self.estoque = 100
    

    def conta(self, cliente, quantidade):

        if cliente.horaFinal < cliente.horaInicial:
            horas = cliente.horaFinal
            horas += (24 - cliente.horaInicial)
        else:
            horas = cliente.horaFinal - cliente.horaInicial
        horasAluguel = horas        #Distinção entre as horas para calculo e horas alugadas reais
        dias = cliente.dataFinal - cliente.dataInicial
        diasAluguel = dias
        if horas >= 5:
            dias += 1
            horas = 0
        semanas = dias // 7
        semanasAluguel = diasAluguel // 7
        dias = dias % 7
        diasAluguel = diasAluguel % 7
        if dias >= 4:
            semanas += 1
            dias = 0

        fatorCobranca = (semanas * 100) + (dias * 25) + (horas * 5)
        if cliente.quantidadeAlugada > 3 and cliente.quantidadeAlugada < 5:
            descontoFamilia = 30%
        else:
            descontoFamilia = 0%
        valorCobranca = fatorCobranca * cliente.quantidadeDevolvida
        valorDesconto = valorCobranca * descontoFamilia
        valorPagar = valorCobranca - DescontoFamilia
        
        print(f'Você devolveu {cliente.quantidadeDevolvida} bicicletas, de um total de {cliente.quantidadeAlugada} bicicletas alugadas!')
        print(f'Periodo de locação: {semanasAluguel} semanas, {diasAluguel} dias e {horasAluguel} horas')
        print(f'O valor total: R$ {valorCobranca}')
        print(f'Desconto de aluguel familia ({descontoFamilia}): R$ {valorDesconto}')
        print(f'Valor a pagar: R$ {valorPagar}')

    

# Calcular a conta quando o cliente decidir devolver a bicicleta;
# Mostrar o estoque de bicicletas;
# Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque.        
# Simulação de alugueis:


matriz = Loja()
clienteA = Cliente()
clienteA.disponivel(matriz)
clienteA.alugar

from random import randint
from utility import leia_din, erro
from utility import cor


class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cliente(Pessoa):
    def __init__(self, name, age, agencia):
        super().__init__(name, age)
        self.conta_c = ContaCorrente(agencia)
        self.conta_p = ContaPoupanca(agencia)


class Conta:
    def __init__(self, agencia):
        self.conta = randint(00000000,99999999)
        self.agencia = agencia
        self.saldo = 100
        self.limite = 15000

    def depositar(self, valor):
        self.saldo += valor
        print(f'{cor[2]}{leia_din(valor)} depositados com sucesso!{cor[0]}')
        print(f'{cor[5]}Novo saldo: {leia_din(self.saldo)}{cor[0]}')

    def sacar(self, valor, banco, cliente):
        if banco.autenticar(cliente, self.conta):
            if valor <= self.limite and valor <= self.saldo:
                self.saldo -= valor
                self.limite -= valor
                print(f'{cor[2]}{leia_din(valor)} sacados com Sucesso!{cor[0]}')
                print(f'{cor[2]}Saldo atual: {leia_din(self.saldo)}{cor[0]}') #TODO Transformar em função
                print(f'{cor[5]}Limite de saque: {leia_din(self.limite)}{cor[0]}')
            else:
                print(f'{cor[1]}Erro ao Validar a operação, Verifique seu saldo e limite diário{cor[0]}')
                print(f'{cor[2]}Saldo atual: {leia_din(self.saldo)}{cor[0]}')
                print(f'{cor[5]}Limite de saque: {leia_din(self.limite)}{cor[0]}')
        else:
            erro('Saque não autorizado!')



class ContaCorrente(Conta):
    def __init__(self, agencia):
        super().__init__(agencia)
        self.nome = 'Conta corrente'
        self.limite = self.limite + 5000

class ContaPoupanca(Conta):
    def __init__(self, agencia):
        self.nome = 'Conta poupança'
        super().__init__(agencia)

class Banco:
    def __init__(self, nome):
        self.nome = nome.capitalize()
        self.clientes = []
        self.agencias = randint(1000, 9999)
        self.contas = []

    def adc(self, name, age):
        cliente = Cliente(name, age, self.agencias)
        self.clientes.append(cliente)
        self.contas.append(cliente.conta_c.conta)
        self.contas.append(cliente.conta_p.conta)

        print(f'{cor[2]}Cliente {cliente.name} adicionado com Sucesso!{cor[0]}')
        return cliente

    def autenticar(self, client, conta):
        if client not in self.clientes:
            erro('Cliente não encontrado')
            return False
        if conta not in self.contas:
            erro('Conta não encontrada')
            return False
        if client.conta_c.agencia != self.agencias:
            erro('Agência não encontrada')
            return False

        return True


#todo PRIVAR atributo SALDO, Deposito, saque
#DEBUG

# bradesco = Banco('o')
# nubank = Banco('b')
# cliente2 = nubank.adc('Maria Chaplin', 20)
# cliente2.conta_c.depositar(200000)
# print(f'Conta corrente: {cliente2.conta_c.saldo}')
# print(f'Conta poupança: {cliente2.conta_p.saldo}')
# cliente2.conta_p.sacar(40, bradesco, cliente2)
# cliente2.conta_p.depositar()

# bk = Banco('bk')
# c5 = bk.adc('Marretada', 24)
# interBank = Banco('InterBank')
# cliente3 = interBank.adc('ASD', 23)
#
#
#
# cliente3.conta_c.conta = 1
# bk.contas[0] = 2
# bk.contas[1] = c5.conta_p.conta
#
# print(bk.contas)
# print(c5.conta_p.conta)
# print(c5.conta_c.conta)
# bk.agencias = 99999
#
# c5.conta_p.sacar(20, bk, c5)






# cliente1 = bradesco.adc('Pedro Guimarães', 30)
# cliente1.conta_c.sacar(50, bradesco, cliente1)



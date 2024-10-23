from random import randint
from utility import leia_din, erro, cor
from files import check_file, update_file


fileName = 'files/clients.csv'
check_file(fileName)

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
        self.conta = randint(00000000,99999999) # ÚNICO
        self.agencia = agencia # ÚNICO, MAS JA FOI PASSADO!
        self.saldo = 100 # ÚNICO
        self.limite = 15000

    def depositar(self, valor):
        self.saldo += valor
        print(f'{cor[2]}{leia_din(valor)} depositados com sucesso!{cor[0]}')
        print(f'{cor[5]}Novo saldo: {leia_din(self.saldo)}{cor[0]}')

    def sacar(self, valor, banco, cliente, bancos):
        if banco.autenticar(cliente, self.conta):
            if valor <= self.limite and valor <= self.saldo:
                self.saldo -= valor
                self.limite -= valor
                print(f'{cor[2]}{leia_din(valor)} sacados com Sucesso!{cor[0]}')
                print(f'{cor[2]}Saldo atual: {leia_din(self.saldo)}{cor[0]}') #TODO Transformar em função
                print(f'{cor[5]}Limite de saque: {leia_din(self.limite)}{cor[0]}')

                update_file(fileName, bancos)

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





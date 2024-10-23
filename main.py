from classes import *
from files import read_file
from utility import *
from time import sleep

bradesco = Banco('bradesco')
nubank = Banco('nubank')
bancos = [bradesco, nubank]
nubank.agencias = 7845
bradesco.agencias = 2268

read_file(fileName, bancos)

# cliente2 = nubank.adc('Maria M', 20)
# cliente3 = bradesco.adc('Julio B', 40)
# cliente = nubank.adc('Julio B', 40) # BANCO, FICA RESPONSÁVEL POR PASSAR A AGÊNCIA.
# cliente.conta_p.conta = 56177189
# cliente.conta_p.saldo = 100
# cliente.conta_c.conta = 35108463
# cliente.conta_c.saldo = 12000


# #TODO criar dados persistente
#
opcao = ['Listar Bancos', 'Sair do Programa']
opcao2 = ['Criar Cliente', 'Listar Clientes','Sacar', 'Depositar', 'Saldo','Voltar']


while True:
    msg('Sistema Bancário')
    for pos, o in enumerate(opcao):
        print(f'{cor[3]}[ {pos+1} ]{cor[0]} - {cor[4]}{o}{cor[0]}')
    opcMenu = leia_int(f'Selecione uma Opção: ')


    if opcMenu == 1:
        msg('Bancos disponiveis: ')
        sel = listar_b(bancos)
        banco = bancos[sel]

        while True:
            msg(f'Banco Internacional {banco.nome}')
            for pos, o in enumerate(opcao2):
                print(f'{cor[3]}[ {pos + 1} ]{cor[0]} - {cor[4]}{o}{cor[0]}')
            opc = leia_int(f'Selecione uma Opção: ')

            if opc == 1: # CRIA CLIENTES
                msg('Criando cliente')

                dados = vef_cliente()
                banco.adc(dados[0], dados[1])


            if opc == 2: # LISTA CLIENTES
                msg(f'Clientes {banco.nome}')
                for c in banco.clientes:
                    print(f'{cor[2]}{c.name}{cor[0]}')
                sleep(2)

            if opc == 3: # SACA DINHEIRO
                msg(f'Sacar [Caixa 24 Horas] {banco.nome}')

                for p, c in enumerate(banco.clientes):
                    print(f'{cor[3]}[ {p+1} ]{cor[0]} - {cor[4]}{c.name}{cor[0]}')
                sel = leia_int('Selecione um cliente: ')
                cliente = banco.clientes[sel-1]
                print(f'{cor[5]}Saldos:{cor[0]}')
                print(f'{cor[4]}Conta corrente:{cor[2]} {leia_din(cliente.conta_c.saldo)}{cor[0]}')
                print(f'{cor[4]}Conta poupança:{cor[2]} {leia_din(cliente.conta_p.saldo)}{cor[0]}')

                print(f'{cor[3]}[ 1 ]{cor[0]} - {cor[4]}Conta corrente{cor[0]}')
                print(f'{cor[3]}[ 2 ]{cor[0]} - {cor[4]}Conta poupança{cor[0]}')
                sel = leia_int('Selecionar conta: ')
                if sel == 1:
                    valor = leia_float('Digite o valor R$: ')
                    cliente.conta_c.sacar(valor, banco, cliente)
                if sel == 2:
                    valor = leia_float('Digite o valor R$: ')
                    cliente.conta_p.sacar(valor, banco, cliente)

            if opc == 4: # DEPOSITA
                msg(f'Depositos Banco {banco.nome}')

                for p, c in enumerate(banco.clientes):
                    print(f'{cor[3]}[ {p + 1} ]{cor[0]} - {cor[4]}{c.name}{cor[0]}')
                sel = leia_int('Selecione um cliente: ')
                cliente = banco.clientes[sel - 1]
                print(f'{cor[3]}[ 1 ]{cor[0]} - {cor[4]}Conta corrente{cor[0]}')
                print(f'{cor[3]}[ 2 ]{cor[0]} - {cor[4]}Conta poupança{cor[0]}')
                sel = leia_int('Selecionar conta: ')
                if sel == 1:
                    msg('Conta Corrente')
                    valor = leia_float('Digite o valor R$: ')
                    cliente.conta_c.depositar(valor)
                if sel == 2:
                    msg('Conta Poupança')
                    valor = leia_float('Digite o valor R$: ')
                    cliente.conta_p.depositar(valor)

            if opc == 5:
                for p, c in enumerate(banco.clientes):
                    print(f'{cor[3]}[ {p + 1} ]{cor[0]} - {cor[4]}{c.name}{cor[0]}')
                sel = leia_int('Selecione um cliente: ')
                cliente = banco.clientes[sel - 1] # todo Corrijir passar numero maior do que a lista de clientes.
                print(f'{cor[5]}Saldos:{cor[0]}')
                print(f'{cor[4]}Conta corrente:{cor[2]} {leia_din(cliente.conta_c.saldo)}{cor[0]}')
                print(f'{cor[4]}Conta poupança:{cor[2]} {leia_din(cliente.conta_p.saldo)}{cor[0]}')
                sleep(2)

            if opc == 6:
                print(f'{cor[2]}Voltando ao Menu Principal...{cor[0]}')
                sleep(1)
                break

    if opcMenu == 2:
        print(f'{cor[2]}Finalizando Programa...{cor[0]}')
        sleep(2)
        break

# bradesco = Banco()
# nubank = Banco()
# cliente2 = nubank.adc('Maria Chaplin', 20)
# cliente2.conta_p.sacar(40, bradesco, cliente2)
#
#
# cliente1 = bradesco.adc('Pedro Guimarães', 30)
# cliente1.conta_c.sacar(50, bradesco, cliente1)


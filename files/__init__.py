import csv
import os.path


def check_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'wt') as file:
            file.write(f'nome,idade,agencia,conta_p,saldo_p,conta_c,saldo_c,banco\n')
        print('Arquivo não encontrado, criando...')

def write_file(file_name, cliente, b_nome): # RECEBE UM OBJETO
    with open(file_name, 'at', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow([cliente.name, cliente.age, cliente.conta_p.agencia, cliente.conta_p.conta, cliente.conta_p.saldo , cliente.conta_c.conta, cliente.conta_c.saldo,
                         b_nome,])




def read_file(file_name, bancos):
    with open(file_name, 'rt', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for cliente in reader:
            for banco in bancos: # Seleciona o banco do cliente.
                if cliente['banco'].lower() == banco.nome.lower():
                    bank = banco

            client = bank.adc(cliente['nome'],cliente['idade'])  # BANCO, FICA RESPONSÁVEL POR PASSAR A AGÊNCIA.
            client.conta_p.conta = cliente['conta_p']
            client.conta_p.saldo = cliente['saldo_p']
            client.conta_c.conta = cliente['conta_c']
            client.conta_c.saldo = cliente['saldo_c']




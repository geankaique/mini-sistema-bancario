
cor = ('\033[m', # reset
       '\033[31;1m', # red  # ERROS
       '\033[32;1m', # green # OK/SALDO
       '\033[36;1m', # blue   # SELECTS
        '\033[33;1m',# yellow
       '\033[34;1m') # DarkBlue

tam2 = 50
c2 = '-'

def linha(tam=tam2, char=c2):
    print(f'{cor[5]}{char}{cor[0]}' * tam)

def msg(mensagem, char=c2, tam=tam2):
    if char == '':
        print(f'{cor[5]}{mensagem:^{tam}}{cor[0]}')
    else:
        linha()
        print(f'{cor[5]}{mensagem:^{tam}}{cor[0]}')
        linha()

def leia_int(txt):
    while True:
        try:
            n = int(input(f'{cor[3]}{txt}{cor[0]}'))
        except ValueError:
            print(f'{cor[1]}ERRO digite um número inteiro válido!{cor[0]}')
        else:
            return n

def leia_float(txt):
    while True:
        try:
            n = float(input(f'{cor[2]}{txt}{cor[0]}').replace(',', '.', 1).strip())
        except ValueError:
            print(f'{cor[1]}ERRO digite um número válido!{cor[0]}')
        else:
            return n

def leia_din(n):
    return f'R${float(n):.2f}'.replace('.', ',')

def vef_cliente():
    while True:
        nome = input(f'{cor[3]}Nome do cliente: {cor[0]}')
        idade = leia_int('Idade do Cliente: ')
        while True:
            linha()
            print(f'{cor[5]}Cliente: {nome}')
            print(f'Idade: {idade}{cor[0]}')
            conf = input(f'{cor[3]}Os dados estão corretos? [S/N]{cor[0]} ')
            if conf[0] in 'SsNn':
                break
        if conf[0] in 'Ss':
            return nome, idade

def listar_b(lista):
    for pos, b in enumerate(lista):
        print(f'{cor[3]}[ {pos + 1} ]{cor[0]} - {cor[4]}{b.nome}{cor[0]}')
    while True:
        sel = leia_int('Selecione um banco: ')
        if sel == 1:
            return sel-1
        if sel == 2:
            return sel-1

def erro(txt):
    print(f'{cor[1]}{txt}{cor[0]}')


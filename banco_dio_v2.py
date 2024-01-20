import textwrap

def menuu():
    menu = '''\n
    ============== MENU ==============
        Menu Banco PY 'v2' (by: Rafael Guimarães)

    [1]\t Depósito;
    [2]\t Saque;
    [3]\t Extrato;
    [4]\t Novo Cliente;
    [5]\t Nova Conta;
    [6]\t Listar Contas;
    [9]\t Sair

    ===================================   
    ==> '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_deposito, extrato, /):
        if valor_deposito >0:
            saldo += valor_deposito
            extrato += (f' Depósito:\tR$ {valor_deposito:.2f} (+) \n ')
            print('\n Depósito bem sucedido!') 
        else:
            print(" O valor informado é inválido!")


        return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite_saque_por_operacao, quantid_saques_realizados, limite_saques_dia):
    excedeu_saldo = valor_saque>saldo
    excedeu_limite_por_operacao = valor_saque > limite_saque_por_operacao
    excedeu_saques = quantid_saques_realizados >= limite_saques_dia

    if excedeu_saldo:
        print('Operação fahou!\nVocê não tem saldo suficiente.')

    elif excedeu_limite_por_operacao:
        print(f'Operação fahou!\nO valor do saque excede o limite o seu limite.\nO seu limite de saque por operação é R${limite_saque_por_operacao:.2f}')
    
    elif excedeu_saques:
        print('Operação fahou!\nMúmero máximo de saques excedido.')
    
    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += (f' Saque:\tR$ {valor_saque:.2f} (-)\n ')
        quantid_saques_realizados += 1
        print(f'Saque bem sucedido!') 
    
    else:
        print("Operação fahou!\nValor informado é inválido.\n ")
    
    return saldo, extrato


def exibir_extrato(saldo, /,*, extrato):
    print("\n ================== Extrato ==================")
    print("\n Não foram realizadas movimentações anteriores." if not extrato else extrato )
    print(f" Saldo:\t  R$ {saldo:.2f}")
    print("================== Fim Extrato ==================")

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n Já existe usuário com esse CPF! ')
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, num - bairro - cidade/sigla estado):  ")

    usuarios.append({'nome':nome,
                     'data_nascimento':data_nascimento,
                     'cpf':cpf,
                     'enderco':endereco })
    print('Usuário criado com sucesso! ')

    '''
    Armazenar em lista
    nome
    data de nascimento
    CPF (SÓ NÚMEROS, OU SEJA, STRING)
    endereço (logradouro, num, bairro, cidade, sigla/Estado )
    NÃO PODEMOS CADASTRAR 2 USUÁRIOS COM O MESMO CPF

    '''


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do Usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('Conta criada com Sucesso!')
        return {'agencia': agencia,
                'numero_conta': numero_conta,
                'usuario': usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado! ")

'''
Agência (Fixo ==> 0001)
Número da conta (Sequancial iniciando em 1)
Usuário (Não teremos conta em conjunto)

'''

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência: \t {conta['agencia']}
            C/C: \t\t {conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}

     '''
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES_DIA = 3
    AGENCIA = '0001'

    saldo = 0
    limite_saque_por_operacao = 500
    extrato = ""
    quantid_saques_realizados = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menuu()

        if opcao == '1':
            valor_deposito = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao =='2':
            valor_saque = float(input('Informe o valor de saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite_saque_por_operacao=limite_saque_por_operacao,
                quantid_saques_realizados=quantid_saques_realizados,
                limite_saques_dia=LIMITE_SAQUES_DIA,
                )
            
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += +1

        elif opcao == '6':
            listar_contas(contas)
    
        elif opcao == '9':
            print("Processo finalizado!")
            break

        else:
            print("Operação inválida\nEscolha uma das opções do MENU")


main()





# Variáveis globais
usuarios = []
contas = []
contador_contas = 0

def novo_usuario():
    """Cria um novo usuário no sistema."""
    nome = input('Digite o nome do usuário: ')
    cpf = input('Digite o CPF do usuário (apenas números): ')
    usuario = {'nome': nome, 'cpf': cpf, 'contas': []}
    usuarios.append(usuario)
    print(f'Usuário {nome} criado com sucesso!')

def nova_conta():
    """Cria uma nova conta bancária e associa a um usuário existente."""
    global contador_contas
    cpf = input('Digite o CPF do usuário para associar à conta: ')
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    if usuario:
        numero_conta = f'{contador_contas + 1:04}'
        nova_conta = {'numero': numero_conta, 'saldo': 0, 'saques': 0, 'valor_depositos': []}
        contas.append(nova_conta)
        usuario['contas'].append(nova_conta)
        contador_contas += 1
        print(f'Conta número {numero_conta} criada e associada ao usuário {usuario["nome"]}.')
    else:
        print('Usuário não encontrado. Cadastre o usuário primeiro.')

def listar_contas():
    """Lista todas as contas no sistema."""
    print('\nListagem de Contas:')
    for conta in contas:
        print(f'Conta Número: {conta["numero"]}, Saldo: R${conta["saldo"]:.2f}, Saques Realizados: {conta["saques"]}')

def depositar(conta):
    """Realiza um depósito na conta especificada."""
    try:
        valor_deposito = float(input('Digite o valor que deseja depositar: '))
        if valor_deposito > 0:
            conta['saldo'] += valor_deposito
            conta['valor_depositos'].append(valor_deposito)
            print(f'Depósito de R${valor_deposito:.2f} realizado com sucesso na conta {conta["numero"]}!')
        else:
            print('ERRO: Valor de depósito deve ser positivo.')
    except ValueError:
        print('ERRO: Digite um valor numérico válido para o depósito.')

def sacar(conta):
    """Realiza um saque da conta especificada."""
    if conta['saques'] >= 3:
        print('LIMITE DE SAQUES EXCEDIDO.')
        return
    
    try:
        valor_saque = float(input('Digite o valor que deseja sacar: '))
        if 0 < valor_saque <= 500 and valor_saque <= conta['saldo']:
            conta['saldo'] -= valor_saque
            conta['saques'] += 1
            print(f'Saque de R${valor_saque:.2f} realizado com sucesso na conta {conta["numero"]}!')
        else:
            print('Valor inválido! O saque deve ser até R$500 e não maior que o saldo disponível.')
    except ValueError:
        print('ERRO: Digite um valor numérico válido para o saque.')

def ver_extrato(conta):
    """Exibe o extrato da conta especificada."""
    print(f'\nExtrato da Conta {conta["numero"]}:')
    print(f'Saldo: R${conta["saldo"]:.2f}')
    print(f'Depósitos: {conta["valor_depositos"]}')
    print(f'Saques Realizados: {conta["saques"]}')

def escolher_conta():
    """Permite que o usuário escolha uma conta existente."""
    listar_contas()
    numero_conta = input('Digite o número da conta que deseja acessar: ')
    conta = next((c for c in contas if c['numero'] == numero_conta), None)
    if conta:
        return conta
    else:
        print('Conta não encontrada.')
        return None

# Loop Principal
while True:
    print('\nBem-vindo ao Sistema Bancário!')
    print('1. Novo Usuário')
    print('2. Nova Conta')
    print('3. Listar Contas')
    print('4. Depositar')
    print('5. Sacar')
    print('6. Ver Extrato')
    print('7. Sair')

    try:
        ope = int(input(': '))
    except ValueError:
        print('Opção inválida! Tente novamente.')
        continue

    if ope == 1:
        novo_usuario()
    elif ope == 2:
        nova_conta()
    elif ope == 3:
        listar_contas()
    elif ope == 4:
        conta = escolher_conta()

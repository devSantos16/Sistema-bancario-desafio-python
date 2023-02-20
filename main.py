# Sistema bancario em python
loop: bool = True
opcao: int
valor_extrato: float = 0.00
tentativas_saque: int = 0

def depositar(valor):
    global valor_extrato
    valor_extrato += valor
    print("Deposito concluido com sucesso com sucesso!")
    mostrar_extrato()
def sacar(valor):
    global valor_extrato
    if(valor_extrato - valor <= 0):
        print("Você não pode sacar um valor menó do que seu saldo!")
    else:
        valor_extrato-=valor
        print("Saque realizado com sucesso!")
        mostrar_extrato()


def mostrar_extrato():
    global valor_extrato
    print("Valor do extrato: {extrato}".format(extrato=valor_extrato))


while(loop):
    print("""
    -------------- DIGITE A OPÇÃO DESEJADA --------------
    1 - Depositar
    2 - Sacar
    3 - Mostrar extrato
    0 - Sair
    """.strip())
    opcao: int = int(input("Digite a opção desejada: "))

    if(opcao == 1):
        valor:int = int(input("Digite o valor que deseja depositar: "))
        depositar(valor)
    elif(opcao == 2):
        if (tentativas_saque == 3):
            print("Você já sacou +3 vezes, não é possivel realizar a transação!")
        else:
            valor:int = int(input("Digite o valor que deseja sacar: "))
            sacar(valor)
            tentativas_saque += 1
    elif(opcao == 3):
        mostrar_extrato()
    elif(opcao == 0):
        break
    else:
        print("Opcao errada, tente novamente!")




menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    def menu ():
    menu = """ \n

    MENU
    [d]\ tDepositar
    [s]\ tSacar
    [e]\ tExtrato 
    [nc]\ tNova conta
    [lc]\ tListar contas 
    [nu]\ tNovo usuario
    [q]\ tSair    

    """
    return input (textwrap.dedent(menu))

    def menu ()
        
    def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"depósito \tR$ {valor : .2 f}\n"
        print ("Depósito realizado com sucesso!")
    else: 
        print ("Operacao falhou! O valor informado é inválido!")

    return saldo, extrato

    def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    def exibir_extrato (saldo, /, *, extrato):

    def criar_usuario (usuarios):

    def filtrar_usuarios (cpf, usuarios):

    def criar_conta (agencia, numero_conta, usuarios):

    def listar_contas (contas):

    def main ():

    main ()  
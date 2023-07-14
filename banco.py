# 1 usuario
# saque 
# valor int e positivo
# 3 saques por dia 
# 500 reais por saque
# exibir mensagem caso saldo = 0

# extrato
# saque - valor e tipo

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

    operacao = input(menu)

    if operacao == 'd':
        valor = float(input("Qual o valor do deposito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Valor depositado: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif operacao == 's':
        valor = float(input("Informe valor do saque: R$ "))

        verifica_saldo = valor > saldo
        verifica_limite_saque = LIMITE_SAQUES <= numero_saques
        verifica_valor_saque = valor > limite

        if verifica_saldo:
            print(f"Saldo insuficiente, seu saldo é: R$ {saldo}")
        elif verifica_limite_saque:
            print("Exedeu a quantidade de saque do dia")
        elif verifica_valor_saque:
            print("O valor do saque excede o limite")

        elif valor <= saldo:
            saldo -= valor
            print(saldo)
            extrato += f"Saque de: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif operacao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif operacao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        


    
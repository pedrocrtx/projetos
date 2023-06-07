menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        deposito = float(input("Qual o valor que deseja depositar? "))

        if deposito > 0:
            saldo =+ deposito
            extrato += f"Depósito: R$ {saldo:.2f}\n"
        else:
            print("[ERROR] O valor do depósito é inválido.")

    elif opcao == "2":
        print("Sacar")
        saque = int(input("Qual o valor que você desejada sacar? "))
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("[ERROR] Você não tem saldo suficiente.")

        elif excedeu_limite:
             print("[ERROR] O valor do saque excede o limite!")
            
        elif excedeu_saques:
            print("[ERROR] Número máximo de saques excedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saques: R$ {saque:.2f}\n"
            numero_saques += 1

        else: 
            print("[ERROR] O valor informado é inválido.")

    elif opcao == "3":
        print("Extrato")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "4":
        break

    else:
        print('[ERROR] Por favor, selecione novamente a operação desejada')
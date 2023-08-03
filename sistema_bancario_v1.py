saldo = 0
limite_diario = 500
saques_totais = escolha = 0
depositos = []
saques = []


while escolha != 4:

    escolha = int(input('''
                Qual operação deseja fazer ?
        1 - Depositar
        2 - Sacar
        3 - Extrato
        4 - Sair
                        
        Escolha: '''))

    if escolha == 1:
        print(f"Você escolheu depositar, seu saldo atual é: {saldo}")
        a = float(input(f"Qual valor deseja depositar?: "))

        if a < 0:
            print("\n por favor, digite um valor válido \n")

        else: 
            saldo = saldo + a
            depositos.append(a)
              
    elif escolha == 2:
        print(f"Você escolheu sacar, seu saldo atual é: {saldo}")
        b = float(input(f"Qual valor deseja sacar?: "))

        if b > 500:
            print('Valor acima do permitido')

        if saques_totais >= 3:
            print('Saques do dia acima do permitido')
            
        
        else:
            saldo = saldo - b
            saques.append(b)
            saques_totais = saques_totais + 1

    elif escolha == 3:
        print(f"Você escolheu olhar seu extato, seu saldo atual é: {saldo}")
        for i in depositos:
            print(f"Seus depósitos são R${i}")
        for x in saques:
            print(f"Seus saques são R${x}")


    elif escolha == 4:
        print(f"Saindo do sistema.")
        break

    else: 
        print('Escolha um valor válido')
        



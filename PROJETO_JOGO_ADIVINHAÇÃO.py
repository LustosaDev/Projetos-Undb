import random
def jogo ():
    numeros = []
    pontuacao = []
    print("Regras do jogo: O comando ira mostrar um numero e voce deve escolher!")
    for valores in range(1,5):
        numeros.append(valores)
        print(numeros)    
    for i in range(5):
        contador = i
        print("Chute um numero de 1 a 10!")
        premiado = random.choice(numeros)
        contador = 5 - i
        print("Voce tem {} tentativas!".format(contador))
        alternativa = int(input("Qual numero voce chuta: "))
        if contador == 1 and alternativa == premiado:
            random.choice(numeros)
            print("PARABENS, ACERTOU!")
            pontuacao.append(100)
            print("Sua pontuacao e: ",pontuacao)
            replay = str(input("Quer continuar?[SIM OU NAO]:  "))
            if replay == "SIM" or "sim":
                menu()
            elif replay == "NAO" or "nao":
                print("Saindo...")
                break
        elif contador == 4 and alternativa == premiado:
            print("ACERTOU DE SEGUNDA")
            pontuacao.append(50)
            print("Sua pontuacao e: ",pontuacao)
            replay = str(input("Quer continuar?[SIM OU NAO]:  "))
            if replay == "SIM" or "sim":
                menu()
            elif replay == "NAO" or "nao":
                print("Saindo...")
                break
        elif contador == 3 and alternativa == premiado:
            print("ACERTOU DE TERCEIRA")
            pontuacao.append(30)
            print("Sua pontuacao e: ",pontuacao)
            replay = str(input("Quer continuar?[SIM OU NAO]:  "))
            if replay == "SIM" or "sim":
                menu()
            elif replay == "NAO" or "nao":
                print("Saindo...")
                break
        elif contador == 2 and alternativa == premiado:
            print("ACERTOU DE QUARTA")
            pontuacao.append(10)
            print("Sua pontuacao e: ",pontuacao)
            replay = str(input("Quer continuar?[SIM OU NAO]:  "))
            if replay == "SIM" or "sim":
                menu()
            elif replay == "NAO" or "nao":
                print("Saindo...")
                break
        elif contador == 1 and alternativa != premiado:
            print("Todas as chances acabaram")
            return(jogo()) 
def menu ():
    print("-"*40)
    print("GAME DE ADIVINHAÇÃO")
    print("-"*40)
    print("Siga os comandos abaixo para inicio do game")
    print("INICIAR GAME = 1")
    print("SAIR DO GAME = 2")
    
    while True:
        
        opcao = int(input("DIGITE SUA OPÇÃO: "))
        if opcao == 1:
            print("Iniciar jogo...")
            jogo()
        elif opcao == 2:
            print("Saindo...")
            break
        else:
            print("Opção inválida ou desconhecida, retornando ao menu...")
            return(menu())
menu()

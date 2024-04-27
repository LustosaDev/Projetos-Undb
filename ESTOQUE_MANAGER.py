nomes_produtos = []
categorias = []
quantidade = []
porcentagem_geral = []

def login():
  print('FAÇA LOGIN PARA ACESSAR O GERENCIADOR DE ESTOQUES ')
  print('-'*40)
  usuario = str(input('Usuário: '))
  senha = str(input('Senha: '))
  print('-'*40)
  if usuario == 'admin' and senha == '@dmiN':
    print('Login efetuado com sucesso!')
    print('Abrindo gerenciador de estoques...')
    print('-'*40)
  else:
    print('Usuário/Senha inválido. Verifique se você digitou corretamente.')
    print('-'*40)
    return(login())

def show():
  print('Nomes dos produtos estocados:')
  print(nomes_produtos)
  print('-'*40)


def menu():
  while True:
    print('Seja bem-vindo ao Gerenciador de Estoque!')
    print('-'*40)
    print('1 - Adicionar produto')
    print('2 - Visualizar produtos estocados')
    print('3 - Mostrar quantidade de produtos estocados')
    print('4 - Visualizar porcentagem de produtos por categoria')
    print('5 - Sair')
    print('-'*40)

    opcao = int(input('O que desejas fazer? '))
    if opcao == 1:
      for i in range(3):
        nome = str(input('Digite o nome do produto que desejas estocar: '))
        nomes_produtos.append(nome)
        print('{} foi estocado com sucesso!'.format(nome))
        print('-'*40)
        print('Dentre as opções abaixo...')
        print('1 - ROUPAS')
        print('2 - CALÇADOS')
        print('3 - ACESSÓRIOS')
        print('4 - EQUIPAMENTOS')
        print('-'*40)

        tipo = int(input('Digite a qual categoria pertence o produto: '))
        if tipo == 1:
          tipo = 'ROUPAS'
          categorias.append(tipo)
        elif tipo == 2:
          tipo = 'CALÇADOS'
          categorias.append(tipo)
        elif tipo == 3:
          tipo = 'ACESSÓRIOS'
          categorias.append(tipo)
        elif tipo == 4:
          tipo = 'EQUIPAMENTOS'
          categorias.append(tipo) 

    
        print('Produto registrado como {}!'.format(tipo))
        pecas = int(input('Digite o número de {}(s) que será estocado (algarismo): '.format(nome)))
        quantidade.append(pecas)
        print('{} {}(s) adicionado ao estoque'.format(pecas, nome))
        print('-'*40)
      return(menu())


    elif opcao == 2:
        print('Nomes dos produtos estocados:')
        print(nomes_produtos)
        print('-'*40)
        return(menu())

    elif opcao == 3:
        print('Produtos estocados:')
        print(nomes_produtos)
        print('Quantidade de produtos estocados, respectivamente:')
        print(quantidade)
        print('-'*40)
        total_produtos = sum(quantidade)
        print('Portanto, o total de produtos estocados é igual a {} peças.'.format(total_produtos) )
        print('-'*40)
        return(menu())  
    
    elif opcao == 4:
        total_produtos = sum(quantidade)
        if total_produtos == 0:
          print('-'*40)
          print('Não há produtos estocados.')
          print('-'*40)
          return(menu())
        print("-"*40)
        if categorias[0] == categorias[1]:
          percent_0 = ((quantidade[0] + quantidade[1])/total_produtos)*100
          percent_2 = (quantidade[2]/total_produtos)*100
          print(f"{categorias[0]} corresponde a {percent_0: .2f}%, do total de produtos")
          print(f"{categorias[2]} corresponde a {percent_2: .2f}%, do total de produtos")
        elif categorias[0] == categorias[2]:
          percent_0 = ((quantidade[0] + quantidade[2])/total_produtos)*100
          percent_1 = (quantidade[1]/total_produtos)*100
          print(f"{categorias[0]} corresponde a {percent_0: .2f}%, do total de produtos")
          print(f"{categorias[1]} corresponde a {percent_1: .2f}%, do total de produtos")
        elif categorias[1] == categorias[2]:
          percent_1 = ((quantidade[1] + quantidade[2])/total_produtos)*100
          percent_0 = (quantidade[0]/total_produtos)*100
          print(f"{categorias[1]} corresponde a {percent_1: .2f}%, do total de produtos")
          print(f"{categorias[0]} corresponde a {percent_0: .2f}%, do total de produtos")
        else:
          percent_0 = (quantidade[0]/total_produtos)*100
          percent_1 = (quantidade[1]/total_produtos)*100
          percent_2 = (quantidade[2]/total_produtos)*100
          print(f"{categorias[0]} corresponde a {percent_0: .2f}%, do total de produtos")
          print(f"{categorias[1]} corresponde a {percent_1: .2f}%, do total de produtos")
          print(f"{categorias[2]} corresponde a {percent_2: .2f}%, do total de produtos")
        return(menu())
      
    elif opcao == 5:
        print('Finalizando o gerenciandor de produtos...')
    break

login()
menu()

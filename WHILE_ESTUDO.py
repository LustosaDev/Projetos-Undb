print("-"*30)
print("CADASTRO DE DADOS")
print("-"*30)
nome = str(input("Digite seu nome [mais 3]: "))
while len(nome) <= 3:
    nome = str(input("Errado, digite seu nome [mais 3]: "))\
        
idade = int(input("Digite sua idade [0 a 100]: "))

while idade <= 0 or idade >= 100:
    idade = int(input("Errado, Digite sua idade [0 a 100]: "))
    
salario = float(input("Digite seu salario [maior que 0]: "))
while salario < 0:
    salario = int(input("Errado, Digite seu salario [maior que 0]: "))
    
sexo = str(input("Qual seu sexo[usar `F` ou `M`]: "))
while sexo != "f" and sexo != "m":
    sexo = str(input("Errado, Qual seu sexo[usar `F` ou `M`]: "))

print("Dados cadastrados")

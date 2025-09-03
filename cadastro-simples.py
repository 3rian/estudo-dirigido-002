# Prática guiada (com expansão de diculdade)
#1. Cadastro simples
#Peça o nome e idade da pessoa e diga se ela pode entrar ou não:

#Expansão: Crie uma função pode_entrar(idade) que retorna True ou False.
#Expansão 2: Coloque dentro de um while que pergunta várias vezes até o usuário digitar sair

"""nome = input("Nome: ")
idade = int(input("Idade: "))
if idade >= 18:
 print(f"{nome}, você pode entrar.")
else:
 print(f"{nome}, você não pode entrar.")"""
 
def pode_entrar(idade):
    return idade >= 18

while True:
    nome = input("Digite seu nome: ")
    
    if nome.lower() == "sair":  # se o usuário digitar "sair", o loop para
        print("Programa encerrado.")
        break

    idade = int(input("Digite a idade:  (Digie sair para encerrar)"))

    if pode_entrar(idade):
        print(f"{nome}, você pode entrar.")
    else:
        print(f"{nome}, você não pode entrar.")
        
        



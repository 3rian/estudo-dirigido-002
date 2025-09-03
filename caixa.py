print("Bem vindo à nossa loja!!")

nome = input("Qual é o seu nome: ")
saldo = float(input("Quanto tem para gastar?: "))

# dicionário com produtos e preços
produtos = {
    "água": 2.50,
    "cerveja": 5.00,
    "refrigerante": 4.00
}

def exibir_menu():
    while True:
        print("\n[1] Consultar produtos disponíveis")
        print("[2] Comprar")
        print("[0] Sair")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            print("\nProdutos disponíveis:")
            for item, preco in produtos.items():
                print(f"- {item.capitalize()} → R$ {preco:.2f}")
        
        elif escolha == 2:
            comprar()
        
        elif escolha == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

def comprar():
    global saldo  # para atualizar o saldo do usuário
    
    print("\nEscolha um dos produtos:")
    for item, preco in produtos.items():
        print(f"- {item.capitalize()} → R$ {preco:.2f}")
    
    produto = input("Digite o nome do produto: ").lower()
    
    if produto not in produtos:
        print("Produto inválido!")
        return
    
    quantidade = int(input(f"Quantas unidades de {produto} você deseja comprar? "))
    total = produtos[produto] * quantidade
    
    if saldo >= total:
        saldo -= total
        print(f" Compra realizada! Você comprou {quantidade} {produto}(s) por R$ {total:.2f}.")
        print(f" Seu saldo agora é: R$ {saldo:.2f}")
    else:
        print(" Saldo insuficiente!")

# inicia o programa
exibir_menu()

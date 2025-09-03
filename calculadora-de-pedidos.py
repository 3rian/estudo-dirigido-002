#2. Calculadora de pedidos
#Crie um programa que simula pedidos em uma lanchonete. Só aceita:
#Cartão (se valor > 20),
#Pix (qualquer valor),
#Dinheiro (somente valor exato)
#Expansão: Transforme esse código em uma função verifica_pagamento(forma, valor) .
#Expansão 2: Crie um loop que peça 3 pedidos seguidos com for 

"""forma = input("Forma de pagamento: ").lower()
valor = float(input("Valor: "))
if forma == "cartao" and valor > 20:
print("Aceito!")
elif forma == "pix":
print("Aceito!")
elif forma == "dinheiro" and valor == 10:
print("Aceito!")
else:
print("Não aceito.")"""

def verifica_pagamento(forma, valor):
    if forma == "cartao" and valor > 20:
         return True
    elif forma == "pix":
         return True
    elif forma == "dinheiro":
     if valor.is_integer():
          return True
    else:
          return False


for i in range(1, 4):  # repete 3 vezes
    print(f"\nPedido {i}:")
    forma = input("Forma de pagamento (cartao/pix/dinheiro): ").lower()
    valor = float(input("Valor: "))

    if verifica_pagamento(forma, valor):
        print("Pagamento Aceito! ")
    else:
        print("Pagamento Não aceito ")


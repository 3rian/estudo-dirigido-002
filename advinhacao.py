def jogo_adivinha():
    segredo = 7
    chances = 0
    
    while True:
        chute = int(input("Adivinhe o número (0-10): "))
        chances += 1
        
        if chute == segredo:
            print(f"Você acertou em {chances} tentativa(s)!")
            break
        elif chute < segredo:
            print("Muito baixo!")
        else:
            print("Muito alto!")

# chama a função
jogo_adivinha()



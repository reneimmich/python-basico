# Jogo de Adivinhacao em Python
# Praticando: loops, condicionais e random

import random

def jogo_adivinhacao():
    print("=== Jogo de Adivinhacao ===")
    print("Tente adivinhar o numero entre 1 e 100!")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    
    while tentativas < max_tentativas:
        tentativas += 1
        print(f"\nTentativa {tentativas}/{max_tentativas}")
        
        try:
            chute = int(input("Seu chute: "))
        except ValueError:
            print("Digite apenas numeros inteiros!")
            tentativas -= 1
            continue
        
        if chute < 1 or chute > 100:
            print("O numero deve estar entre 1 e 100!")
            tentativas -= 1
            continue
        
        if chute == numero_secreto:
            print(f"\nParabens! Voce acertou em {tentativas} tentativa(s)!")
            if tentativas <= 3:
                print("Incrivel! Voce eh muito bom nisso!")
            elif tentativas <= 6:
                print("Bom trabalho!")
            else:
                print("Continue praticando!")
            return
        elif chute < numero_secreto:
            print("Muito baixo! Tente um numero maior.")
        else:
            print("Muito alto! Tente um numero menor.")
        
        dicas_restantes = max_tentativas - tentativas
        if dicas_restantes > 0:
            print(f"Voce tem {dicas_restantes} tentativa(s) restante(s).")
    
    print(f"\nGame over! O numero era {numero_secreto}.")
    print("Tente novamente!")

def main():
    while True:
        jogo_adivinhacao()
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Ate a proxima!")
            break

if __name__ == "__main__":
    main()

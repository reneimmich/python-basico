# Calculadora simples em Python
# Aprendendo operacoes basicas

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero!"
    return a / b

def calculadora():
    print("=== Calculadora Python ===")
    print("Operacoes: + soma | - subtracao | * multiplicacao | / divisao")
    
    while True:
        print("\n1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opcao: ")
        
        if opcao == "0":
            print("Encerrando calculadora. Ate logo!")
            break
        
        if opcao not in ["1", "2", "3", "4"]:
            print("Opcao invalida! Tente novamente.")
            continue
        
        a = float(input("Digite o primeiro numero: "))
        b = float(input("Digite o segundo numero: "))
        
        if opcao == "1":
            print(f"Resultado: {a} + {b} = {somar(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {a} - {b} = {subtrair(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {a} * {b} = {multiplicar(a, b)}")
        elif opcao == "4":
            print(f"Resultado: {a} / {b} = {dividir(a, b)}")

if __name__ == "__main__":
    calculadora()

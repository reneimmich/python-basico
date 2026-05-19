# Conversor de Temperatura
# Converte entre Celsius, Fahrenheit e Kelvin

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return fahrenheit_para_celsius(f) + 273.15

def kelvin_para_celsius(k):
    if k < 0:
        raise ValueError("Kelvin nao pode ser negativo!")
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return celsius_para_fahrenheit(kelvin_para_celsius(k))

def exibir_menu():
    print("\n=== Conversor de Temperatura ===")
    print("1 - Celsius para Fahrenheit e Kelvin")
    print("2 - Fahrenheit para Celsius e Kelvin")
    print("3 - Kelvin para Celsius e Fahrenheit")
    print("0 - Sair")

def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha: ")

        if opcao == "0":
            print("Encerrando. Ate logo!")
            break

        try:
            if opcao == "1":
                c = float(input("Digite a temperatura em Celsius: "))
                print(f"  {c}°C = {celsius_para_fahrenheit(c):.2f}°F")
                print(f"  {c}°C = {celsius_para_kelvin(c):.2f} K")

            elif opcao == "2":
                f = float(input("Digite a temperatura em Fahrenheit: "))
                print(f"  {f}°F = {fahrenheit_para_celsius(f):.2f}°C")
                print(f"  {f}°F = {fahrenheit_para_kelvin(f):.2f} K")

            elif opcao == "3":
                k = float(input("Digite a temperatura em Kelvin: "))
                print(f"  {k} K = {kelvin_para_celsius(k):.2f}°C")
                print(f"  {k} K = {kelvin_para_fahrenheit(k):.2f}°F")

            else:
                print("Opcao invalida!")

        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()

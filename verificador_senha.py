# Verificador e Gerador de Senhas
# Nivel medio: regex, string methods, random

import re
import random
import string

def verificar_forca(senha):
    """Verifica a forca de uma senha e retorna nivel e dicas."""
    pontos = 0
    dicas = []

    if len(senha) >= 8:
        pontos += 1
    else:
        dicas.append("Use pelo menos 8 caracteres")

    if len(senha) >= 12:
        pontos += 1

    if re.search(r'[A-Z]', senha):
        pontos += 1
    else:
        dicas.append("Adicione letras maiusculas")

    if re.search(r'[a-z]', senha):
        pontos += 1
    else:
        dicas.append("Adicione letras minusculas")

    if re.search(r'[0-9]', senha):
        pontos += 1
    else:
        dicas.append("Adicione numeros")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        pontos += 1
    else:
        dicas.append("Adicione caracteres especiais (!@#$...)")

    if pontos <= 2:
        nivel = "FRACA"
    elif pontos <= 4:
        nivel = "MEDIA"
    elif pontos <= 5:
        nivel = "FORTE"
    else:
        nivel = "MUITO FORTE"

    return nivel, pontos, dicas

def gerar_senha(tamanho=12, usar_especiais=True):
    """Gera uma senha aleatoria segura."""
    caracteres = string.ascii_letters + string.digits
    if usar_especiais:
        caracteres += "!@#$%&*"

    # Garante pelo menos um de cada tipo
    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
    ]
    if usar_especiais:
        senha.append(random.choice("!@#$%&*"))

    # Completa o restante
    for _ in range(tamanho - len(senha)):
        senha.append(random.choice(caracteres))

    random.shuffle(senha)
    return "".join(senha)

def exibir_resultado(senha, nivel, pontos, dicas):
    print(f"\nSenha: {senha}")
    print(f"Forca: {nivel} ({pontos}/6 pontos)")
    if dicas:
        print("Dicas para melhorar:")
        for d in dicas:
            print(f"  - {d}")
    else:
        print("Senha excelente!")

def main():
    print("=== Verificador e Gerador de Senhas ===")
    while True:
        print("\n1 - Verificar uma senha")
        print("2 - Gerar senha segura")
        print("0 - Sair")
        opcao = input("Opcao: ")

        if opcao == "0":
            break
        elif opcao == "1":
            senha = input("Digite a senha: ")
            nivel, pontos, dicas = verificar_forca(senha)
            exibir_resultado(senha, nivel, pontos, dicas)
        elif opcao == "2":
            try:
                tam = int(input("Tamanho da senha (padrao 12): ") or "12")
                especiais = input("Usar caracteres especiais? (s/n): ").lower() == "s"
                senha = gerar_senha(tam, especiais)
                nivel, pontos, dicas = verificar_forca(senha)
                print(f"\nSenha gerada: {senha}")
                print(f"Forca: {nivel}")
            except ValueError:
                print("Tamanho invalido!")

if __name__ == "__main__":
    main()

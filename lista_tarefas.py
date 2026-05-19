# Lista de Tarefas (To-Do List)
# Praticando: listas, dicionarios, arquivos e funcoes

import json
import os
from datetime import datetime

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def adicionar_tarefa(tarefas, titulo):
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False,
        "criada_em": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n=== Suas Tarefas ===")
    for t in tarefas:
        status = "V" if t["concluida"] else "O"
        print(f"[{status}] #{t['id']} - {t['titulo']} ({t['criada_em']})")

def concluir_tarefa(tarefas, id_tarefa):
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"Tarefa #{id_tarefa} concluida!")
            return
    print(f"Tarefa #{id_tarefa} nao encontrada.")

def remover_tarefa(tarefas, id_tarefa):
    for i, t in enumerate(tarefas):
        if t["id"] == id_tarefa:
            removida = tarefas.pop(i)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida['titulo']}' removida!")
            return
    print(f"Tarefa #{id_tarefa} nao encontrada.")

def main():
    tarefas = carregar_tarefas()
    while True:
        print("\n1-Adicionar  2-Listar  3-Concluir  4-Remover  0-Sair")
        opcao = input("Opcao: ")
        if opcao == "0":
            break
        elif opcao == "1":
            titulo = input("Nome da tarefa: ").strip()
            if titulo:
                adicionar_tarefa(tarefas, titulo)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            listar_tarefas(tarefas)
            id_t = int(input("ID: "))
            concluir_tarefa(tarefas, id_t)
        elif opcao == "4":
            listar_tarefas(tarefas)
            id_t = int(input("ID: "))
            remover_tarefa(tarefas, id_t)

if __name__ == "__main__":
    main()

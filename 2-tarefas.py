''' Essa aplicação organiza as tarefas do usuário, ela possui as seguintes funcionalidades:
    1. Salvar tarefas
    2. Adicionar tarefa
    3. Concluir tarefa
    4. Listar tarefas
    5. Sair
'''
import json
from datetime import datetime

ARQUIVO = "tarefas.json"

tarefas = []

def carregar():
    # Retorna a lista de tarefas
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)           
    except:
        return []

def salvar():
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f)

def adicionar():
    # Tarefa
    # chaves: descricao, criacao, status
    tarefas.append({
            "descricao": input("Digite a nova tarefa: "),
            "criacao": datetime.now().strftime("%Y.%m.%d %H:%M"),
            "status": "criada"
            })

def concluir():
    if not tarefas:
        print("Não há tarefas a serem removidas.")
    else:
        tarefa_a_apagar = input("Digite o número da tarefa a ser removida: ")
        if tarefa_a_apagar.isdigit() and tarefa_a_apagar <= str(len(tarefas)):
            tarefas[int(tarefa_a_apagar) - 1]["status"] = "feita" 

def listar():
    if not tarefas:
        print("Não há tarefas a serem listadas.")   
    else:
        tarefas_inconclusas = [tarefa for tarefa in tarefas if tarefa["status"] == "criada"]
        for (i, tarefa) in enumerate(tarefas_inconclusas):
            print(f"{i + 1}. {tarefa}")

def main():
    print("Bem vindo ao Gerenciador de Tarefas")
    tarefas = carregar()

    while True:
        print("\nMenu: \n1. Salvar arquivo\n2. Adicionar tarefa\n3. Remover tarefa\n4. Listar tarefas\n5. Sair\n")
        escolha = input("Digite uma opção: ")

        if escolha == "1": salvar()
        elif escolha == "2": adicionar()
        elif escolha == "3": concluir()
        elif escolha == "4": listar()
        elif escolha == "5": break
        else: print("Escolha inexistente.\n")

if __name__ == "__main__":
    main()
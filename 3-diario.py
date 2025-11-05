# diario_pessoal.py
import json
from datetime import datetime

ARQUIVO = "diario.json"

# -----------------------------
# Funções de persistência
# -----------------------------
def carregar():
    """Carrega o diário do arquivo JSON ou retorna lista vazia se não existir."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Arquivo corrompido. Iniciando diário vazio.")
        return []

def salvar(diario):
    """Salva a lista de entradas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(diario, f, ensure_ascii=False, indent=2)

# -----------------------------
# Funções de operações
# -----------------------------
def adicionar_entrada(diario):
    """Adiciona uma nova entrada ao diário."""
    texto = input("Digite sua entrada: ").strip()
    if texto:
        entrada = {
            "texto": texto,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        diario.append(entrada)
        salvar(diario)
        print("Entrada adicionada com sucesso!")
    else:
        print("Entrada vazia não foi adicionada.")

def listar_entradas(diario):
    """Mostra todas as entradas do diário."""
    if not diario:
        print("(Nenhuma entrada cadastrada)")
        return
    print("\n=== Diário Pessoal ===")
    for i, entrada in enumerate(diario, start=1):
        print(f"{i}. [{entrada['data']}] {entrada['texto']}")

def buscar_entradas(diario):
    """Busca entradas por palavra-chave."""
    if not diario:
        print("(Nenhuma entrada cadastrada)")
        return
    palavra = input("Digite a palavra-chave para busca: ").strip().lower()
    resultados = [e for e in diario if palavra in e["texto"].lower()]
    if resultados:
        print(f"\n=== Entradas que contém '{palavra}' ===")
        for e in resultados:
            print(f"[{e['data']}] {e['texto']}")
    else:
        print("Nenhuma entrada encontrada com essa palavra.")

# -----------------------------
# Função principal
# -----------------------------
def main():
    diario = carregar()
    print("=== Bem-vindo ao Diário Pessoal ===")
    while True:
        print("\nMenu:")
        print("1 - Adicionar entrada")
        print("2 - Listar entradas")
        print("3 - Buscar entradas")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            adicionar_entrada(diario)
        elif escolha == "2":
            listar_entradas(diario)
        elif escolha == "3":
            buscar_entradas(diario)
        elif escolha == "4":
            print("Saindo do diário. Até logo!")
            break
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()

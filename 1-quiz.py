'''
Quiz Interativo
Itera por 4 perguntas, recebendo a resposta do usuário e, ao final, apresenta o resultado.
'''

print("Quiz Interativo")
nome = input("Qual seu nome? ")

combo_qa = [
    ("Quanto é 2 + 2?", "4"),
    ("Qual a capital da França?", "paris"),
    ("Qual o maior planeta do sistema solar?", "júpiter"), 
    ("Qual linguagem estamos aprendendo?", "python")
]

pontos = 0
total_perguntas = len(combo_qa)

while pontos < total_perguntas:
    print(f"Seja bem vindo {nome}, novo jogo!")
    pontos = 0
    for (pergunta, resposta) in combo_qa:
        if resposta == input(pergunta).lower().strip():
            pontos += 1
    pontos_feitos = pontos / total_perguntas * 100
    print(f"Você fez {pontos_feitos} pontos.")

print("Você acertou tudo!")
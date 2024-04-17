from typing import Dict, List
def adicionar_contato(contatos: list, nome: str, telefone: any, email: str) -> Dict:
    contato = {"nome": nome,
               "telefone": telefone,
               "email": email,
               "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return
def ver_contatos(contatos: list) -> List:
    return

contatos = []

while True:
    print("\nMenu de Agenda de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver lista de Contatos")
    print("3. Atualizar Contatos")
    print("4. Favoritar/Desfavoritar Contato")
    print("5. Lista de Contatos Favoritos")
    print("6. Deletar Contato da Agenda")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do seu contato: ")
        telefone = input("Digite o numero do seu contato: ")
        email = input("Digite o email do seu contato: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == "7":
        break

print("Programa finalizado!")
    
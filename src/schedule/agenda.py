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
    for indice, contato in enumerate(contatos, start=1):
        favorito = "☆" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}.[{favorito}] Nome: {nome} || Telefone: {telefone} || Email: {email}")   
    return
def update_nome(contatos: list, indice_contato: int, novo_nome_contato: str) -> Dict:
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
    print(f"Contato {indice_contato} atualizado para {novo_nome_contato}")
    if dado_alterado == "nome":
        return update_nome
    else:
        return "Você pode alterar apenas esses dados: Nome, Telefone e Email!"

def update_telefone(contatos: list, indice_contato: int, novo_telefone_contato: any) -> Dict:
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
    print(f"Telefone do contato {indice_contato} atualizado para {novo_telefone_contato}")
    if dado_alterado == "telefone":
        return update_telefone
    else:
        return "Você pode alterar apenas esses dados: Nome, Telefone e Email!"

def update_email(contatos: list, indice_contato: int, novo_email_contato: str) -> Dict:
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["email"] = novo_email_contato
    print(f"Email do contato {indice_contato} atualizado para {novo_email_contato}")
    if dado_alterado == "email":
        return update_email
    else:
        return "Você pode alterar apenas esses dados: Nome, Telefone e Email!"

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
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ")
        dado_alterado = input("Deseja alterar qual dado do contato? ")
        if dado_alterado == "nome":
            novo_nome = input("Digite o novo nome do contato: ")
            update_nome(contatos, indice_contato, novo_nome)
        elif dado_alterado == "telefone":
            novo_telefone = input("Digite o novo numero do contato: ")
            update_telefone(contatos, indice_contato, novo_telefone)
        elif dado_alterado == "email":
            novo_email = input("Digite o novo email do contato: ")
            update_email(contatos, indice_contato, novo_email)
        else:
            print("Você pode alterar apenas esses dados: Nome, Telefone e Email!")
    elif escolha == "7":
        break

print("Programa finalizado!")
    
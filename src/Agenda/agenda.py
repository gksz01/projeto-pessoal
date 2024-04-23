from typing import Dict, List

# Function: Create Contact
def adicionar_contato(contatos: list, nome: str, telefone: any, email: str) -> Dict:
    contato = {"nome": nome,
               "telefone": telefone,
               "email": email,
               "favorito": False}
    contatos.append(contato)
    print(f"\nContato {nome} adicionado com sucesso!")
    return

# Function: View Contact
def ver_contatos(contatos: list) -> List:
    for indice, contato in enumerate(contatos, start=1):
        favorito = "♥" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}.[{favorito}] Nome: {nome} || Telefone: {telefone} || Email: {email}")   
    return

# Function: Update Contact Name
def update_nome(contatos: list, indice_contato: int, novo_nome_contato: str) -> str:
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["nome"] = novo_nome_contato
        print(f"\nContato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("Indice da tarefa não corresonde com as existentes!")

# Function: Update Contact Number
def update_telefone(contatos: list, indice_contato: int, novo_telefone_contato: any) -> any:
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["telefone"] = novo_telefone_contato
        print(f"\nTelefone do contato {indice_contato} atualizado para {novo_telefone_contato}")
    else:
        print("Indice da tarefa não corresonde com as existentes!")

# Function: Update Contact Email
def update_email(contatos: list, indice_contato: int, novo_email_contato: str) -> str:
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["email"] = novo_email_contato
        print(f"\nEmail do contato {indice_contato} atualizado para {novo_email_contato}")
    else:
        print("Indice da tarefa não corresonde com as existentes!")
 
# Function: Favorite the Contact 
def favoritar_contato(contatos: list, indice_contato: int) -> str:
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["favorito"] = True
    print(f"\nContato {indice_contato} adicionado aos Favoritos!")

# Function: Unfavorite the Contact 
def desfavoritar_contato(contatos: list, indice_contato: int) -> str:
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["favorito"] = False
    print(f"\nContato {indice_contato} removido dos Favoritos!")

# Function: View Favorite Contacts   
def ver_favoritos(contatos: list) -> list:
    print("Contatos Favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"\n{indice}. Nome: {nome} || Telefone: {telefone} || Email: {email}")
    return

# Function: Remove Contact
def remover_contato(contatos: list, indice_contato: int) -> None: 
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        del contatos[indice_ajustado]
        print(f"\nContato {indice_contato} foi removido da sua agenda!")
    else:
        print("O contato que você escolheu não existe")
    return

# Contacts List variable
contatos = []

# Looping Menu Interaction 
while True:
    print("\nMenu de Agenda de Contatos:") # Contact Agenda Menu
    print("1. Adicionar Contato") # Add Contact
    print("2. Ver lista de Contatos") # View Contacts
    print("3. Atualizar Contatos") # Update Contact
    print("4. Favoritar/Desfavoritar Contato") # Favorite/Unfavorite Contact
    print("5. Lista de Contatos Favoritos") # View Favorite Contacts
    print("6. Deletar Contato da Agenda") # Remove Contact
    print("7. Sair") # Exit

# User Option variable (1, 2, 3, 4, 5, 6, 7)
    escolha = input("Digite sua escolha: ") 

    # Option 1.
    if escolha == "1":
        nome = input("Digite o nome do seu contato: ") # Write the contact name
        telefone = input("Digite o numero do seu contato: ") # Write the contact number
        email = input("Digite o email do seu contato: ") # Write the contact email
        adicionar_contato(contatos, nome, telefone, email)
    # Option 2.
    elif escolha == "2": # List of Contacts
        ver_contatos(contatos) 
    # Option 3.
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja atualizar: ") # Write the index number to update the contact
        dado_alterado = input("Deseja alterar qual dado do contato? ").lower() # Choose wich data you wanna update (Nome, Telefone, Email) respectively = (Name, Phone number, Email)
        # Condition to update only the contact name
        if dado_alterado == "nome":
            novo_nome = input("Digite o novo nome do contato: ") # Write the new contact name
            update_nome(contatos, indice_contato, novo_nome)
        # Condition to update only the contact number
        elif dado_alterado == "telefone":
            novo_telefone = input("Digite o novo numero do contato: ") # Write the new contact number
            update_telefone(contatos, indice_contato, novo_telefone)
        # Condition to update only the contact email
        elif dado_alterado == "email":
            novo_email = input("Digite o novo email do contato: ") # Write the new contact email
            update_email(contatos, indice_contato, novo_email)
        else:
            print("Você pode alterar apenas esses dados: Nome, Telefone e Email!") # (You can only update these datas: Name, Phone number, Email)
    # Option 4.
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite qual contato deseja favoritar ou desfavoritar: ") # Write the index number to Favorite or Unfavorite the contact
        favoritar = input("Deseja adicionar ou remover este contato dos favoritos? ").lower() # Asks if you wanna Add or remove the contact from Favorites
        # Condition to ask if the user want to Favorite the Contact
        if favoritar == "adicionar": # keyword add
            favoritar_contato(contatos, indice_contato)
        # Condition to ask if the user want to Unfavorite the Contact
        elif favoritar == "remover": # keyword remove
            desfavoritar_contato(contatos, indice_contato)
        else:
            print("Digite (adicionar) ou (remover) para prosseguir!") # (You can only type (adicionar = add) or (remover = remove) to proceed)
    # Option 5.
    elif escolha == "5":
        ver_favoritos(contatos) # List of Favorite Contacts
    # Option 6.
    elif escolha == "6":
        ver_contatos(contatos) 
        indice_contato = input("Digite qual contato deseja remover: ").lower() # Write the index number of wich contact you wanna remove
        remover_contato(contatos, indice_contato)
    # Option 7.
    elif escolha == "7": # Break the while loop and end the program
        break

print("Programa finalizado!")

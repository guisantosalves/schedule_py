import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


mylist = []
verify = True
contador = 0

while verify:
    value = int(input(" 1 - incluir\n 2 - alterar \n 3 - excluir\n 4 - pesquisar\n"))

    if value == 1:
        name = input("Digite o nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        newList = [name, telefone, email]
        mylist.append(newList)

    if value == 2:
        while contador < len(mylist):
            print(f"{contador} : {mylist[contador]}")
            contador = contador + 1
        a = int(input("Qual deseja alterar ?"))
        name = input("Digite o nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        newList = [name, telefone, email]
        mylist[a] = newList

    if value == 3:
        contador = 0
        while contador < len(mylist):
            print(f"{contador} : {mylist[contador]}")
            contador = contador + 1
        b = int(input("Qual deseja excluir (passe o num)?"))
        del mylist[b]

    if value == 4:
        for x in mylist:
            print(x)

    
    option = input("Deseja continuar S/N")
    if option == 's':
        verify = True
        clearConsole()
    elif option == 'n':
        verify = False
    else: 
        verify = False
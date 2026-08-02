from ListaDuplamenteEncadeada import ListaDuplamenteEncadeada

lista = ListaDuplamenteEncadeada()


def menu():
    print("=== MENU LISTA DUPLAMENTE ENCADEADA ===")
    print("1. Inserir elemento no início")
    print("2. Inserir elemento no fim (Recursivo)")
    print("3. Inserir elemento no meio (por índice - Recursivo)")
    print("4. Remover todas as ocorrências de um valor (Recursivo)")
    print("5. Ordenar a lista com Insertion Sort (Recursivo)")
    print("6. Exibir lista")
    print("0. Sair")
    opcao = ""
    while (opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4"
           and opcao != "5" and opcao != "6" and opcao != "0"):
        opcao = input("Digite sua opção: ")
    print("\n")

    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
        while True:
            try:
                valor = int(input("Insira um valor: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número inteiro.")
        if opcao == "3":
            while True:
                try:
                    indice = int(input("Digite o índice: "))
                    break
                except ValueError:
                    print("índice inválido. Digite um número inteiro.")

    if opcao == "1":
        lista.inserir_no_inicio(valor)
        menu()
    elif opcao == "2":
        lista.inserir_no_fim(valor)
        menu()
    elif opcao == "3":
        lista.inserir_no_meio(valor, indice)
        menu()
    elif opcao == "4":
        lista.remover_todos(valor)
        menu()
    elif opcao == "5":
        lista.ordenar()
        menu()
    elif opcao == "6":
        print(lista.exibir_lista())
        menu()
    else:
        print("Programa encerrado. Saindo...")


menu()

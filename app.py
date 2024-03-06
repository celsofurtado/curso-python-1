import os

restaurantes = [
    {
        "nome": "Restaurante 1",
        "categoria": "Mineira",
        "ativo": False
    },
    {
        "nome": "Restaurante 2",
        "categoria": "Japonesa",
        "ativo": True
    },
{
        "nome": "Restaurante 3",
        "categoria": "Bahiana",
        "ativo": True
    },
]


def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo("controle de estoque encerrado.")


def opcao_invalida():
    print("Opção inválida!")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system("cls")
    print("-----------------------------------------")
    print(texto.upper())
    print("-----------------------------------------")
    print()


def voltar_ao_menu_principal():
    input("\nPressione <Enter> para voltar ao menu principal...")
    main()


def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastro de restaurante")

    nome_do_restaurante = input("Nome do restaurante: ")
    categoria = input("Categoria do restaurante: ")

    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False
    }

    restaurantes.append(dados_do_restaurante)

    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("listar restaurantes")

    print(f"Total de restaurantes: {len(restaurantes)}\n")

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"|{nome_restaurante:<45}{categoria:<25}{ativo:<10}|")
        print("----------------------------------------------------------------------------------")

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as e:
        print(e)
        opcao_invalida()


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()

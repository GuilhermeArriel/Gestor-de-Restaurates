import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Massas', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


def exibir_sistema():
    '''Essa função é responsável por exibir a logo do sistema'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_opcoes():
    '''Essa função é responsável por exibir as opções do sistema'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar():
    '''Essa função é responsável por finalizar o sistema'''
    limpar_tela()
    exibir_subtitulo('Encerrando o sistema')


def opcao_invalida():
    '''Essa função é responsável por dar uma resposta ao usuário caso ele fornecesse uma informação incorreta'''
    limpar_tela()
    print('Opção inválida\n')
    voltar_menu()


def cad_rest():
    '''Essa função é responsável por realizar o cadastro de um novo de restaurante'''
    limpar_tela()
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_rest = input('Digite o nome do restaurante: ')
    categoria = input(
        f'Digite o nome da categoria do restaurante {nome_rest}: ')
    dados_do_restaurante = {'nome': nome_rest,
                            'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O Restaurante {nome_rest} foi cadastrado com sucesso!')
    voltar_menu()


def listar_rest():
    '''Essa função é responsável por listar todos os restaurantes criados'''
    limpar_tela()
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {
          'Categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)
                   } | {categoria.ljust(20)} | {ativo}')

    voltar_menu()


def alternar_status_restaurante():
    '''Essa função é responsável por alternar o estado do restaurante'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu()


def escolher_opcao():
    '''Essa função é responsável por designar uma função para a respectiva resposta do usuário'''
    try:
        resp = int(input('Escolha uma opção: \n'))
        print(f'Você escolheu a opção: {resp}')

        if resp == 1:
            cad_rest()
        elif resp == 2:
            listar_rest()
        elif resp == 3:
            alternar_status_restaurante()
        elif resp == 4:
            finalizar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo de cada menu com o caracter * aconhado pela quantidade de letras'''
    limpar_tela()
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def main():
    '''Essa função é responsável por exibir o menu'''
    os.system('cls')
    exibir_sistema()
    exibir_opcoes()
    escolher_opcao()


def voltar_menu():
    '''Essa função é responsável por exibir o menu novamente após o usuário digitar uma tecla'''
    input('Digite uma tecla para voltar ao menu principal\n')
    main()


def limpar_tela():
    '''Essa função é responsável por limpar a tela do console'''
    os.system('cls')


if __name__ == '__main__':
    '''Essa função é responsável por definir essa classe como principal'''
    main()

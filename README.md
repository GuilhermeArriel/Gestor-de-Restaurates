# Sistema de Gerenciamento de Restaurantes

Um sistema simples desenvolvido em Python para gerenciar restaurantes. Ele permite o cadastro, listagem e alteração do status de restaurantes de forma intuitiva no terminal.

---

## Funcionalidades

- **Cadastrar Restaurante**:  
  Permite registrar novos restaurantes, informando o nome e a categoria. O status inicial do restaurante será "desativado".

- **Listar Restaurantes**:  
  Exibe todos os restaurantes cadastrados em uma tabela organizada com nome, categoria e status (ativo ou desativado).

- **Alterar Status do Restaurante**:  
  Permite ativar ou desativar um restaurante, alternando o estado atual.

- **Sair do Sistema**:  
  Opção para encerrar o sistema de forma organizada.

---

## Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado.

### Passo a Passo
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-restaurantes.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd gerenciador-restaurantes
   ```

3. Execute o arquivo principal:
   ```bash
   python main.py
   ```

---

## Exemplo de Uso

### Menu Principal:
```plaintext
1. Cadastrar restaurante
2. Listar restaurantes
3. Alternar estado do restaurante
4. Sair
```

### Cadastro de Restaurante:
```plaintext
Digite o nome do restaurante: Cantina do Chef
Digite o nome da categoria do restaurante Cantina do Chef: Italiana
O Restaurante Cantina do Chef foi cadastrado com sucesso!
```

### Listagem de Restaurantes:
```plaintext
Nome do restaurante    | Categoria            | Status
- Praça                | Japonesa            | desativado
- Pizza Suprema        | Massas              | ativo
- Cantina              | Italiana            | desativado
```

---

## Estrutura do Código

- **`main.py`**: Contém todas as funções e a lógica do sistema:
  - **Funções Principais**:
    - `cad_rest`: Cadastrar novos restaurantes.
    - `listar_rest`: Listar os restaurantes cadastrados.
    - `alternar_status_restaurante`: Alternar o status de ativo/inativo de um restaurante.
  - **Funções Auxiliares**:
    - `limpar_tela`: Limpa a tela do terminal.
    - `voltar_menu`: Exibe o menu principal novamente após a interação.
    - `escolher_opcao`: Controla a navegação entre as opções do menu.
    - `finalizar`: Finaliza o sistema de forma organizada.

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Módulos**: Apenas o módulo padrão `os` para limpar a tela.

---

## Objetivos e Aprendizados

Este projeto foi desenvolvido com o intuito de praticar conceitos fundamentais de programação, incluindo:
- Estruturas condicionais e de repetição.
- Manipulação de listas e dicionários.
- Modularização de código e funções.
- Boas práticas no desenvolvimento de sistemas.

---

## Contribuições

Contribuições são bem-vindas! Caso tenha sugestões de melhorias ou novas funcionalidades, abra uma _issue_ ou envie um _pull request_.

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

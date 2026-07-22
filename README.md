# Base de Clientes em Python

## Ideia central do projeto

Este projeto é uma aplicação simples em Python para cadastro e consulta de clientes em uma base local, utilizando o SQLite como banco de dados.

A proposta inicial era criar um pequeno sistema terminal para registrar clientes, armazenar informações básicas como nome, CPF e CNPJ, e permitir consultas por ID, CPF ou CNPJ.

O projeto representa uma atividade prática de estudo, no contexto da DIO, onde o objetivo é aplicar conceitos de programação em Python, manipulação de banco de dados e melhoria de código com apoio de ferramentas de inteligência artificial, como o GitHub Copilot.

## Contexto da atividade

Essa atividade faz parte de um exercício de desenvolvimento orientado, em que um projeto já existente foi revisitado e aprimorado com o uso do Copilot.

A ideia foi:

- entender a estrutura inicial do código;
- identificar pontos frágeis, como entradas inválidas, falta de validação e organização limitada;
- melhorar a experiência do usuário;
- deixar o sistema mais seguro, legível e preparado para manutenção.

Assim, o projeto passou de uma versão funcional básica para uma versão mais organizada, robusta e profissional.

## O que foi alterado

A seguir, estão os principais pontos de melhoria implementados:

### 1. Estrutura do código mais organizada

O código foi reorganizado em funções e uma classe dedicada para o acesso ao banco de dados.

Isso trouxe:

- maior clareza no fluxo do programa;
- melhor manutenção futura;
- separação entre interface, regras de negócio e acesso ao banco.

### 2. Validação de entradas

Foram adicionadas validações para evitar que o programa quebre ao receber entradas inesperadas.

Exemplos:

- o usuário não precisa digitar valores inválidos para números;
- entradas vazias são bloqueadas;
- respostas de confirmação recebem tratamento melhorado.

### 3. Validação de CPF e CNPJ

Antes, o sistema aceitava qualquer valor digitado para CPF e CNPJ. Agora, a aplicação verifica se:

- o CPF possui 11 dígitos numéricos;
- o CNPJ possui 14 dígitos numéricos;
- o valor informado tem o formato esperado.

Isso aumenta a confiabilidade dos dados cadastrados.

### 4. Melhor tratamento de erros

O código passou a lidar com situações como:

- tentativa de cadastro duplicado;
- uso de dados inconsistentes;
- problemas de execução mais previsíveis.

### 5. Melhor experiência no terminal

O menu foi refinado para ficar mais intuitivo, com mensagens mais claras e fluxo mais simples para:

- cadastrar cliente;
- buscar cliente;
- listar clientes;
- sair do sistema.

### 6. Uso de SQLite de forma mais estruturada

A conexão com o banco foi encapsulada em uma classe, tornando o código mais limpo e organizado.

Isso facilita futuras alterações, como:

- incluir novos campos;
- criar funções de atualização e exclusão;
- evoluir a aplicação para um sistema maior.

## Funcionalidades atuais

O sistema permite:

- cadastrar clientes do tipo PF ou PJ;
- salvar nome, CPF ou CNPJ no banco;
- buscar clientes por ID, CPF ou CNPJ;
- listar todos os clientes cadastrados.

## Como executar

1. Certifique-se de ter o Python instalado.
2. Execute o arquivo principal:

```bash
python cliente_otimizado.py
```

3. O programa criará automaticamente o arquivo de banco de dados SQLite, caso ainda não exista.

## Tecnologias utilizadas

- Python
- SQLite
- Terminal interativo

## Observação sobre o uso do Copilot

Este projeto foi melhorado com apoio do GitHub Copilot, que ajudou a:

- identificar melhorias no código;
- sugerir organização mais limpa;
- reforçar validações e segurança básica;
- transformar um projeto simples em uma solução mais profissional.

Essa abordagem demonstra como ferramentas de IA podem acelerar o processo de refatoração e aprimoramento de projetos já existentes.

## Conclusão

Este projeto mostra como um sistema simples pode evoluir significativamente com boas práticas de programação, organização de código e uso de ferramentas inteligentes no processo de desenvolvimento.

A versão atual mantém a proposta original, mas com muito mais robustez, clareza e potencial para crescimento.

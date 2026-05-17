# CEUCRUD - Sistema de Gerenciamento Universitario

**Deploy:**  https://lucasabrantes2006.github.io/Trabalho-Bootcamp-II-Desafio---Entrega-Inicial/Inicial/`https://SEU_USUARIO.github.io/NOME_DO_REPOSITORIO/`

O **CEUCRUD** e um sistema desktop desenvolvido em **Python** com **CustomTkinter** para gerenciamento de dados universitarios. Ele se conecta a um banco MySQL e permite realizar CRUD de cursos, alunos, funcionarios, materias e matriculas.

Na entrega intermediaria, o projeto tambem passou a consumir uma **API publica do IBGE** para consultar municipios por UF, exibindo os dados em uma nova aba da interface.

## Entrega Intermediaria

- Issue sugerida: [docs/ISSUE_ENTREGA_INTERMEDIARIA.md](docs/ISSUE_ENTREGA_INTERMEDIARIA.md)
- Branch obrigatoria: `entrega-intermediaria`
- API integrada: IBGE Localidades
- Endpoint usado: `https://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/municipios`
- Teste de integracao: `tests/test_api_ibge.py`
- CI/CD: `.github/workflows/ci.yml`
- Deploy: `docs/index.html` pronto para GitHub Pages

## Tecnologias Utilizadas

- Python 3
- CustomTkinter
- MySQL
- mysql-connector-python
- API publica de Localidades do IBGE
- unittest
- GitHub Actions
- GitHub Pages

## Estrutura do Projeto

```text
.
├── .github/workflows/ci.yml
├── api_ibge.py
├── bd_universidade.sql
├── database.py
├── docs/
│   ├── ISSUE_ENTREGA_INTERMEDIARIA.md
│   └── index.html
├── main.py
├── requirements.txt
├── roxo_theme.json
└── tests/
    └── test_api_ibge.py
```

## Funcionalidades

- Cursos: adicionar, listar, atualizar e excluir.
- Alunos: adicionar, listar, atualizar e excluir.
- Funcionarios: adicionar, listar, atualizar e excluir.
- Materias: adicionar, listar, atualizar e excluir.
- Matriculas: adicionar, listar, atualizar e excluir.
- IBGE: consultar municipios por UF usando API publica.

## Banco de Dados

O script `bd_universidade.sql` cria o banco `universidade`, suas tabelas e dados ficticios para teste.

Para criar o banco, execute no MySQL:

```sql
SOURCE bd_universidade.sql;
```

Depois configure a conexao em `database.py`:

```python
host="localhost"
user="root"
password="SUA_SENHA"
database="universidade"
```

## Como Executar

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute a aplicacao:

```bash
python main.py
```

## Como Testar

Execute os testes automatizados:

```bash
python -m unittest discover -s tests
```

O teste de integracao simula a resposta da API do IBGE para validar o fluxo de dados sem depender de instabilidade externa durante a execucao da pipeline.

## Como Publicar no GitHub Pages

1. Suba o projeto para o GitHub.
2. Acesse `Settings > Pages`.
3. Em `Build and deployment`, selecione `Deploy from a branch`.
4. Escolha a branch `main` e a pasta `/docs`.
5. Salve e copie o link gerado.
6. Atualize a linha **Deploy** no topo deste README com o link publico.

## Fluxo Git da Entrega

```bash
git checkout -b entrega-intermediaria
git add .
git commit -m "Integra API publica do IBGE"
git push -u origin entrega-intermediaria
```

Abra um Pull Request para `main` usando no texto:

```text
closes #NUMERO_DA_ISSUE
```

Depois que o PR for aprovado/mesclado, a Issue sera fechada automaticamente.

## Licenca

Este projeto esta sob a licenca MIT.

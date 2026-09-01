# 📘 Atividade: SQLite com FastAPI

## 🎯 Objetivo

Evolua uma API de tarefas para armazenar dados em um banco SQLite usando SQLAlchemy. Você praticará a criação de tabelas, sessões de banco de dados e endpoints que persistem dados entre execuções.

## 📝 Tarefas

### 🛠️ Configurar o Banco de Dados

#### Descrição
Configure o SQLAlchemy para criar e acessar um arquivo de banco SQLite para a API de tarefas.

#### Requisitos
O programa concluído deve:

- Criar um engine SQLAlchemy apontando para o arquivo `tasks.db`
- Configurar uma fábrica de sessões para acessar o banco de dados
- Definir um modelo `Task` com os campos `id`, `title` e `completed`
- Criar a tabela de tarefas quando a aplicação iniciar

### 🛠️ Salvar e Listar Tarefas

#### Descrição
Implemente endpoints que criem tarefas no banco de dados e retornem as tarefas persistidas.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para salvar uma nova tarefa no banco de dados
- Implementar `GET /tasks` para retornar todas as tarefas salvas
- Retornar o status HTTP `201 Created` ao criar uma tarefa
- Validar que `title` contém pelo menos 3 caracteres usando um modelo Pydantic

### 🛠️ Atualizar uma Tarefa Persistida

#### Descrição
Adicione um endpoint para alterar o status de conclusão de uma tarefa existente no banco de dados.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar o campo `completed`
- Salvar a alteração no banco de dados antes de retornar a resposta
- Retornar a tarefa atualizada em formato JSON
- Retornar `404 Not Found` quando o identificador não existir

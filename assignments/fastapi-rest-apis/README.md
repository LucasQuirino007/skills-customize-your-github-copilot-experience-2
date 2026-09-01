# 📘 Atividade: APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI. Você praticará a criação de endpoints, a validação de dados com modelos Pydantic e o uso apropriado de códigos de status HTTP.

## 📝 Tarefas

### 🛠️ Criar o Endpoint Inicial

#### Descrição
Configure a aplicação FastAPI e implemente um endpoint que confirme que a API está em funcionamento.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` no arquivo `starter-code.py`
- Implementar `GET /` retornando um JSON com a mensagem `{"message": "Task API is running"}`
- Executar a aplicação com Uvicorn e acessar a documentação interativa em `/docs`

### 🛠️ Implementar Endpoints de Tarefas

#### Descrição
Crie endpoints para listar tarefas e adicionar uma nova tarefa à lista em memória fornecida.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks` para retornar a lista de tarefas
- Implementar `POST /tasks` para adicionar uma tarefa com os campos `title` e `completed`
- Retornar o status HTTP `201 Created` após criar uma tarefa
- Validar que `title` contém pelo menos 3 caracteres usando um modelo Pydantic

### 🛠️ Atualizar e Remover Tarefas

#### Descrição
Complete a API com endpoints que permitam atualizar o status de uma tarefa e removê-la pelo seu identificador.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar o campo `completed`
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa
- Retornar `404 Not Found` quando o identificador não existir
- Retornar `204 No Content` depois de remover uma tarefa com sucesso

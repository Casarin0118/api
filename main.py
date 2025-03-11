from flask import Flask, request, jsonify
from flasgger import Swagger
from tarefa import Tarefa

app = Flask(__name__)
swagger = Swagger(app)

tarefas = [
    Tarefa(
        taskid=1,
        titulo="estudar java script",
        descricao="aprender a adicionar eventos nas paginas web",
        status="Em andamento",
        prioridade="Alta",
        data_criacao="2025-04-25",
        responsavel="João"
    ),
    Tarefa(
        taskid=2,
        titulo="lavar louça",
        descricao="lavar as louças",
        status="A fazer",
        prioridade="Baixa",
        data_criacao="2025-02-25",
        responsavel="Maria"
    )
]

@app.route('/tasks', methods=['GET'])
def get_task():
    """
    Retorna todas as tarefas cadastradas.
    ---
    responses:
      200:
        description: Lista de tarefas cadastradas
    """
    return jsonify([tarefa.__dict__ for tarefa in tarefas])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    """
    Retorna uma tarefa específica pelo ID.
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Retorna a tarefa correspondente
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.taskid == task_id:
            return jsonify(tarefa.__dict__)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Cria uma nova tarefa.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - titulo
            - descricao
            - status
            - prioridade
            - data_criacao
            - responsavel
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            data_criacao:
              type: string
            responsavel:
              type: string
    responses:
      201:
        description: Tarefa criada com sucesso
    """
    data = request.json
    new_task = Tarefa(
        taskid=max([t.taskid for t in tarefas], default=0) + 1,
        titulo=data['titulo'],
        descricao=data['descricao'],
        status=data['status'],
        prioridade=data['prioridade'],
        data_criacao=data['data_criacao'],
        responsavel=data['responsavel']
    )
    tarefas.append(new_task)
    return jsonify(new_task.__dict__), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Atualiza uma tarefa existente.
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            titulo:
              type: string
            descricao:
              type: string
            status:
              type: string
            prioridade:
              type: string
            data_criacao:
              type: string
            responsavel:
              type: string
    responses:
      200:
        description: Tarefa atualizada com sucesso
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.taskid == task_id:
            data = request.json
            tarefa.titulo = data.get('titulo', tarefa.titulo)
            tarefa.descricao = data.get('descricao', tarefa.descricao)
            tarefa.status = data.get('status', tarefa.status)
            tarefa.prioridade = data.get('prioridade', tarefa.prioridade)
            tarefa.data_criacao = data.get('data_criacao', tarefa.data_criacao)
            tarefa.responsavel = data.get('responsavel', tarefa.responsavel)
            return jsonify(tarefa.__dict__)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def excluir_task(task_id):
    """
    Exclui uma tarefa pelo ID.
    ---
    parameters:
      - name: task_id
        in: path
        type: integer
        required: true
        description: ID da tarefa
    responses:
      200:
        description: Tarefa excluída com sucesso
      404:
        description: Tarefa não encontrada
    """
    for tarefa in tarefas:
        if tarefa.taskid == task_id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa excluída com sucesso"}), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)

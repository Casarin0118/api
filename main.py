from flask import Flask, request
app = Flask(__name__)


tarefas = [
        {
            "id":1,
            "titulo":"estudar java script",
            "descricao":"aprender a adicionar eventos nas paginas web",
            "status":"Em andamento",
            "prioridade": "Alta",
            "data_criacao": "2025-04-25",
            "responsavel": "João"

        },
        {
            "id":2,
            "titulo":"lavar louça",
            "descricao":"lavar as louças",
            "status" : "A fazer",
            "prioridade": "Baixa",
            "data_criacao": "2025-02-25",
            "responsavel": "Maria"
        }
]

@app.route('/tasks', methods=['GET'])
def get_task():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return tarefa


@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    task['id'] = tarefas[-1].get('id') + 1
    tarefas.append(task)
    print(task)
    return ''

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['prioridade'] = task_body.get('prioridade')
    task_search['data_criacao'] = task_body.get('data_criacao')
    task_search['responsavel'] = task_body.get('responsavel')
    return task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def excluir_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
    return 'tarefa excluida com sucesso!'


if __name__ == '__main__':
    app.run(debug=True)
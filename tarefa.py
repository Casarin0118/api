class Tarefa:
    def __init__(self, taskid, titulo, descricao, status, prioridade, data_criacao, responsavel):
        self.taskid = taskid
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
        self.data_criacao = data_criacao
        self.responsavel = responsavel
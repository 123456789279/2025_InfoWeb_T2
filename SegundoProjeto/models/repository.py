from models import Funcionario, Agendamento

class FuncionarioRepository:
    def __init__(self, conexao):
        self.conexao = conexao
    def salvar(self, trabalhador):
        cursor = self.conexao.cursor()
        cursor.execute(
        "INSERT INTO trabalhador (nome, cpf, email) VALUES (?, ?, ?)",
        (trabalhador.nome, trabalhador.cpf, trabalhador.email)
        )
    self.conexao.commit()
    def buscar_por_id(self, id):
        cursor = self.conexao.cursor()
        cursor.execute(
        "SELECT id, nome, cpf, email FROM trabalhador WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        if resultado:
            return Funcionario(
              id=resultado[0],
              nome=resultado[1],
              cpf=resultado[2],
              email=resultado[3]
              )
            return None
        
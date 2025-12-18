from database import Database
from models.funcionario import Funcionario

# Criar banco e conexão
db = Database()
conexao = db.get_conexao()


# Repositórios
trab_repo = FuncionarioRepository(conexao)
agend_repo = AgendamentoRepository(conexao)


# Criar funcionario)
funcionario= Funcionario(
nome="Maria Silva",
cpf="123.456.789-00",
email="maria@email.com"
)


# Salvar funcionario
funcionario_salvo = trab_repo.salvar(funcionario)
print("Trabalhador salvo:", funcionario_salvo)


# Criar agendamento
agendamento = Agendamento(
data="2025-03-20",
horario="09:30",
local="Posto do Trabalho - Centro",
funcionario_id=funcionario_salvo.id)


# Salvar agendamento
agendamento_salvo = agend_repo.salvar(agendamento)
print("Agendamento salvo:", agendamento_salvo)


# Ler agendamento do banco
agendamento_lido = agend_repo.buscar_por_id(agendamento_salvo.id)
print("Agendamento lido do banco:", agendamento_lido)
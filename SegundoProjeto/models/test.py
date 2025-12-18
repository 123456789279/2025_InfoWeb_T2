from database import Database
from models import Funcionario, Agendamento

# Criar banco e conexão
db = Database()
conexao = db.get_conexao()


# Repositórios
trab_repo = FuncionarioRepository(conexao)
agend_repo = AgendamentoRepository(conexao)


# Criar trabalhador
trabalhador = Trabalhador(
nome="Maria Silva",
cpf="123.456.789-00",
email="maria@email.com"
)


# Salvar trabalhador
trabalhador_salvo = trab_repo.salvar(trabalhador)
print("Trabalhador salvo:", trabalhador_salvo)


# Criar agendamento
agendamento = Agendamento(
data="2025-03-20",
horario="09:30",
local="Posto do Trabalho - Centro",
trabalhador_id=trabalhador_salvo.id
)


# Salvar agendamento
agendamento_salvo = agend_repo.salvar(agendamento)
print("Agendamento salvo:", agendamento_salvo)


# Ler agendamento do banco
agendamento_lido = agend_repo.buscar_por_id(agendamento_salvo.id)
print("Agendamento lido do banco:", agendamento_lido)
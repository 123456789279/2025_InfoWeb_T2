from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.proficional import Proficional, ProficionalDAO
from models.horario import Horario, HorarioDAO

class View:

    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)  
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)   

    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_listar():
        return ServicoDAO.listar()
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)   

    def proficional_inserir(nome, especialidade, conselho, email, senha):
        proficional = Proficional(0, nome, especialidade, conselho, email, senha)
        ProficionalDAO.inserir(proficional)
    def proficional_listar():
        return ProficionalDAO.listar()
    def proficional_listar_id(id):
        return ProficionalDAO.listar_id(id)
    def proficional_atualizar(id, nome, especialidade, conselho, email, senha):
        proficional = Proficional(id, nome, especialidade, conselho, email, senha)
        ProficionalDAO.atualizar(proficional)
    def proficional_excluir(id):
        proficional = Proficional(id, "", "", "", "", "")
        ProficionalDAO.excluir(proficional)   

    def horario_inserir(data, confirmado, cliente, servico, proficional):
        horario = Horario(0, data, confirmado, cliente, servico, proficional)
        HorarioDAO.inserir(horario)
    def horario_listar():
        return HorarioDAO.listar()
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    def horario_atualizar(id, data, confirmado, cliente, servico, proficional):
        horario = Horario(id, data, confirmado, cliente, servico, proficional)
        HorarioDAO.atualizar(horario)
    def horario_excluir(id):
        horario = Proficional(id, "", "", "", "", "")
        HorarioDAO.excluir(horario) 

    def cliente_criar_admin():
        for c in View.cliente_listar():
           if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")   
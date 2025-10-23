from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.proficional import Proficional, ProficionalDAO
from models.horario import Horario, HorarioDAO

import datetime

class View:

    def cliente_inserir(nome, email, fone, senha):
        # verifia se o email ja existe
        for obj in View.cliente_listar():
            if obj.get_email() == email:
                raise ValueError("cliente já cadastrado")
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, fone, senha):
        # verifica se o email já existe em outro serviço
        for obj in View.cliente_listar():
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("Email já cadastrado em outro cliente")
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)  
    def cliente_excluir(id):
        # verifica se o cliente já foi agendado alguma vez
        for obj in View.cliente_listar():
            if obj.get_id_cliente() == id:
                raise ValueError("Cliente já agendado: não é possível excluir")
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente) 

    def servico_inserir(descricao, valor): 
        # verifica se a descrição já existe
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    def servico_atualizar(id, descricao, valor):
        # verifica se a descrição já existe em outro serviço
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Descriçao já cadastrada em outro serviço")
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        # verifica se o serviço já foi agendado alguma vez
        for obj in View.horario_listar():
            if obj.get_id_servico() == id:
                raise ValueError("Serviço já agendado: não é possível excluir")
        servico = Servico(id, "sem descricao", 0)
        ServicoDAO.excluir(servico)   

    def proficional_inserir(nome, especialidade, conselho, email, senha):
        # verifia se o email ja existe
        for obj in View.proficional_listar():
            if obj.get_email() == email:
                raise ValueError("Proficional já cadastrado")
        proficional = Proficional(0, nome, especialidade, conselho, email, senha)
        ProficionalDAO.inserir(proficional)
    def proficional_listar():
        r = ProficionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def proficional_listar_id(id):
        return ProficionalDAO.listar_id(id)
    def proficional_atualizar(id, nome, especialidade, conselho, email, senha):
        # verifica se o email já existe em outro serviço
        for obj in View.proficional_listar():
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("Email já cadastrado em outro proficional")
        proficional = Proficional(id, nome, especialidade, conselho, email, senha)
        ProficionalDAO.atualizar(proficional)
    def proficional_excluir(id):
        # verifica se o proficional já foi agendado alguma vez
        for obj in View.proficional_listar():
            if obj.get_id_proficional() == id:
                raise ValueError("Proficionaljá agendado: não é possível excluir")
        proficional = Proficional(id, "", "", "", "", "")
        ProficionalDAO.excluir(proficional)
    def proficional_alterar_senha(id, senha):
        proficional = Proficional(id, senha)
        ProficionalDAO.alterar_senha(proficional)   

    def horario_inserir(data, confirmado, cliente, servico, proficional):
        # verifia se o proficional ja foi agendado
        for obj in View.horario_listar():
            if obj.get_proficional() == proficional:
                raise ValueError("Proficional já agendado")
        horario = Horario(0, data, confirmado, cliente, servico, proficional)
        HorarioDAO.inserir(horario)
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def horario_listar_id(id):
        return HorarioDAO.listar_id(id)
    def horario_atualizar(id, data, confirmado, cliente, servico, proficional):
        # verifica se o proficional já foi agendado em outro lugar
        for obj in View.proficional_listar():
            if obj.get_id() != id and obj.get_proficional() == proficional:
                raise ValueError("Proficional já agendado em outro lugar")
        horario = Horario(id, data, confirmado, cliente, servico, proficional)
        HorarioDAO.atualizar(horario)
    def horario_excluir(id):
        # verifica se o cliente já foi agendado alguma vez
        for obj in View.cliente_listar():
            if obj.get_id_cliente() == id:
                raise ValueError("Cliente já agendado: não é possível excluir")
        horario = Proficional(id, "", "", "", "", "")
        HorarioDAO.excluir(horario) 
    def horario_agendar_horario(id_proficional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_proficional() == id_proficional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    
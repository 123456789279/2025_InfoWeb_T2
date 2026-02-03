from models.funcionario import Funcionario, FuncionarioDAO
from models.empregador import Empregador, EmpregadorDAO
from models.agendamento import Agendamento, AgendamentoDAO

import datetime

class View:

    def funcionario_inserir(nome, email, fone, senha, cpf):
        # verifia se o email ja existe
        for obj in View.funcionario_listar():
            if obj.get_email() == email:
                raise ValueError("funcionario já cadastrado")
        funcionario = Funcionario(0, nome, email, fone, senha, cpf)
        FuncionarioDAO.inserir(funcionario)
    def funcionario_listar():
        r = FuncionarioDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def funcionario_listar_id(id):
        return FuncionarioDAO.listar_id(id)
    def funcionario_atualizar(id, nome, email, fone, senha, cpf):
        # verifica se o email já existe em outro serviço
        for obj in View.funcionario_listar():
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("Email já cadastrado em outro funcionario")
        funcionario = Funcionario(id, nome, email, fone, senha, cpf)
        FuncionarioDAO.atualizar(funcionario)  
    def funcionario_excluir(id):
        # verifica se o funcionario já foi agendado alguma vez
        for obj in View.funcionario_listar():
            if obj.get_id() == id:
                raise ValueError("Funcionario já agendado: não é possível excluir")
        funcionario = Funcionario(id, "", "", "", "")
        FuncionarioDAO.excluir(funcionario) 
    def funcionario_criar_admin():
        for c in View.funcionario_listar():
            if c.get_email() == "admin": return
        View.funcionario_inserir("admin", "admin", "fone", "1234", "123")
    def funcionario_autenticar(email, senha):
        for c in View.funcionario_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def empregador_inserir(id, nome, email, senha):
        # verifia se o email ja existe
        for obj in View.empregador_listar():
            if obj.get_email() == email:
                raise ValueError("Proficional já cadastrado")
        empregador = Empregador(0, nome, email, senha)
        EmpregadorDAO.inserir(empregador)
    def Empregador_listar():
        r = EmpregadorDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def empregador_listar_id(id):
        return EmpregadorDAO.listar_id(id)
    def empregador_atualizar(id, nome, email, senha):
        # verifica se o email já existe em outro serviço
        for obj in View.empregador_listar():
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("Email já cadastrado em outro empregador")
        empregador = Empregador(id, nome, email, senha)
        EmpregadorDAO.atualizar(empregador)
    def empregador_excluir(id):
        # verifica se o empregador já foi agendado alguma vez
        for obj in View.empregador_listar():
            if obj.get_id() == id:
                raise ValueError("Empregador já agendado: não é possível excluir")
        empregador = Empregador(id, "", "", "")
        EmpregadorDAO.excluir(empregador)
    def empregador_alterar_senha(id, nova_senha):
        empregador = Empregador.get_id(id)  # ou como você busca pelo id
        if empregador is None:
            raise ValueError("Profissional não encontrado")
        empregador.set_senha(nova_senha)
        EmpregadorDAO.atualizar(empregador)  # salva a alteração

    def agendamento_inserir(data, confirmado, funcionario):
        # verifia se o funcionario ja foi agendado
        for obj in View.agendamento_listar():
            if obj.get_funcionario() == funcionario:
                raise ValueError("Funcionario já agendado")
        agendamento = Agendamento(0, data, confirmado, funcionario)
        AgendamentoDAO.inserir(agendamento)
    def agendamento_listar():
        r = AgendamentoDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def agendamento_listar_id(id):
        return AgendamentoDAO.listar_id(id)
    def agendamento_atualizar(id, data, confirmado, funcionario):
        # verifica se o funcionario já foi agendado em outro lugar
        for obj in View._listar():
            if obj.get_id() != id and obj.get_funcionario() == funcionario:
                raise ValueError("Funcionario já agendado em outro lugar")
        agendamento = Agendamento(id, data, confirmado, funcionario)
        AgendamentoDAO.atualizar(agendamento)
    def agendamento_excluir(id):
        # verifica se o cliente já foi agendado alguma vez
        for obj in View.cliente_listar():
            if obj.get_id_cliente() == id:
                raise ValueError("Cliente já agendado: não é possível excluir")
        agendamento = Funcionario(id, "", "", "", "", "")
        AgendamentoDAO.excluir(agendamento) 
    def agendamento_agendar_agendamentoo(id_funcionario):
        r = []
        agora = datetime.datetime.now()
        for h in View.agendamento_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_empregador() == None and h.get_id_funcionario() == id_funcionario:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
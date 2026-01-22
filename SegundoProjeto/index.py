from templates.manterfuncionarioUI import ManterFuncionarioUI
from templates.manterempregadorUI import ManterEmpregadorUI
from templates.manteragendamentoUI import ManterAgendamentoUI

from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilfuncionarioUI import PerfilFuncionarioUI
from views import View

import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Funcionarios", "Cadastro de Empregadores", "Cadastro de Agendamentos"])
        if op == "Cadastro de Funcionarios": ManterFuncionarioUI.main()
        if op == "Cadastro de Empregadores": ManterEmpregadorUI.main()
        if op == "Cadastro de Agendamentos": ManterAgendamentoUI.main()
    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
            "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_funcionario()
            IndexUI.sair_do_sistema()
    def main():
        # verifica a existe o usuário admin
        View.funcionario_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Solicitar Proficional"])
        if op == "Meus Dados": PerfilFuncionarioUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Solicitar Proficional": SolicitarProficionalUI.main()

IndexUI.main()
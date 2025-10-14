from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterproficionalUI import ManterProficionalUI
from templates.manterhorarioUI import ManterHorarioUI

from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.agendarservicoUI import AgendarServicoUI
from views import View

import streamlit as st

class IndexUI:
    def cliente_criar_admin():
        for c in View.cliente_listar():
           if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Proficionais", "Cadastro de Horarios"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Proficionais": ManterProficionalUI.main()
        if op == "Cadastro de Horarios": ManterHorarioUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
            "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()
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
            st.sidebar.write("Bem-vindo(a), " +
                st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
            IndexUI.menu_admin()
    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()

IndexUI.main()
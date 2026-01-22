import streamlit as st
from views import View
import time

class PerfilFuncionarioUI:
      def main():
          st.header("Meus Dados")
          op = View.cliente_listar_id(st.session_state["usuario_id"])
          nome = st.text_input("Informe o novo nome", op.get_nome())
          email = st.text_input("Informe o novo e-mail", op.get_email())
          fone = st.text_input("Informe o novo fone", op.get_fone())
          senha = st.text_input("Informe a nova senha", op.get_senha())
          cpf = st.text_input("Informe o novo cpf", op.get_cpf()),
              type=("password")
          if st.button("Atualizar"):
              id = op.get_id()
              try:
                  id = op.get_id()
                  View.funcionario_atualizar(id, nome, email, fone, senha, cpf)
                  st.success("Funcionario atualizado com sucesso")
              except ValueError as erro:
                  st.error(erro)
          time.sleep(2)
          st.rerun()
import streamlit as st
import pandas as pd
import time
from views import View
class ManterEmpregadorUI:
  def main():
    st.header("Cadastro de Proficionais")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterEmpregadorUI.listar()
    with tab2: ManterEmpregadorUI.inserir()
    with tab3: ManterEmpregadorUI.atualizar()
    with tab4: ManterEmpregadorUI.excluir()
  def listar():
    empregadores = View.empregador_listar()
    if len(empregadores) == 0: st.write("Nenhum empregador cadastrado")
    else:
      list_dic = []
      for obj in empregadores: list_dic.append(obj.to_json())
      df = pd.DataFrame(list_dic)
      st.dataframe(df)
  def inserir():
    id = st.text_input("Informe o id")
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o email")
    senha = st.text_input("Informe a senha", type="password")
    if st.button("Inserir"):
      try:
          View.empregador_inserir(id, nome, email, senha)
          st.success("Empregadores inserido com sucesso")
      except ValueError as erro:
          st.error(erro)
      time.sleep(2)
      st.rerun()
  def atualizar():
    empregadores = View.empregador_listar()
    if len(empregadores) == 0: st.write("Nenhum empregador cadastrado")
    else:
      op = st.selectbox("Atualização de Proficionais", empregadores)
      id = st.text_input("Novo id", op.get_id())
      nome = st.text_input("Novo nome", op.get_nome())
      email = st.text_input("Novo email", op.get_email())
      senha = st.text_input("Nova senha", op.get_senha(), type="password")
      if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.empregador_atualizar(id, nome, email, senha)
            st.success("Empregador atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
  def excluir():
    empregadores = View.empregador_listar()
    if len(empregadores) == 0: st.write("Nenhum empregador cadastrado")
    else:
      op = st.selectbox("Exclusão de Empregadores", empregadores)
      if st.button("Excluir"):
        try:
            id = op.get_id()
            View.empregador_excluir(id)
            st.success("Empregador excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
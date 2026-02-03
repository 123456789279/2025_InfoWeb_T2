import streamlit as st
import pandas as pd
import time
from views import View

class ManterFuncionarioUI:
  def main():
    st.header("Cadastro de Funcionario")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterFuncionarioUI.listar()
    with tab2: ManterFuncionarioUI.inserir()
    with tab3: ManterFuncionarioUI.atualizar()
    with tab4: ManterFuncionarioUI.excluir()
  def listar():
    funcionarios = View.funcionario_listar()
    if len(funcionarios) == 0: st.write("Nenhum funcionario solicitou seguro desemprego")
    else:
      list_dic = []
      for obj in funcionarios: list_dic.append(obj.to_json())
      df = pd.DataFrame(list_dic)
      st.dataframe(df)
  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    cpf = st.text_input("Informe o cpf")
    senha = st.text_input("Informe a senha", type="password")
    if st.button("Inserir"):
      try:
          View.funcionario_inserir(nome, email, fone, senha, cpf)
          st.success("Funcionario inserido com sucesso")
      except ValueError as erro:
          st.error(erro)
      time.sleep(2)
      st.rerun()
  def atualizar():
    funcionarios = View.funcionario_listar()
    if len(funcionarios) == 0: st.write("Nenhum Funcionario fez solicitação")
    else:
      op = st.selectbox("Atualização de Funcionarios", funcionarios)
      nome = st.text_input("Novo nome", op.get_nome())
      email = st.text_input("Novo e-mail", op.get_email())
      fone = st.text_input("Novo fone", op.get_fone())
      cpf = st.text_input("Novo cpf", op.get_cpf())
      senha = st.text_input("Nova senha", op.get_senha(), type="password")
      if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.funcionario_atualizar(id, nome, email, fone, senha, cpf)
            st.success("Funcionario atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
  def excluir():
    funcionarios = View.funcionario_listar()
    if len(funcionarios) == 0: st.write("Nenhum funcionario cadastrado")
    else:
      op = st.selectbox("Exclusão de Funcionarios", funcionarios)
      if st.button("Excluir"):
        try:
            id = op.get_id()
            View.funcionario_excluir(id)
            st.success("Funcionario excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
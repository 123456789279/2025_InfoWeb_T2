import streamlit as st
import pandas as pd
import time
from views import View
class ManterProficionalUI:
  def main():
    st.header("Cadastro de Proficionais")
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir", "Alterar_Senha"])
    with tab1: ManterProficionalUI.listar()
    with tab2: ManterProficionalUI.inserir()
    with tab3: ManterProficionalUI.atualizar()
    with tab4: ManterProficionalUI.excluir()
    with tab5: ManterProficionalUI.alterar_senha()
  def listar():
    proficionais = View.proficional_listar()
    if len(proficionais) == 0: st.write("Nenhum proficional cadastrado")
    else:
      list_dic = []
      for obj in proficionais: list_dic.append(obj.to_json())
      df = pd.DataFrame(list_dic)
      st.dataframe(df)
  def inserir():
    id = st.text_input("Informe o id")
    nome = st.text_input("Informe o nome")
    especialidade = st.text_input("Informe a especialidade")
    conselho = st.text_input("Informe o conselho")
    email = st.text_input("Informe o email")
    senha = st.text_input("Informe a senha", type="password")
    if st.button("Inserir"):
      try:
          View.proficional_inserir(id, nome, especialidade, conselho, email, senha)
          st.success("Proficionais inserido com sucesso")
      except ValueError as erro:
          st.error(erro)
      time.sleep(2)
      st.rerun()
  def atualizar():
    proficionais = View.proficional_listar()
    if len(proficionais) == 0: st.write("Nenhum proficional cadastrado")
    else:
      op = st.selectbox("Atualização de Proficionais", proficionais)
      id = st.text_input("Novo id", op.get_id())
      nome = st.text_input("Novo nome", op.get_nome())
      especialidade = st.text_input("Nova especialidade", op.get_especialidade())
      conselho = st.text_input("Novo conselho", op.get_conselho())
      email = st.text_input("Novo email", op.get_email())
      senha = st.text_input("Nova senha", op.get_senha(), type="password")
      if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.proficional_atualizar(id, nome, especialidade, conselho, email, senha)
            st.success("Proficional atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
  def excluir():
    proficionais = View.proficional_listar()
    if len(proficionais) == 0: st.write("Nenhum proficional cadastrado")
    else:
      op = st.selectbox("Exclusão de Proficionais", proficionais)
      if st.button("Excluir"):
        try:
            id = op.get_id()
            View.proficional_excluir(id)
            st.success("Proficional excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
  def alterar_senha():
      proficionais = View.proficional_alterar_senha()
      if len(proficionais) == 0: st.write("Nenhuma senha cadastrada")
      else:
        op = st.selectbox("Atualização de Proficionais", proficionais)
        id = st.text_input("Novo id", op.get_id(), type="password")
        senha = st.text_input("Nova senha", op.get_senha(), type="password")
        if st.button("Alterar_Senha"):
          try:
              id = op.get_id()
              View.proficional_atualizar(id, senha)
              st.success("Senha e id alterados com sucesso")
          except ValueError as erro:
              st.error(erro)
          time.sleep(2)
          st.rerun()
import streamlit as st
import pandas as pd
import time
from views import View
class ManterProficionalUI:
  def main():
    st.header("Cadastro de Proficionais")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir",
      "Atualizar", "Excluir"])
    with tab1: ManterProficionalUI.listar()
    with tab2: ManterProficionalUI.inserir()
    with tab3: ManterProficionalUI.atualizar()
    with tab4: ManterProficionalUI.excluir()
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
    if st.button("Inserir"):
      View.cliente_inserir(id, nome, especialidade, conselho)
      st.success("Proficionais inserido com sucesso")
      time.sleep(2)
      st.rerun()
  def atualizar():
    proficionais = View.cliente_listar()
    if len(proficionais) == 0: st.write("Nenhum cliente cadastrado")
    else:
      op = st.selectbox("Atualização de Proficionais", proficionais)
      id = st.text_input("Novo id", op.get_id())
      nome = st.text_input("Novo nome", op.get_nome())
      especialidade = st.text_input("Nova especialidade", op.get_especialidade())
      conselho = st.text_input("Novo conselho", op.get_conselho())
      if st.button("Atualizar"):
        id = op.get_id()
        View.cliente_atualizar(id, nome, especialidade, conselho)
        st.success("Proficional atualizado com sucesso")
  def excluir():
    proficionais = View.cliente_listar()
    if len(proficionais) == 0: st.write("Nenhum proficional cadastrado")
    else:
      op = st.selectbox("Exclusão de Proficionais", proficionais)
      if st.button("Excluir"):
        id = op.get_id()
        View.proficional_excluir(id)
        st.success("Proficional excluído com sucesso")
import streamlit as st
import pandas as pd
import time
from views import View
class ManterServicoUI:
  def main():
    st.header("Cadastro de Servico")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir",
      "Atualizar", "Excluir"])
    with tab1: ManterServicoUI.listar()
    with tab2: ManterServicoUI.inserir()
    with tab3: ManterServicoUI.atualizar()
    with tab4: ManterServicoUI.excluir()
  def listar():
    servicos = View.servico_listar()
    if len(servicos) == 0: st.write("Nenhum servico cadastrado")
    else:
      list_dic = []
      for obj in servicos: list_dic.append(obj.to_json())
      df = pd.DataFrame(list_dic)
      st.dataframe(df)
  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    if st.button("Inserir"):
      View.cliente_inserir(nome, email, fone)
      st.success("Cliente inserido com sucesso")
      time.sleep(2)
      st.rerun()
  def atualizar():
    servicos = View.cliente_listar()
    if len(servicos) == 0: st.write("Nenhum servico cadastrado")
    else:
      op = st.selectbox("Atualização de Servico", servicos)
      nome = st.text_input("Novo nome", op.get_nome())
      email = st.text_input("Novo e-mail", op.get_email())
      fone = st.text_input("Novo fone", op.get_fone())
      if st.button("Atualizar"):
        id = op.get_id()
        View.servico_atualizar(id, nome, email, fone)
        st.success("Servico atualizado com sucesso")
  def excluir():
    servicos = View.cliente_listar()
    if len(servicos) == 0: st.write("Nenhum servico cadastrado")
    else:
      op = st.selectbox("Exclusão de Servicos", servicos)
      if st.button("Excluir"):
        id = op.get_id()
        View.cliente_excluir(id)
        st.success("Servico excluído com sucesso")
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
    descricao = st.text_input("Informe a descricao")
    valor = st.text_input("Informe o valor")
    if st.button("Inserir"):
      try:
          View.servico_inserir(descricao, float(valor))
          st.success("Serviço inserido com sucesso")
      except ValueError as erro:
          st.error(erro)
      time.sleep(2)
      st.rerun()
  def atualizar():
    servicos = View.servico_listar()
    if len(servicos) == 0: st.write("Nenhum servico cadastrado")
    else:
      op = st.selectbox("Atualização de Servico", servicos)
      descricao = st.text_input("Nova descricao", op.get_descricao())
      valor = st.text_input("Novo valor", op.get_valor())
      if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.servico_atualizar(id, descricao, valor)
            st.success("Servico atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
  def excluir():
    servicos = View.servico_listar()
    if len(servicos) == 0: st.write("Nenhum servico cadastrado")
    else:
      op = st.selectbox("Exclusão de Servicos", servicos)
      if st.button("Excluir"):
        try:
            id = op.get_id()
            View.servico_excluir(id)
            st.success("Servico excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime
class ManterAgendamentoUI:
   def main():
     st.header("Cadastro de Agendamentos")
     tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", 
        "Atualizar", "Excluir"])
     with tab1: ManterAgendamentoUI.listar()
     with tab2: ManterAgendamentoUI.inserir()
     with tab3: ManterAgendamentoUI.atualizar()
     with tab4: ManterAgendamentoUI.excluir()
   def listar():
     agendamentos = View.agendamento_listar()
     if len(agendamentos) == 0: st.write("Nenhum agendamento cadastrado")
     else:
       dic = []
       for obj in agendamentos:
         funcionario = View.funcionario_listar_id(obj.get_id_funcionario())
         if funcionario != None: funcionario = funcionario.get_nome()
         dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "funcionario" : funcionario})
       df = pd.DataFrame(dic)
       st.dataframe(df)
   def inserir():
     funcionarios = View.funcionario_listar()
     data = st.text_input("Informe a data e agendamento do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
     confirmado = st.checkbox("Confirmado")
     funcionario = st.selectbox("Informe o funcionario", funcionarios, index = None)
     if st.button("Inserir"):
      if funcionario != None: 
         id_funcionario= funcionario.get_id()
      try:
          View.agendamento_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_funcionario)
          st.success("Agendamento inserido com sucesso")
      except ValueError as erro:
          st.error(erro)
      time.sleep(2)
      st.rerun()
   def atualizar():
     agendamentos = View.agendamento_listar()
     if len(agendamentos) == 0: st.write("Nenhum agendamento cadastrado")
     else:
       funcionarios = View.funcionario_listar()
       op = st.selectbox("Atualização de Agendamento", agendamentos)
       data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
       confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
       id_funcionario = None if op.get_id_funcionario() in [0, None] else op.get_id_funcionario()
       #id_serviço ...
       funcionario = st.selectbox("Informe o novo funcionario", funcionarios, next((i for i, c in enumerate(funcionarios) if c.get_id() == id_funcionario), None))
       if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_funcionario, id_servico, id_proficional)
            st.success("Horário atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        if funcionario != None: id_funcionario = funcionario.get_id()
        id_funcionario = None
        time.sleep(2)
        st.rerun()
   def excluir():
     agendamentos = View.agendamento_listar()
     if len(agendamentos) == 0: st.write("Nenhum agendamento cadastrado")
     else:
       op = st.selectbox("Exclusão de Agendamentos", agendamentos)
       if st.button("Excluir"):
        try:
            id = op.get_id()
            View.agendamento_excluir(op.get_id())
            st.success("Agendamento excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
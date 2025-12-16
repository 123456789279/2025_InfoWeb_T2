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
         servico = View.servico_listar_id(obj.get_id_servico())
         proficional = View.proficional_listar_id(obj.get_id_proficional())
         if funcionario != None: funcionario = funcionario.get_nome()
         if servico != None: servico = servico.get_descricao()
         dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "funcionario" : funcionario, "serviço" : servico, "proficional" : proficional})
       df = pd.DataFrame(dic)
       st.dataframe(df)
   def inserir():
     funcionarios = View.funcionario_listar()
     servicos = View.servico_listar()
     proficional = View.proficional_listar()
     data = st.text_input("Informe a data e agendamento do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
     confirmado = st.checkbox("Confirmado")
     funcionario = st.selectbox("Informe o funcionario", funcionarios, index = None)
     servico = st.selectbox("Informe o serviço", servicos, index = None)
     proficional = st.selectbox("Informe o proficional", proficional, index = None)
     if st.button("Inserir"):
      if funcionario != None: 
         id_funcionario= funcionario.get_id()
      if servico != None: 
         id_servico = servico.get_id()
      if proficional != None: 
         id_proficional = proficional.get_id()
      try:
          View.agendamento_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_funcionario, id_servico, id_proficional)
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
       servicos = View.servico_listar()
       proficionais = View.proficional_listar()
       op = st.selectbox("Atualização de Horários", agendamentos)
       data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
       confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
       id_funcionario = None if op.get_id_funcionario() in [0, None] else op.get_id_funcionario()
       id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
       id_proficional = None if op.get_id_proficional() in [0, None] else op.get_id_proficional()
       #id_serviço ...
       funcionario = st.selectbox("Informe o novo funcionario", funcionarios, next((i for i, c in enumerate(funcionarios) if c.get_id() == id_funcionario), None))
       servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
       proficional = st.selectbox("Informe o novo proficional", proficionais, next((i for i, s in enumerate(proficionais) if s.get_id() == id_proficional), None))
       if st.button("Atualizar"):
        try:
            id = op.get_id()
            View.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_funcionario, id_servico, id_proficional)
            st.success("Horário atualizado com sucesso")
        except ValueError as erro:
            st.error(erro)
        if funcionario != None: id_funcionario = funcionario.get_id()
        if servico != None: id_servico = servico.get_id()
        if proficional != None: id_proficional = proficional.get_id()
        id_funcionario = None
        id_servico = None
        id_proficional = None
        time.sleep(2)
        st.rerun()
   def excluir():
     agendamentos = View.agendamento_listar()
     if len(agendamentos) == 0: st.write("Nenhum horário cadastrado")
     else:
       op = st.selectbox("Exclusão de Horários", agendamentos)
       if st.button("Excluir"):
        try:
            id = op.get_id()
            View.agendamento_excluir(op.get_id())
            st.success("Agendamento excluído com sucesso")
        except ValueError as erro:
            st.error(erro)
        time.sleep(2)
        st.rerun()
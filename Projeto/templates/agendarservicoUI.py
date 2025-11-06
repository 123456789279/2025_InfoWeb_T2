import streamlit as st
from views import View
from models.servico import Servico
import time
class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional cadastrado")
        else:
            proficional = st.selectbox("Informe o proficional", profs)
            horarios = View.horario_agendar_horario(proficional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
              horario = st.selectbox("Informe o horário", horarios)
              servicos = View.servico_listar()
              servico = st.selectbox("Informe o serviço", servicos)
              if st.button("Agendar"):
                  View.horario_atualizar(horario.get_id(),
                      horario.get_data(), False,
                      st.session_state["usuario_id"],
                      servico.get_id(), proficional.get_id())
                  st.success("Horário agendado com sucesso")
                  time.sleep(2)
                  st.rerun()
    
    def solicitar_proficional():
        st.header("Solicitar Profissional")
        profs = View.profissional_listar()
        if len(profs) == 0: st.write("Nenhum profissional solicitado")
        else:
            proficional = st.selectbox("Informe o proficional", profs)
            proficionais = st.selectbox("Informe os proficionais", profs)
            horarios = View.horario_agendar_horario(proficional.get_id())
            if len(horarios) == 0: st.write("Nenhum horário disponível")
            else:
              horario = st.selectbox("Informe o horário", horarios)
              proficionais = View.proficional_listar()
              proficional = st.selectbox("Informe o serviço", proficionais)
              if st.button("Agendar"):
                  View.horario_atualizar(horario.get_id(),
                      horario.get_data(), False,
                      st.session_state["usuario_id"],
                      Servico.get_id(), proficional.get_id())
                  st.success("Horário agendado com sucesso")
                  time.sleep(2)
                  st.rerun()
import streamlit as st
from templates import AbrirMinhaAgendaUI
import time
import datetime

class ConfrirmarServicoUI:
      def confirmar():
          st.header("Abrir Conta no Sistema")
          horario = st.strptime_input("Informe o horario")
          cliente = st.text_input("Informe o cliente", type="password")
          if st.button("Inserir"):
              templates.abrirminhaagendaUI(horario, cliente)
              st.success("Conta criada com sucesso")
              time.sleep(2)
              st.rerun()
          templates.abrirminhaagendaUI(datetime.strptime(horario, "%d/%m/%Y %H:%M"), horario)
          st.success("Horário inserido com sucesso")
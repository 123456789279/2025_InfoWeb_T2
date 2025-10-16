import streamlit as st
from views import View
import time
import datetime
class ConfirmarServicoUI:
      def confirmar():
          st.header("Abrir Conta no Sistema")
          horario = st.strptime_input("Informe o horario")
          cliente = st.text_input("Informe o cliente", type="password")
          if st.button("Inserir"):
              View.abrirminhaagendaUI(horario, cliente)
              st.success("Conta criada com sucesso")
              time.sleep(2)
              st.rerun()
          View.abrirminhaagendaUI(datetime.strptime(horario, "%d/%m/%Y %H:%M"), horario)
          st.success("Horário inserido com sucesso")
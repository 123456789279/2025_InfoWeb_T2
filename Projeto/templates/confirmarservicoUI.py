import streamlit as st
from templates import AbrirMinhaAgendaUI
import time
import datetime

class ConfrirmarServicoUI:
      def main():
          st.header("Abrir Conta no Sistema")
          horario = st.text_datetime("Informe o horario")
          cliente = st.text_input("Informe o cliente", type="password")
          if st.button("Inserir"):
              templates.abrirminhaagendaUI(horario, cliente)
              st.success("Conta criada com sucesso")
              time.sleep(2)
              st.rerun()
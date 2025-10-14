import streamlit as st
from views import View
from models.proficional import Proficional, ProficionalDAO
import time
import datetime

class AbrirMinhaAgendaUI:
      def main():
          st.header("Abrir Agenda no Sistema")
          data = st.datetime_input("Informe a data no formato dd/mm/aaaa")
          horario_inicio = st.datetime_input("Informe o horario inicial no formato HH:MM")
          horario_final = st.datetime_input("Informe o horario final no formato HH:MM")
          intervalo = st.timedate_input("Informe o intervalo entre os horarios{min}")
          if st.button("Inserir"):
              View.proficional_inserir(data, horario_inicio, horario_final, intervalo)
              st.success("agenda aberta com sucesso")
              time.sleep(2)
              st.rerun()
      def listar():
        proficionais = View.proficional_listar()
        if len(proficionais) == 0: st.write("Nenhum proficional cadastrado")
        else:
          list_dic = []
          for obj in proficionais: list_dic.append(obj.to_json())
          df = pd.DataFrame(list_dic)
          st.dataframe(df)
      def inserir():
        nome_cliente = st.text_input("Informe o nome do cliente")
        servico_realizado = st.text_input("Informe a servico que foi realizado")
        servico_ser_realizado = st.text_input("Informe o servico a ser realizado")
        if st.button("Inserir"):
          View.cliente_inserir(nome_cliente, servico_realizado, servico_ser_realizado)
          st.success("Realizado com sucesso")
          time.sleep(2)
          st.rerun()
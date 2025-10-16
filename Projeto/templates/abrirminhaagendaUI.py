import streamlit as st
from views import View
import time
import datetime
import pandas as pd

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
          View.abrirminhaagendaUI(datetime.strptime(horario_inicio, "%H:%M"), horario_inicio)
          View.abrirminhaagendaUI(datetime.strptime(horario_final, "%H:%M"), horario_final)
          View.abrirminhaagendaUI(datetime.strptime(intervalo, "%M"), intervalo)
          st.success("Horário inserido com sucesso")
      def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horario listado")
        else:
          list_dic = []
          for obj in horarios: list_dic.append(obj.to_json())
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
        def alterar():
          proficionais = View.abrirminhaagendaUI_alterar()
          if len(proficionais) == 0: st.write("Nenhuma senha cadastrada")
          else:
            op = st.selectbox("Atualização de Proficionais", proficionais)
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if st.button("Alterar_Senha"):
              id = op.get_id()
              View.cliente_atualizar(id, senha)
              st.success("Senha alterada com sucesso")
              time.sleep(2)
              st.rerun()
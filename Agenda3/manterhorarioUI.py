import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
   def main():
     st.header("Cadastro de Horários")
     tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
     with tab1: ManterHorarioUI.listar()
     with tab2: ManterHorarioUI.inserir()
     with tab3: ManterHorarioUI.atualizar()
     with tab4: ManterHorarioUI.excluir()
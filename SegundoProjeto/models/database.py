import sqlite3


class Database:
   def __init__(self, nome_banco="seguro.db"):
       self.conexao = sqlite3.connect(nome_banco)
       self.criar_tabelas()


def criar_tabelas(self):
    cursor = self.conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trabalhador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        email TEXT NOT NULL
        )
        """)
    cursor.execute(""" CREATE TABLE IF NOT EXISTS agendamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        local TEXT NOT NULL,
        trabalhador_id INTEGER NOT NULL,
        FOREIGN KEY (trabalhador_id) REFERENCES trabalhador(id)
        )
        """)
    self.conexao.commit()

def get_conexao(self):
    return self.conexao
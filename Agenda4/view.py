from Agenda4.proficional import Proficional, ProficionalDAO
class View:
  def proficional_listar():
    return ProficionalDAO.listar()
  def proficional_inserir(id, nome, especialidade, conselho):
    proficional = Proficional(0, nome, especialidade, conselho)
    ProficionalDAO.inserir(proficional)
  def proficional_atualizar(id, nome, especialidade, conselho):
    proficional = Proficional(id, nome, especialidade, conselho)
    ProficionalDAO.atualizar(proficional)
  def proficional_excluir(id):
    proficional = Proficional(id, "", "", "")
    ProficionalDAO.excluir(proficional)
class Cliente:
    def __init__(self):
        self.__id = ""
        self.__nome = ""
        self.__email = ""
        self.__fone = ""
    def set__id(self, id):
        if self.__id <= 5: raise ValueError("O id deve ter no minimo 5 digitos")
        self.__id = id
    def set__nome(self, nome):
        if self.__nome <= 4: raise ValueError("O nome do cliente deve ter no minimo 4 letras")
        self.__nome = nome
    def set__email(self, email):
        if self.__email <= 4: raise ValueError("O E-mail do cliente deve ter no minimo 4 caracteris")
        self.__email = email
    def set__fone(self, fone):
        if self.__id <= 5: raise ValueError("O id deve ter no minimo 5 digitos")

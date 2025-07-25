class Cliente:
    def __init__(self):
        self.__id = ""
        self.__nome = ""
        self.__email = ""
        self.__fone = ""
    def set__id(self, id):
        if self.__id <= 5: raise ValueError("O id de um cliente deve ter no minimo 5 digitos")
        self.__id = id
    def set__nome(self, nome):
        if self.__nome <= 4: raise ValueError("O nome do cliente deve ter no minimo 4 letras")
        self.__nome = nome
    def set__email(self, email):
        if self.__email <= 4: raise ValueError("O E-mail do cliente deve ter no minimo 4 caracteris")
        self.__email = email
    def set__fone(self, fone):
        if self.__fone <= 5: raise ValueError("O fone deve ter no minimo 5 digitos no registro de um cliente, ou de uma empresa")
        self.__fone = fone
    def get__id(self):
        return self.__nome
    def get__nome(self):
        return self.__nome
    def get__email(self):
        return self.__email
    def get__fone(self):
        return self.__fone
    def ToString(self, id, nome, email, fone):
        return  {id: self.__id
                 nome: self.__nome
                 email: self.__email
                 fone: self.__fone}
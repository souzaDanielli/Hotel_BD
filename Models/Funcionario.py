class Funcionario:
    def __init__(self, cpf, nome, telefone, data_nascimento, data_cadastro):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._data_nascimento = data_nascimento
        self._data_cadastro = data_cadastro

    # Getters e Setters
    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_data_nascimento(self):
        return self._data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento
    
    def get_data_cadastro(self):
        return self._data_cadastro

    def set_data_cadastro(self, data_cadastro):
        self._data_cadastro = data_cadastro



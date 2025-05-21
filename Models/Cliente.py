class Cliente:
    def __init__(self, cpf, nome, data_nascimento, cidade, telefone):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cidade = cidade
        self._telefone = telefone

    # cpf
    def get_cpf(self):
        return self._cpf
    def set_cpf(self, cpf):
        self._cpf = cpf

    #nome
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome
    
    #data_nascimento
    def get_data_nascimento(self):
        return self._data_nascimento
    def set_data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento
    
    #cidade
    def get_cidade(self):
        return self._cidade
    def set_cidade(self, cidade):
        self._cidade = cidade

    #telefone
    def get_telefone(self):
        return self._telefone
    def set_telefone(self, telefone):
        self._telefone = telefone
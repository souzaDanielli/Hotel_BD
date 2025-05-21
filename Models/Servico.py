class Servico:
    def __init__(self, id, id_funcionario, descricao, id_cliente, id_quarto):
        self._id = id
        self._id_funcionario = id_funcionario
        self._descricao = descricao
        self._id_cliente = id_cliente
        self._id_quarto = id_quarto

    # Getters e Setters
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_id_funcionario(self):
        return self._id_funcionario

    def set_id_funcionario(self, id_funcionario):
        self._id_funcionario = id_funcionario

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_id_cliente(self):
        return self._id_cliente

    def set_id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    def get_id_quarto(self):
        return self._id_quarto

    def set_id_quarto(self, id_quarto):
        self._id_quarto = id_quarto
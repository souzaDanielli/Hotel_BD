class Reserva:
    def __init__(self, id, data_entrada, data_saida, cpf_cliente):
        self.id = id
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.cpf_cliente = cpf_cliente

    # id
    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id

    # data_entrada
    def get_data_entrada(self):
        return self._data_entrada
    def set_data_entrada(self, data_entrada):
        self._data_entrada = data_entrada

    # data_saida
    def get_data_saida(self):
        return self._data_saida
    def set_data_saida(self, data_saida):
        self._data_saida = data_saida;

    # cpf_cliente
    def get_cpf_cliente(self):
        return self._cpf_cliente
    def set_cpf_cliente(self,cpf_cliente):
        self._cpf_cliente = cpf_cliente

class Quarto:
    def __init__(self, num_quarto, descricao, id_reserva):
        self.num_quarto = num_quarto
        self.descricao = descricao
        self.id_reserva = id_reserva

    # num_quarto
    def get_num_quarto(self):
        return self._num_quarto
    def set_num_quarto(self, num_quarto):
        self._num_quarto = num_quarto

    # descricao
    def get_descricao(self):
        return self._descricao
    def set_descricao(self, descricao):
        self._descricao = descricao

    # id_reserva
    def get_id_reserva(self):
        return self._id_reserva
    def set_id_reserva(self, id_reserva):
        self._id_reserva = id_reserva
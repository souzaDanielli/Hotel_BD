class Quarto:
    def __init__(self, num_quarto, descricao):
        self._num_quarto = num_quarto
        self._descricao = descricao

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
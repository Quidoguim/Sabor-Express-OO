from Modelos.Cardápio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    @property
    def descricao(self):
        return self._descricao

    def __str__(self):
        return self._nome + ' - ' + str(self._preco) + ' - ' + self._descricao

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)  # Aplicando 5% de desconto

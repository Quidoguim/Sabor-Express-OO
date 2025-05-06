from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        """
        Método abstrato para aplicar desconto no item do cardápio.
        Deve ser implementado nas subclasses.
        """
        pass

    def __str__(self):
        return self._nome + ' - ' + str(self._preco)

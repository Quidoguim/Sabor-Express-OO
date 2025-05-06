from Modelos.pareceres import Pareceres
from Modelos.Cardápio.item_cardapio import ItemCardapio


class Restaurante:
    """
    Classe que representa um restaurante no sistema de avaliação.

    Atributos de classe:
        restaurantes (list): Lista de todos os objetos Restaurante instanciados.
    """

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa um novo restaurante com nome, categoria, status inativo e lista de pareceres vazia.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria do restaurante (ex: 'Japonesa', 'Italiana').
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._status = False
        self._pareceres = []
        self._cardapio = []
        self.restaurantes.append(self)

    def __str__(self):
        """
        Retorna a representação textual do restaurante, incluindo nome, categoria,
        média das avaliações e status atual.

        Returns:
            str: Representação textual do restaurante.
        """
        return f'Nome: {self._nome}, Categoria: {self._categoria}, Avaliação: {self._pareceres}, Status: {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        """
        Exibe no terminal todos os restaurantes cadastrados, com informações formatadas:
        nome, categoria, média das avaliações e status.
        """
        print(f'Listando restaurantes...')
        for restaurante in cls.restaurantes:
            print(
                f'Nome: {restaurante._nome.ljust(20)} | Categoria: {restaurante._categoria.ljust(20)} | Avaliação: {str(restaurante.meio_pareceres).ljust(20)} | Status: {restaurante.status.ljust(20)} |')

    @property
    def status(self):
        """
        Retorna o status atual do restaurante em forma de emoji.

        Returns:
            str: '✅' se ativo, '❎' se inativo.
        """
        return '✅' if self._status else '❎'

    def alternar_status(self):
        """
        Alterna o status do restaurante entre ativo e inativo.
        """
        self._status = not self._status

    def receber_parecer(self, cliente, nota):
        """
        Registra um parecer (avaliação) para o restaurante, com base em uma nota de um cliente.

        Args:
            cliente (str): Nome do cliente que está avaliando.
            nota (float): Nota atribuída ao restaurante (entre 0 e 10).
        """
        if nota < 0 or nota <= 10:
            pareceres = Pareceres(cliente, nota)
            self._pareceres.append(pareceres)

    @property
    def meio_pareceres(self):
        """
        Calcula e retorna a média das notas dos pareceres recebidos.

        Returns:
            float | str: Média das notas (com uma casa decimal), ou '-' se não houver avaliações.
        """
        if not self._pareceres:
            return '-'
        soma_das_notas = sum([parecer._nota for parecer in self._pareceres])
        quantidade_de_notas = len(self._pareceres)
        resultado = round(soma_das_notas / quantidade_de_notas, 1)
        return resultado

    # def adicionar_bebida(self, bebida):
    #     """
    #     Adiciona uma bebida ao cardápio do restaurante.

    #     Args:
    #         bebida (Bebida): Objeto Bebida a ser adicionado ao cardápio.
    #     """
    #     self._cardapio.append(bebida)

    # def adicionar_prato(self, prato):
    #     """
    #     Adiciona um prato ao cardápio do restaurante.

    #     Args:
    #         prato(Prato): Objeto Prato a ser adicionado ao cardápio.
    #     """

    #     self._cardapio.append(prato)

    def adicionar_item_cardapio(self, item_cardapio):
        if isinstance(item_cardapio, ItemCardapio):
            self._cardapio.append(item_cardapio)

    @property
    def listar_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}:\n')
        for i, item_cardapio in enumerate(self._cardapio, start=1):
            if hasattr(item_cardapio, 'descricao'):
                mensagem_prato = f'{i} - Nome: {item_cardapio._nome} | Preço: R$ {item_cardapio._preco} | Descrição: {item_cardapio._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i} - Nome: {item_cardapio._nome} | Preço: R$ {item_cardapio._preco} | Descrição: {item_cardapio._descricao}'
                print(mensagem_bebida)

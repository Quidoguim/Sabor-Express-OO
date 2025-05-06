from Modelos.restaurante import Restaurante
from Modelos.Cardápio.prato import Prato
from Modelos.Cardápio.bebida import Bebida

restaurante_1 = Restaurante('Yakuza Sushi 893', 'Japonesa')
prato_1 = Prato('Sushi', 25.00, 'Sushi de salmão')
prato_1.aplicar_desconto()
bebida_1 = Bebida('Cerveja', 10.00, 'Cerveja gelada')
bebida_1.aplicar_desconto()
restaurante_1.adicionar_item_cardapio(prato_1)
restaurante_1.adicionar_item_cardapio(bebida_1)


def main():
    restaurante_1.listar_cardapio


if __name__ == '__main__':
    main()

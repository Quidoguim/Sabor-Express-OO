from Modelos.restaurante import Restaurante
from Modelos.Cardápio.prato import Prato
from Modelos.Cardápio.bebida import Bebida

restaurante_1 = Restaurante('Yakuza Sushi 893', 'Japonesa')
prato_1 = Prato('Sushi', 25.00, 'Sushi de salmão')
bebida_1 = Bebida('Cerveja', 10.00, 'Cerveja gelada')


def main():
    print(prato_1)


if __name__ == '__main__':
    main()

from Modelos.restaurante import Restaurante

restaurante_1 = Restaurante('Yakuza Sushi 893', 'Japonesa')
restaurante_1.receber_parecer('Guilherme', 10)
restaurante_1.receber_parecer('Maria', 9)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()

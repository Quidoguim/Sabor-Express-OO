class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False

    def __str__(self):
        return f'Nome: {self.nome}, Categoria: {self.categoria}, Status: {self.status}'


restaurante_1 = Restaurante('Yakuza', 'Japonesa')
restaurante_2 = Restaurante('Coco Bambu', 'Frutos do Mar')

restaurantes = [restaurante_1, restaurante_2]

print(restaurante_1)
print(restaurante_2)

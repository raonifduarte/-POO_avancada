class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class SpiderMan(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teia entre predios')


if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')
    aranha = Aranha()
    print(f'Aranha: {aranha.capacidades}')
    parker = SpiderMan()
    print(f'Peter Parker: {parker.capacidades}')

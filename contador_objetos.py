class ClassesSimples:
    contador = 0

    def __init__(self):
        self.contar()

    @classmethod
    def contar(cls):
        cls.contador += 1


if __name__ == '__main__':
    Lista = [ClassesSimples(), ClassesSimples(), ClassesSimples()]
    print(ClassesSimples.contador)

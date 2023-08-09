#02
class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


estudante1 = Estudante("Gabriel", 21)
estudante2 = Estudante("Giovana", 22)
estudante3 = Estudante("Carlos", 19)

estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()

#01
class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando uma instância da classe Estudante
estudante1 = Estudante("Gabriel", 21)

# Chamando o método apresentar
estudante1.apresentar()
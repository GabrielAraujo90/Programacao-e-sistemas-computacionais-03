#03 
class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")

# Criando três instâncias da classe Estudante com informações diferentes
estudante1 = Estudante("Gabriel", 21, "Engenharia")
estudante2 = Estudante("Giovana", 22, "Zootecnia")
estudante3 = Estudante("Carlos", 19, "Administração")

# Usando o método apresentar para exibir informações dos três estudantes
estudante1.apresentar()
estudante2.apresentar()
estudante3.apresentar()
#04 
class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}.")
    
    def aniversario(self):
        self.idade += 1

# Criando uma instância da classe Estudante
estudante1 = Estudante("Gabriel", 21, "Engenharia")

# Usando o método aniversario para aumentar a idade do estudante em 1
estudante1.aniversario()

# Usando o método apresentar para exibir informações atualizadas do estudante
estudante1.apresentar()
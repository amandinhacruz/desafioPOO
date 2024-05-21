class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.ocupado = False

    def falar(self, mensagem):
        if self.ocupado:
            print(f"{self.nome} diz: Estou ocupado.")

        else:
            print(f"{self.nome} diz: {mensagem}")


    def comer(self, comida):
        if self.ocupado:
            print(f"{self.nome} diz: Não posso comer, estou ocupado")

        else:
            print(f"{self.nome} está comendo {comida}")
            self.ocupado = True

    def dormir(self):
        if self.ocupado:
            print(f"{self.nome} está ocupado e não pode dormir agora")

        else:
            print(f"{self.nome} está dormindo")
            self.ocupado = False
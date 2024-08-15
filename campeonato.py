class Equipe:
    def __init__(self, nome):
        self.nome = nome

class Campeonato:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Campeonato, cls).__new__(cls)
            cls._instance.equipes = []
        return cls._instance

    def adicionar_equipe(self, equipe):
        self.equipes.append(equipe)

    def listar_equipes(self):
        return [equipe.nome for equipe in self.equipes]
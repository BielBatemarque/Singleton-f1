# observer.py
class CarroObserver:
    def update(self, carro):
        pass

class CombustivelObserver(CarroObserver):
    def update(self, carro):
        if carro.combustivel < 10:
            print(f"Aviso: O combustível do carro está baixo!")

class PneusObserver(CarroObserver):
    def update(self, carro):
        if carro.desgaste_pneus > 70:
            print(f"Aviso: Os pneus do carro estão desgastados!")

class CarroMonitorado:
    def __init__(self):
        self.observers = []
        self._combustivel = 100
        self._desgaste_pneus = 0

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self)

    @property
    def combustivel(self):
        return self._combustivel

    @combustivel.setter
    def combustivel(self, valor):
        self._combustivel = valor
        self.notificar_observers()

    @property
    def desgaste_pneus(self):
        return self._desgaste_pneus

    @desgaste_pneus.setter
    def desgaste_pneus(self, valor):
        self._desgaste_pneus = valor
        self.notificar_observers()
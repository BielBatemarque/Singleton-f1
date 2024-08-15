class Carro:
    def __init__(self):
        self.motor = None
        self.chassis = None
        self.pneus = None

    def especificacoes(self):
        return f"Motor: {self.motor}, Chassis: {self.chassis}, Pneus: {self.pneus}"

class CarroBuilder:
    def __init__(self):
        self.carro = Carro()

    def construir_motor(self, motor):
        self.carro.motor = motor
        return self

    def construir_chassis(self, chassis):
        self.carro.chassis = chassis
        return self

    def construir_pneus(self, pneus):
        self.carro.pneus = pneus
        return self

    def get_carro(self):
        return self.carro
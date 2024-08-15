class Motor:
    def tipo(self):
        raise NotImplementedError

class MotorCombustao(Motor):
    def tipo(self):
        return "Motor a Combustão"

class MotorEletrico(Motor):
    def tipo(self):
        return "Motor Elétrico"

class MotorAdapter:
    def __init__(self, motor):
        self.motor = motor

    def especificacao(self):
        return f"Adaptado: {self.motor.tipo()}"
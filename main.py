# main.py
from campeonato import Campeonato, Equipe
from carro import CarroBuilder
from motor import MotorCombustao, MotorEletrico, MotorAdapter
from observer import CarroMonitorado, CombustivelObserver, PneusObserver

def main():
    # Singleton: Criando campeonato e adicionando equipes
    campeonato = Campeonato()
    equipe_a = Equipe("Equipe A")
    equipe_b = Equipe("Equipe B")
    campeonato.adicionar_equipe(equipe_a)
    campeonato.adicionar_equipe(equipe_b)
    print("Equipes no campeonato:", campeonato.listar_equipes())

    # Builder: Construindo um carro
    builder = CarroBuilder()
    carro = (builder
             .construir_motor("V8")
             .construir_chassis("Monocoque")
             .construir_pneus("Pirelli")
             .get_carro())

    print("Especificações do carro:", carro.especificacoes())

    # Adapter: Usando motor com Adapter
    motor_combustao = MotorCombustao()
    motor_eletrico = MotorEletrico()

    adaptador_combustao = MotorAdapter(motor_combustao)
    adaptador_eletrico = MotorAdapter(motor_eletrico)

    print(adaptador_combustao.especificacao())
    print(adaptador_eletrico.especificacao())

    # Observer: Monitorando o estado do carro
    carro_monitorado = CarroMonitorado()
    carro_monitorado.adicionar_observer(CombustivelObserver())
    carro_monitorado.adicionar_observer(PneusObserver())

    # Alterando estados do carro para acionar os observers
    carro_monitorado.combustivel = 5  # Aviso de combustível baixo
    carro_monitorado.desgaste_pneus = 80  # Aviso de desgaste de pneus

if __name__ == "__main__":
    main()
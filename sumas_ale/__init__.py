import random
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'sumas'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIME_OUT_SUMAS = 20


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    resultado = models.IntegerField()
    sumando1 = models.IntegerField()
    sumando2 = models.IntegerField()
    buenas = models.IntegerField(initial=0)
    malas = models.IntegerField(initial=0)


class Sumas(Page):
    form_model = 'player'
    form_fields = ['resultado']
    timeout_seconds = C.TIME_OUT_SUMAS
    timer_text = 'Tiempo restante:'

    @staticmethod
    def vars_for_template(player: Player):
        player.sumando1 = random.randint(10, 80)
        player.sumando2 = random.randint(10, 80)
        return(dict(sumando1=player.sumando1, sumando2=player.sumando2))

    @staticmethod
    def live_method(player, data):
        print('resultado del jugador', player.id_in_group, ':', data)
        resultado = player.sumando1 + player.sumando2
        print('respuesta correcta: ',resultado)
        if data == resultado:
            respuesta = 'Correcto'
            player.buenas = player.buenas+1
        else:
            respuesta = 'Incorrecto'
            player.malas = player.malas + 1

        player.sumando1 = random.randint(10, 80)
        player.sumando2 = random.randint(10, 80)
        return {player.id_in_group: dict(sumando1=player.sumando1, sumando2=player.sumando2, respuesta=respuesta)}


class Resultado(Page):
    pass

page_sequence = [Sumas, Resultado]

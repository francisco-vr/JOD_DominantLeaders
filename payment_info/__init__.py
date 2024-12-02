from otree.api import *
from collections import defaultdict
import random


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PAGO_BASE = 5000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def get_data_from_previous_apps(player: Player):
    """Función para obtener valores de aciertos y pagos de cada ronda."""
    
    # Inicializar las listas para almacenar los aciertos y los pagos
    acierto_norms = []
    JOD_PagoFinal = []

    # Recorrer las 12 rondas para agregar los aciertos de normas (si están disponibles)
    for round_num in range(1, 13):
        for i in range(1, 9):
            acierto_norma = getattr(player.participant, f'acierto_norma{round_num}_{i}', None)
            if acierto_norma is not None:
                acierto_norms.append(acierto_norma)

    # Verificar si existe el diccionario 'endownment_final_per_round' en participant.vars
    if 'endownment_final_per_round' in player.participant.vars:
        # Agregar cada valor del diccionario a la lista de pagos
        for round_num, endownment_value in player.participant.vars['endownment_final_per_round'].items():
            JOD_PagoFinal.append(endownment_value)

    # Retornar las listas completas
    return acierto_norms, JOD_PagoFinal


def calculate_payment(player: Player):
    """Función para calcular el pago total del participante."""
    
    # Obtener las listas de aciertos y pagos finales
    acierto_norms, JOD_PagoFinal = get_data_from_previous_apps(player)

    # Pago base
    total_payment = C.PAGO_BASE

    # Filtrar listas para eliminar posibles valores None
    acierto_norms = [value for value in acierto_norms if value is not None]
    JOD_PagoFinal = [value for value in JOD_PagoFinal if value is not None]

    # Seleccionar aleatoriamente un acierto de normas y un pago final si existen
    random_aciertoNorms = random.choice(acierto_norms) if acierto_norms else 0
    random_JODPagoFinal = random.choice(JOD_PagoFinal) if JOD_PagoFinal else 0

    # Seleccionar aleatoriamente entre el acierto y el pago final
    random_pagoFinal = random.choice([random_aciertoNorms, random_JODPagoFinal])

    # Calcular el pago final basado en la elección
    if random_pagoFinal == random_aciertoNorms:
        if random_pagoFinal == 1:
            total_payment += 7000  # Si el acierto es 1, agregar 7000 CLP
        else:
            total_payment += 0  # Si el acierto es 0, no agregar nada
    else:
        total_payment += random_pagoFinal  # Si se selecciona el pago final, agregarlo al total

    return total_payment


# PAGES
class final(Page):

    @staticmethod
    def vars_for_template(player: Player):
        # Calcular el pago total usando la función calculate_payment
        total_payment = calculate_payment(player)
        print("total_payment es: ", total_payment)
        
        # Obtener los valores aleatorios de aciertos y pagos para mostrar en la plantilla
        acierto_norms, JOD_PagoFinal = get_data_from_previous_apps(player)
        random_JODPagoFinal = random.choice(JOD_PagoFinal) if JOD_PagoFinal else 0
        random_aciertoNorms = random.choice(acierto_norms) if acierto_norms else 0
        
        # Seleccionar el pago final (random entre acierto y pago final)
        random_pagoFinal = random.choice([random_aciertoNorms, random_JODPagoFinal])
        
        # Retornar las variables al contexto de la plantilla
        return dict(
            total_payment=total_payment,
            random_pagoFinal=random_pagoFinal
        )


page_sequence = [final]

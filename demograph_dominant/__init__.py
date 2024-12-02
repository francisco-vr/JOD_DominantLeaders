from otree.api import *
from collections import defaultdict
import random



def make_field(label):
    return models.StringField(
        choices=[[1, 'Muy inapropiado socialmente'], [2, 'Algo inapropiado socialmente'], [3,'Algo apropiado socialmente'], [4,'Muy apropiado socialmente']],
        label=label,
        widget=widgets.RadioSelect
    )


def SDO_make_field(label):
    return models.StringField(
        choices=[[1, '1. Fuertemente en contra'], [2, '2. Algo en contra'], [3,'3.Ligeramente en contra'], [4,'4. neutral'],
        [5,'5. Ligeramente a favor'], [6,'6. Algo a favor'], [7,'7. Fuertemente a favor']],
        label=label,
        widget=widgets.RadioSelect
    )

def SDO_make_inverted_field(label):
    return models.StringField(
        choices=[[7, '1. Fuertemente en contra'], [6, '2. Algo en contra'], [5,'3.Ligeramente en contra'], [4,'4. neutral'],
        [3,'5. Ligeramente a favor'], [2,'6. Algo a favor'], [1,'7.Fuertemente a favor']],
        label=label,
        widget=widgets.RadioSelect
    )


class C(BaseConstants):
    NAME_IN_URL = 'demograph_dominant'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    PAGO_BASE = 5000


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    age = models.IntegerField(label='¿Cuál es su edad?', min=18, max=125)
    gender = models.StringField( 
        choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'],['Otro','Otro']],
        label='¿Cuál es su género?',
        widget=widgets.RadioSelect)
    income = models.StringField(choices =[[1, "$0 a $150.0000"], [2, "$151.000 a $270.000"], [3, "$271.000 a $460.000"], [4, "$461.000 a $810.000"],
    [5, "$811.000 a 1.4 Millones"],[6, "1.5 Millones a 2.4 Millones"],[7, "2.5 Millones o más"]],
    label="¿Cuál es el ingreso familiar de su hogar?", widget=widgets.RadioSelect)
    educacion = models.StringField(choices=[[0, 'Sin estudios formales'], [1, 'Básica completa'], [2, 'Media Completa'],
    [3, 'Educación superior técnica o universidaria completa'],[4, 'Postgrado completo']],
    label = 'Con respecto al jefe de su hogar: ¿Cuál es el mayor nivel educacional completado?', widget= widgets.RadioSelect)
    SDO7_1=SDO_make_field('Algunos grupos de personas deben ser forzados a quedarse en su lugar')
    SDO7_2=SDO_make_field('Está bien que ciertos grupos estén arriba y otros grupos estén abajo')
    SDO7_3=SDO_make_field('En una sociedad ideal algunos grupos deben estar arriba y otros gruposdeben estar abajo')
    SDO7_4=SDO_make_field('Algunos grupos de personas son simplemente inferiores a otros grupos')
    SDO7_5=SDO_make_inverted_field('Los grupos que están abajo en la sociedad merecen tener lo mismo que los grupos que están arriba')
    SDO7_6=SDO_make_inverted_field('Ningún grupo debiera dominar en la sociedad')
    SDO7_7=SDO_make_inverted_field('Los grupos que están abajo no debieran ser forzados a mantenerse en su posición')
    SDO7_8=SDO_make_inverted_field('Que algunos grupos dominen por sobre otros es poco ético')
    SDO7_9=SDO_make_field('No debiéramos defender la igualdad entre distintos grupos')
    SDO7_10=SDO_make_field('No debiéramos tratar de garantizar que todos los grupos tengan la misma calidad de vida')
    SDO7_11=SDO_make_field('Es injusto intentar que haya igualdad entre todos los grupos')
    SDO7_12=SDO_make_field('La igualdad entre grupos no debiera ser nuestro objetivo principal')
    SDO7_13=SDO_make_inverted_field('Debiéramos trabajar para que todos los grupos tengan la misma oportunidad de éxito en la sociedad')
    SDO7_14=SDO_make_inverted_field('Debiéramos hacer todo lo posible por igualar las condiciones de diferentes grupos')
    SDO7_15=SDO_make_inverted_field('Sin importar qué tan difícil sea, debiéramos esforzarnos por asegurar que todos los grupos tengan la misma oportunidad en la vida')
    SDO7_16=SDO_make_inverted_field('La igualdad entre los grupos debiera ser nuestro ideal')
    interes = models.StringField(choices=[[5, 'Muy interesado'], [4, 'Bastante interesado'], [3, 'Algo interesado'], [2, 'No muy interesado'], [1, 'Nada interesado']],
    widget=widgets.RadioSelect, label="")
    ideologia=models.StringField(label="Habitualmente la gente se identifica como 'izquierda', 'derecha' o 'centro' para explicar su ideología política. indique cuál es su ideología siendo 1 'Muy de izquierda' y 10 'muy de derecha'",
    choices=[[1, '1.Muy de izquierda'],[2, '2'],[3,'3'],[4,'4'],[5,'Centro'],[6,'6'],[7,'7'],[8,'8'],[9,'9'],[10,'10 Muy de derecha'],[0, 'Sin ideología']],
    widget=widgets.RadioSelect)
    comentario_lider = models.LongStringField(label= "Señale qué sentimientos y/o pensamientos le inspira su líder durante el juego", blank=True)
    comentario_otro = models.LongStringField(label="Señale qué sentimientos y/o pensamientos le inspira la pareja con la que Ud. jugó", blank=True)
    comentarios = models.LongStringField(label="Si tiene algún comentario o pensamiento sobre este experimento, puede escribirlo aquí", blank=True)
    beliefs_final1 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir 0")
    beliefs_final2 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 100 y 1000")
    beliefs_final3 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 1100 y 2000")
    beliefs_final4 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 2100 y 3000")
    beliefs_final5 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 3100 y 4000")
    beliefs_final6 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 4100 y 5000")
    beliefs_final7 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 5100 y 6000")
    beliefs_final8 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 6100 y 7000")
    beliefs_count = models.IntegerField(initial=0, min=0, max=4)
    data = models.StringField()
    reelection = models.StringField(choices=[[1, 'Sí'], [0, 'No']])
    norms_elicitation3_1 = make_field('Destruir $0')
    norms_elicitation3_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation3_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation3_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation3_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation3_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation3_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation3_8 = make_field('Destruir entre 6100 y 7000')
    acierto_norma3_1 = models.IntegerField()
    acierto_norma3_2 = models.IntegerField()
    acierto_norma3_3 = models.IntegerField()
    acierto_norma3_4 = models.IntegerField()
    acierto_norma3_5 = models.IntegerField()
    acierto_norma3_6 = models.IntegerField()
    acierto_norma3_7 = models.IntegerField()
    acierto_norma3_8 = models.IntegerField()
    random_JODPago = models.IntegerField(blank=True, null=True)
    random_norms = models.IntegerField(blank=True, null=True)
    area_estudio = models.StringField(choices=[['Arquitectura y Arte','Arquitectura y Arte'],['Comunicaciones', 'Comunicaciones'],
    ['Ciencias de la salud', 'Ciencias de la salud'],['Derecho','Derecho'],['Diseño','Diseño'],
    ['Economía y Negocios','Economía y Negocios'], ['Educación','Educación'],['Gobierno','Gobierno'],['Ingeniería','Ingeniería'],
    ['Psicología','Psicología']])
    
# FUNCTIONS


# PAGES

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class Demographics2(Page):
    form_model = 'player'
    form_fields = ['income', 'educacion']
 
class BFI2_XS(Page):
    form_model = 'player'
    form_fields= [f'BFI2_XS_{i}' for i in range (1, 16)]  

class SDO7_1(Page):
    form_model = 'player'
    form_fields = [f'SDO7_{i}' for i in range (1,9)]

class SDO7_2(Page):
    form_model = 'player'
    form_fields = [f'SDO7_{i}' for i in range (9,17)]


class interest(Page):
    form_model = 'player'
    form_fields = ['interes']


class politics(Page):
    form_model = 'player'
    form_fields = ['ideologia']

class comentario(Page):
    form_model = 'player'
    form_fields = ['comentario_lider', 'comentario_otro','comentarios']

class relection(Page):
    form_model = 'player'
    form_fields = ['reelection']


class norms_elicitation_final(Page):
    form_model = 'player'
    form_fields= ['norms_elicitation3_1', 'norms_elicitation3_2', 'norms_elicitation3_3','norms_elicitation3_3','norms_elicitation3_4',
    'norms_elicitation3_4', 'norms_elicitation3_5', 'norms_elicitation3_6','norms_elicitation3_7','norms_elicitation3_8']


class beliefs_final(Page):
    form_model = 'player'
    form_fields=['beliefs_final1','beliefs_final2','beliefs_final3','beliefs_final4','beliefs_final5','beliefs_final6','beliefs_final7','beliefs_final8']

    @staticmethod
    def error_message(player, values):
        total = sum([
            int(values['beliefs_final1']), int(values['beliefs_final2']), int(values['beliefs_final3']), int(values['beliefs_final4']),
            int(values['beliefs_final5']), int(values['beliefs_final6']), int(values['beliefs_final7']), int(values['beliefs_final8'])
        ])
        if total != 3:
            return 'El número total debe ser 3. No debes contarte a ti'

       
class final(Page):
    pass

class reelection(Page):
    form_model = 'player'
    form_fields = ['reelection']
    

class CalcularPagos(WaitPage):
    wait_for_all_groups = True  # Esto asegura que todos los jugadores esperen antes de proceder

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        # Recorre todos los jugadores de la sesión
        for player in subsession.get_players():
            # Aquí realizamos el cálculo de los pagos
            acierto_norms = []
            JOD_PagoFinal = []

            # 1. Crear la lista de aciertos de normas
            for round_num in range(1, 4):  # Para las tres rondas
                for i in range(1, 9):  # Para cada pregunta de la ronda
                    acierto_norma = getattr(player.participant, f'acierto_norma{round_num}_{i}', None)
                    if acierto_norma is not None:
                        acierto_norms.append(acierto_norma)

            # 2. Crear la lista de JOD_PagoFinal
            for round_num in range(1, 13):  # Para las 12 rondas
                endownment_final_value = getattr(player.participant, f'endownment_final{round_num}', None)
                if endownment_final_value is not None:
                    JOD_PagoFinal.append(endownment_final_value)

            # 3. Escoger aleatoriamente un valor de las dos listas
            random_norms = random.choice(acierto_norms) if acierto_norms else 0
            random_JODPago = random.choice(JOD_PagoFinal) if JOD_PagoFinal else 0

            # 4. Escoger aleatoriamente entre random_norms y random_JODPago
            Pago_random = random.choice([random_norms, random_JODPago])

            # 5. Calcular el pago final
            if Pago_random == random_norms:
                if random_norms == 1:
                    player.payoff = C.PAGO_BASE + 7000  # Si es un acierto en normas
                else:
                    player.payoff = C.PAGO_BASE  # Si falló en las normas
            else:
                player.payoff = C.PAGO_BASE + random_JODPago  # Si viene del endownment final

            # Debug para asegurarte de que todo funciona
            print(f"Pago calculado para el jugador {player.id_in_group}: {player.payoff}")

class Pregunta_Facultad(Page):
    form_model = 'player'
    form_fields = ['area_estudio']



page_sequence = [beliefs_final,CalcularPagos, Demographics, Demographics2,Pregunta_Facultad, SDO7_1, SDO7_2, interest, politics, reelection, comentario, final] 



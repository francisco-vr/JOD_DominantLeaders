from otree.api import *
from collections import defaultdict


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

def BFI2_XS_make_field(label):
    return models.StringField(
        choices=[[1, '1. Muy en desacuerdo'], [2, '2. Algo en desacuerdo'], [3,'3.Neutral, sin opinión'], [4,'4. Algo de acuerdo'],
        [5,'5. Muy de acuerdo']],
        label=label,
        widget=widgets.RadioSelect
        
    )

def BFI2_XS_inverted_field(label):
    return models.StringField(
        choices=[[5, '1. Muy en desacuerdo'], [4, '2. Algo en desacuerdo'], [3,'3.Neutral, sin opinión'], [2,'4. Algo de acuerdo'],
        [1,'5. Muy de acuerdo']],
        label=label,
        widget=widgets.RadioSelect
    )



class C(BaseConstants):
    NAME_IN_URL = 'demograph'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    age = models.IntegerField(label='¿Cuál es su edad?', min=18, max=125)
    gender = models.StringField( 
        choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'],['Otro','Otro']],
        label='Cuál es su género?',
        widget=widgets.RadioSelect)
    income = models.StringField(choices =[[1, "menos de "], [2, "entre y "], [3, "entre y "], [4, "bla"], [5, "bla bla"]],
    label="Cuál es el ingreso familiar de su hogar?", widget=widgets.RadioSelect)
    educacion = models.StringField(choices=[[0, 'Sin estudios formales'], [1, 'Básica incompleta'], [2, 'Básica Completa'], [4, 'Media completa'],
    [5, 'Educación superior técnica o universitaria incompleta'], [6, 'Educación superior técnica o universidaria completa'], [7, 'Postgrado incompleto'],
    [8, 'Postgrado completo']],
    label = '¿Cuál es el mayor nivel educacional completado por el jefe de hogar?', widget= widgets.RadioSelect)
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
    BFI2_XS_1=BFI2_XS_make_field('Compasivo/a, con un gran corazón')
    BFI2_XS_2=BFI2_XS_inverted_field('Relajado/a, que gestiona bien el estrés')
    BFI2_XS_3=BFI2_XS_make_field('Respetuoso/a, que trata a los demàs con respeto')
    BFI2_XS_4=BFI2_XS_make_field('Formal, constante')
    BFI2_XS_5=BFI2_XS_inverted_field('Que tiende a estar callado')
    BFI2_XS_6=BFI2_XS_make_field('Fascinado/a por el arte, la música o la literatura')
    BFI2_XS_7=BFI2_XS_make_field('Dominante, que actúa como líder')
    BFI2_XS_8=BFI2_XS_inverted_field('Emocionalmente estable, que no se altera con facilidad')
    BFI2_XS_9=BFI2_XS_make_field('Que mantiene todo limpio y ordenado')
    BFI2_XS_10=BFI2_XS_make_field('Lleno/a de energía')
    BFI2_XS_11=BFI2_XS_make_field('Tenaz, que trabaja hasta terminar la tarea')
    BFI2_XS_12=BFI2_XS_make_field('Que tiende a sentirse deprimido/a, melancólico/a')
    BFI2_XS_13=BFI2_XS_inverted_field('Con poco interés por ideas abstractas')
    BFI2_XS_14=BFI2_XS_make_field('Que piensa bien de la gente')
    BFI2_XS_15=BFI2_XS_make_field('Original, que aporta ideas nuevas')
    interes = models.StringField(choices=[[5, 'Muy interesado'], [4, 'Bastante interesado'], [3, 'Algo interesado'], [2, 'No muy interesado'], [1, 'Nada interesado']],
    label="¿Cuán interesado está en entender temas de política actual?", widget=widgets.RadioSelect)
    ideologia=models.StringField(label="Habitualmente la gente se identifica como 'izquierda', 'derecha' o 'centro' para explicar su ideología política. indique cuál es su ideología siendo 1 'Muy de izquierda' y 10 'muy de derecha'",
    choices=[[1, '1.Muy de izquierda'],[2, '2'],[3,'3'],[4,'4'],[5,'Centro'],[6,'6'],[7,'7'],[8,'8'],[9,'9'],[10,'10 Muy de derecha'],[0, 'Sin ideología']],
    widget=widgets.RadioSelect)
    comentarios = models.StringField(label="Si tiene algún comentario o pensamiento sobre este experimento, puede escribirlo aquí")

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

class SDO7(Page):
    form_model = 'player'
    form_fields = [f'SDO7_{i}' for i in range (1,17)]

class politics(Page):
    form_model = 'player'
    form_fields = ['interes', 'ideologia']

class comentario(Page):
    form_model = 'player'
    form_fields = ['comentarios']





page_sequence = [Demographics, Demographics2, SDO7, politics, BFI2_XS, comentario] 

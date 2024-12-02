from otree.api import *
from collections import defaultdict
import random
import json
from statistics import mode, StatisticsError

def make_field(label):
    return models.StringField(
        choices=[[1, 'Muy inapropiado socialmente'], [2, 'Algo inapropiado socialmente'], [3,'Algo apropiado socialmente'], [4,'Muy apropiado socialmente']],
        label=label,
        widget=widgets.RadioSelect
    )


class C(BaseConstants):
    NAME_IN_URL = 'JOD_MESSAGE'
    PLAYERS_PER_GROUP = 4 
    NUM_ROUNDS = 12
    PASSWORD = 'LEMCICS'


class Subsession(BaseSubsession):
    promedio_grupoklee = models.FloatField()
    promedio_grupokandinski = models.FloatField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    evaluacion = models.StringField(choices=[[1,'Muy desagradable'],[2 , 'Desagradable'], [3, 'ni agradable ni desagradable'], [4, 'Agradable'], [5, 'Muy Agradable']],
    label= '¿Cómo calificas esta imagen?', widget=widgets.RadioSelect)
    punished_player_id = models.IntegerField(initial=None, blank=True, null=True)
    endownment = models.IntegerField(initial=7000, max = 7000)
    agression = models.IntegerField(initial=0, min=0, max= 7000)
    agression_lider = models.IntegerField()
    endownment_final = models.IntegerField()
    agresion_guardada = models.IntegerField()
    leader_message = models.StringField( 
        choices=[['No le destruyas dinero', 'No le destruyas dinero'],
        ['Debes destruirle la mitad del dinero', 'Debes destruirle la mitad del dinero'],
        ['Debes destruirle todo el dinero', 'Debes destruirle todo el dinero'],
        ['Puedes hacer lo que prefieras','Puedes hacer lo que prefieras'],
        ['Sugiero destruirle la mitad del dinero', 'Sugiero destruirle la mitad del dinero'],
        ['Sugiero destruirle todo el dinero', 'Sugiero destruirle todo el dinero'],
        ['Sugiero destruirle $1.000', 'Sugiero destruirle $1.000'],
        ['Debes destruirle $1.000','Debes destruirle $1.000'],
        ['Sugiero destruirle $2.000', 'Sugiero destruirle $2.000'],
        ['Debes destruirle $2.000', 'Debes destruirle $2.000']],label='¿Cuál mensaje les enviarás a tus seguidores?',
        widget=widgets.RadioSelect, blank=True)
    norms_elicitation1_1 = make_field('Destruir $0')
    norms_elicitation1_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation1_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation1_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation1_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation1_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation1_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation1_8 = make_field('Destruir entre 6100 y 7000')
    norms_elicitation2_1 = make_field('Destruir $0')
    norms_elicitation2_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation2_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation2_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation2_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation2_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation2_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation2_8 = make_field('Destruir entre 6100 y 7000')
    norms_elicitation3_1 = make_field('Destruir $0')
    norms_elicitation3_2 = make_field('Destruir entre 100 y 1000')
    norms_elicitation3_3 = make_field('Destruir entre 1100 y 2000')
    norms_elicitation3_4 = make_field('Destruir entre 2100 y 3000')
    norms_elicitation3_5 = make_field('Destruir entre 3100 y 4000')
    norms_elicitation3_6 = make_field('Destruir entre 4100 y 5000')
    norms_elicitation3_7 = make_field('Destruir entre 5100 y 6000')
    norms_elicitation3_8 = make_field('Destruir entre 6100 y 7000')
    beliefs_1 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir 0")
    beliefs_2 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 100 y 1000")
    beliefs_3 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 1100 y 2000")
    beliefs_4 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 2100 y 3000")
    beliefs_5 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 3100 y 4000")
    beliefs_6 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 4100 y 5000")
    beliefs_7 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 5100 y 6000")
    beliefs_8 = models.StringField(choices=[[0,'0'],[1,'1'],[2,'2'],[3,'3'],[4,'4']],label="Destruir entre 6100 y 7000")
    beliefs_count = models.IntegerField(initial=0, min=0, max=4)
    data = models.StringField()
    promedio_grupokandinski = models.IntegerField()
    promedio_grupoklee = models.IntegerField()
    prueba1 = make_field(label='Llevarse la billetera')
    prueba2 = make_field(label='Preguntas a otras personas cerca si la billetera les pertenece')
    prueba3 = make_field(label='Dejar la biletera donde está')
    prueba4 = make_field(label='Entregar la billetera al gerente del café')
    comprension1 = models.StringField(choices=[[1,'$0'], [0, '$3.000'], [0, '$5.000'], [0, '$7.000'], [0,'$2.000']], widget=widgets.RadioSelect, blank=True, label=' ')
    comprension2 = models.StringField(choices=[[0,'Muy socialmente inapropiado'],[1, 'Algo socialmente inapropiado'], [0, 'Algo socialmente apropiado'],
    [0, 'Muy socialmente apropiado'], [0, 'Ninguna de las anteriores']],
    label=' ', widget=widgets.RadioSelect)
    intentos_fallidos1 = models.IntegerField(initial=0)
    password_input1 = models.StringField(blank=True, initial="", label="Contraseña")
    intentos_fallidos2 = models.IntegerField(initial=0)
    password_input2 = models.StringField(blank=True, initial="", label="Contraseña")
    promedio_grupal = models.IntegerField()
    intentos_fallidos = models.IntegerField(initial=0)
    password_input = models.StringField(blank=True)
    comprension3 = models.StringField(choices=[[0,'$0'], [0, '$60.000'], [0, '$12.000'], [1, '$5.000'], [0,'Ninguna de las anteriores']], widget=widgets.RadioSelect, blank=True, label=' ')
    comprension4 = models.StringField(choices=[[0,'$0'], [0, '$3.500'], [0, '$5.000'], [0, '$7.000'], [1,'$11.000']], widget=widgets.RadioSelect, blank=True, label=' ')
    intentos_fallidos3 = models.IntegerField(initial=0)
    password_input3 = models.StringField(blank=True, initial="", label="Contraseña")
    intentos_fallidos4 = models.IntegerField(initial=0)
    password_input4 = models.StringField(blank=True, initial="", label="Contraseña")
    moda_norms = models.IntegerField()
    acierto_norma1_1 = models.IntegerField()
    acierto_norma1_2 = models.IntegerField()
    acierto_norma1_3 = models.IntegerField()
    acierto_norma1_4 = models.IntegerField()
    acierto_norma1_5 = models.IntegerField()
    acierto_norma1_6 = models.IntegerField()
    acierto_norma1_7 = models.IntegerField()
    acierto_norma1_8 = models.IntegerField()
    acierto_norma2_1 = models.IntegerField()
    acierto_norma2_2 = models.IntegerField()
    acierto_norma2_3 = models.IntegerField()
    acierto_norma2_4 = models.IntegerField()
    acierto_norma2_5 = models.IntegerField()
    acierto_norma2_6 = models.IntegerField()
    acierto_norma2_7 = models.IntegerField()
    acierto_norma2_8 = models.IntegerField()
    acierto_norma3_1 = models.IntegerField()
    acierto_norma3_2 = models.IntegerField()
    acierto_norma3_3 = models.IntegerField()
    acierto_norma3_4 = models.IntegerField()
    acierto_norma3_5 = models.IntegerField()
    acierto_norma3_6 = models.IntegerField()
    acierto_norma3_7 = models.IntegerField()
    acierto_norma3_8 = models.IntegerField()
    endownment_final1 = models.IntegerField(blank=True, null=True)
    endownment_final2 = models.IntegerField(blank=True, null=True)
    endownment_final3 = models.IntegerField(blank=True, null=True)
    endownment_final4 = models.IntegerField(blank=True, null=True)
    endownment_final5 = models.IntegerField(blank=True, null=True)
    endownment_final6 = models.IntegerField(blank=True, null=True)
    endownment_final7 = models.IntegerField(blank=True, null=True)
    endownment_final8 = models.IntegerField(blank=True, null=True)
    endownment_final9 = models.IntegerField(blank=True, null=True)
    endownment_final10 = models.IntegerField(blank=True, null=True)
    endownment_final11 = models.IntegerField(blank=True, null=True)
    endownment_final12 = models.IntegerField(blank=True, null=True)


# FUNCTIONS

def calculate_group_mode_and_accuracy_all(player: Player, round_number: int):
    """
    Calcula la moda y los aciertos para un conjunto de normas elicitadas y los guarda en player.participant.
    - round_number: 1 para norms_elicitation1, 2 para norms_elicitation2, 3 para norms_elicitation3.
    """
    session_players = player.subsession.get_players()  # Obtén todos los jugadores de la sesión.

    # Filtrar los jugadores por grupo Klee y Kandinski
    klee_players = [p for p in session_players if p.participant.group_artist == 'grupo_klee']
    kandinski_players = [p for p in session_players if p.participant.group_artist == 'grupo_kandinski']

    field_prefix = f'norms_elicitation{round_number}_'

    for i in range(1, 9):
        klee_values = []
        kandinski_values = []

        # Recolectar respuestas de los jugadores del grupo Klee
        for p in klee_players:
            response = getattr(p, f'{field_prefix}{i}')
            if response is not None:
                klee_values.append(int(response))  # Convertir respuesta a int

        # Recolectar respuestas de los jugadores del grupo Kandinski
        for p in kandinski_players:
            response = getattr(p, f'{field_prefix}{i}')
            if response is not None:
                kandinski_values.append(int(response))

        # Calcular la moda para cada grupo (Klee y Kandinski)
        try:
            moda_klee = mode(klee_values) if klee_values else None
        except StatisticsError:
            moda_klee = None

        try:
            moda_kandinski = mode(kandinski_values) if kandinski_values else None
        except StatisticsError:
            moda_kandinski = None

        # Comparar las respuestas con la moda y actualizar los aciertos
        for p in session_players:
            player_response = int(getattr(p, f'{field_prefix}{i}'))
            if p.participant.group_artist == 'grupo_klee':
                if moda_klee is not None and player_response == moda_klee:
                    setattr(p, f'acierto_norma{round_number}_{i}', 1)
                else:
                    setattr(p, f'acierto_norma{round_number}_{i}', 0)
            elif p.participant.group_artist == 'grupo_kandinski':
                if moda_kandinski is not None and player_response == moda_kandinski:
                    setattr(p, f'acierto_norma{round_number}_{i}', 1)
                else:
                    setattr(p, f'acierto_norma{round_number}_{i}', 0)

            # Guardar los aciertos en participant
            setattr(p.participant, f'acierto_norma{round_number}_{i}', getattr(p, f'acierto_norma{round_number}_{i}'))



# PAGES
class pagina_cero(Page):
    pass


class ShuffleWaitPage2(WaitPage):
    
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):

        range_lista = [[] for _ in range(subsession.session.num_participants)]
    

        estructura = subsession.get_group_matrix(range_lista)

        # Identificación de los líderes de cada grupo
        leaders_pair = [None, None]

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_klee" and player.participant.group_role == "lider":
                    leaders_pair[0] = player.participant.id_in_session
                    break

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_kandinski" and player.participant.group_role == "lider":
                    leaders_pair[1] = player.participant.id_in_session
                    break

        print("La lista de pares de líderes es: ", leaders_pair)

        # Crear listas vacías para los seguidores de cada grupo
        group1_seguidores = []  # Seguidores de grupo_klee
        group2_seguidores = []  # Seguidores de grupo_kandinski

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_klee" and player.participant.group_role == "seguidor":
                    group1_seguidores.append(player.participant.id_in_session)

        for row in estructura:
            for player in row:
                if player.participant.group_artist == "grupo_kandinski" and player.participant.group_role == "seguidor":
                    group2_seguidores.append(player.participant.id_in_session)

   
        # Asegúrate de tener suficientes seguidores en cada grupo para formar 3 parejas
        assert len(group1_seguidores) >= 3, "No hay suficientes seguidores en grupo 1 para formar 3 parejas."
        assert len(group2_seguidores) >= 3, "No hay suficientes seguidores en grupo 2 para formar 3 parejas."

        # Seleccionar aleatoriamente seguidores de cada grupo
        follower1 = random.choice(group1_seguidores)
        follower2 = random.choice(group2_seguidores)

        follower3 = random.choice([f for f in group1_seguidores if f != follower1])
        follower4 = random.choice([f for f in group2_seguidores if f != follower2])

        follower5 = random.choice([f for f in group1_seguidores if f not in [follower1, follower3]])
        follower6 = random.choice([f for f in group2_seguidores if f not in [follower2, follower4]])

        # Emparejar los seguidores
        pairs_followers1 = [follower1, follower2]  # Primera pareja
        pairs_followers2 = [follower3, follower4]  # Segunda pareja
        pairs_followers3 = [follower5, follower6]   # Tercera pareja
        



        # Nueva matriz de grupos
        new_group_matrix = [leaders_pair, pairs_followers1, pairs_followers2, pairs_followers3]

        # Asignar la nueva matriz de grupos
        subsession.set_group_matrix(new_group_matrix)


class protocolo(Page):
    form_model = 'player'

    def is_displayed(player:Player):
        return player.round_number == 1

class instruccion_elicitation(Page):
    
    def is_displayed(player:Player):
        return player.round_number == 1 

class norms_elicitation1(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation1_1', 'norms_elicitation1_2', 'norms_elicitation1_3',
                   'norms_elicitation1_4', 'norms_elicitation1_5', 'norms_elicitation1_6', 
                   'norms_elicitation1_7', 'norms_elicitation1_8']

    def is_displayed(player: Player):
        return player.round_number == 1


class calculo_moda(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        round_number = subsession.round_number  # Obtenemos la ronda actual de la subsession
        print(f"Calculando modas para la ronda {round_number}")

        for group in subsession.get_groups():
            for player in group.get_players():
                # Usar 1 para la ronda 1, 2 para la ronda 7 y 3 para la ronda 12
                if player.round_number == 1:
                    calculate_group_mode_and_accuracy_all(player, 1)
                elif player.round_number == 7:
                    calculate_group_mode_and_accuracy_all(player, 2)
                elif player.round_number == 12:
                    calculate_group_mode_and_accuracy_all(player, 3)
                else:
                    print(f"Ronda desconocida: {player.round_number}")





class norms_elicitation2(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation2_1', 'norms_elicitation2_2', 'norms_elicitation2_3',
                   'norms_elicitation2_4', 'norms_elicitation2_5', 'norms_elicitation2_6', 
                   'norms_elicitation2_7', 'norms_elicitation2_8']

    def is_displayed(player: Player):
        return player.round_number == 7

   
class norms_elicitation3(Page):
    form_model = 'player'
    form_fields = ['norms_elicitation3_1', 'norms_elicitation3_2', 'norms_elicitation3_3',
                   'norms_elicitation3_4', 'norms_elicitation3_5', 'norms_elicitation3_6', 
                   'norms_elicitation3_7', 'norms_elicitation3_8']

    def is_displayed(player: Player):
        return player.round_number == 12

   

class elicitacion_prueba(Page):
    
    def is_displayed(player:Player):
        return player.round_number == 1


class tabla_prueba_norms(Page):
    form_model = 'player'
    form_fields = ['prueba1', 'prueba2', 'prueba3', 'prueba4']

    def is_displayed(player:Player):
        return player.round_number == 1


class tabla_norms(Page):
    form_model = 'player'
    form_fields= ['norms_elicitation1_1', 'norms_elicitation1_2', 'norms_elicitation1_3','norms_elicitation1_4','norms_elicitation1_5',
    'norms_elicitation1_6', 'norms_elicitation1_7', 'norms_elicitation1_8']

    def is_displayed(player:Player):
        return player.round_number == 1

    @staticmethod
    def after_all_players_arrive():
        for player in subsession.get_players():
            # Iterar sobre los campos de norms_elicitation
            for i in range(1, 9):
                field_name = f'norms_elicitation1_{i}'
                # Obtener el valor del campo en el jugador
                field_value = getattr(player, field_name)
                # Asignar ese valor al participante
                setattr(player.participant, field_name, field_value)


class comprension1(Page):
    form_model = 'player'
    form_fields = ['comprension1', 'password_input1']

    def is_displayed(player:Player):
        return player.round_number == 1

    """
    @staticmethod
    def error_message(player: Player, values):
        respuesta = int(values['comprension1'])
        pswd = values['password_input1']
        print("respuesta: " + str(respuesta))
        print("intentos: " + str(player.intentos_fallidos1))
        print("pasword:" + pswd)
        if respuesta != 1 and player.intentos_fallidos1 < 2:
            player.intentos_fallidos1 += 1
            if player.intentos_fallidos1 <= 3:
                return 'Incorrecto. <br> No lo olvide, únicamente la respuesta seleccionada por la mayoría de las personas de tu grupo recibirá el pago adicional.'
            else:
                return 'Por favor levante su mano y espere a que el experimento continúe.'
        elif respuesta != 1 and player.intentos_fallidos1 == 2 and pswd != C.PASSWORD:
            return 'Ingrese la contraseña correcta'
        else:
            player.comprension1 = "1"
    """

    @staticmethod
    def error_message(player: Player, values):
        pswd = values['password_input1']

        # Caso especial: intentos fallidos >= 2, solo validar la contraseña
        if player.intentos_fallidos1 >= 2:
            if not pswd:
                return "Debes ingresar la contraseña para continuar."
            if pswd != C.PASSWORD:
                return "La contraseña ingresada es incorrecta."
            return None  # Contraseña válida, permitir avanzar

        # Caso general: validar 'comprension1'
        if values['comprension1'] is None:
            return "Debes responder esta pregunta antes de continuar."

        # Convertir respuesta a entero y validar
        respuesta = int(values['comprension1'])
        if respuesta != 1 and player.intentos_fallidos1 < 2:
            player.intentos_fallidos1 += 1
            return 'Incorrecto. <br> No lo olvide, únicamente la respuesta seleccionada por la mayoría de las personas de tu grupo recibirá el pago adicional.'
        elif respuesta == 1:
            player.comprension1 = "1"  # Marcar respuesta como correcta
            return None


class feedback1(Page):

    def is_displayed(player:Player):
        return player.round_number == 1

class comprension2(Page):
    form_model = 'player'
    form_fields = ['comprension2', 'password_input2']

    def is_displayed(player:Player):
        return player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        pswd = values['password_input2']

        # Caso especial: intentos fallidos >= 2, solo validar la contraseña
        if player.intentos_fallidos2 >= 2:
            if not pswd:
                return "Debes ingresar la contraseña para continuar."
            if pswd != C.PASSWORD:
                return "La contraseña ingresada es incorrecta."
            return None  # Contraseña válida, permitir avanzar

        # Caso general: validar 'comprension1'
        if values['comprension2'] is None:
            return "Debes responder esta pregunta antes de continuar."

        # Convertir respuesta a entero y validar
        respuesta = int(values['comprension2'])
        if respuesta != 1 and player.intentos_fallidos2 < 2:
            player.intentos_fallidos2 += 1
            return 'Incorrecto. <br> No lo olvide, únicamente la respuesta seleccionada por la mayoría de las personas de tu grupo recibirá el pago adicional.'
        elif respuesta == 1:
            player.comprension2 = "1"  # Marcar respuesta como correcta
            return None

class feedback2(Page):
    def is_displayed(player:Player):
        return player.round_number == 1


class comprension4(Page):
    form_model = 'player'
    form_fields = ['comprension4', 'password_input4']

    def is_displayed(player:Player):
        return player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        pswd = values['password_input4']

        # Caso especial: intentos fallidos >= 2, solo validar la contraseña
        if player.intentos_fallidos4 >= 2:
            if not pswd:
                return "Debes ingresar la contraseña para continuar."
            if pswd != C.PASSWORD:
                return "La contraseña ingresada es incorrecta."
            return None  # Contraseña válida, permitir avanzar

        # Caso general: validar 'comprension1'
        if values['comprension4'] is None:
            return "Debes responder esta pregunta antes de continuar."

        # Convertir respuesta a entero y validar
        respuesta = int(values['comprension4'])
        if respuesta != 1 and player.intentos_fallidos4 < 2:
            player.intentos_fallidos4 += 1
            return 'Incorrecto. <br> No lo olvide: El pago final total es el pago base, sumado al dinero que queda después de lo destruído po su pareja de juego'
        elif respuesta == 1:
            player.comprension4 = "1"  # Marcar respuesta como correcta
            return None

class feedback3(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class comprension3(Page):
    form_model = 'player'
    form_fields = ['comprension3', 'password_input3']

    def is_displayed(player:Player):
        return player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        pswd = values['password_input3']

        # Caso especial: intentos fallidos >= 2, solo validar la contraseña
        if player.intentos_fallidos3 >= 2:
            if not pswd:
                return "Debes ingresar la contraseña para continuar."
            if pswd != C.PASSWORD:
                return "La contraseña ingresada es incorrecta."
            return None  # Contraseña válida, permitir avanzar

        # Caso general: validar 'comprension1'
        if values['comprension3'] is None:
            return "Debes responder esta pregunta antes de continuar."

        # Convertir respuesta a entero y validar
        respuesta = int(values['comprension3'])
        if respuesta != 1 and player.intentos_fallidos3 < 2:
            player.intentos_fallidos3 += 1
            return 'Incorrecto. <br> No lo olvide: sólo una ronda elegida al azar será pagada.'
        elif respuesta == 1:
            player.comprension3 = "1"  # Marcar respuesta como correcta
            return None

class feedback4(Page):
    def is_displayed(player:Player):
        return player.round_number == 1 and player.intentos_fallidos4 <= 1


class beliefs(Page):
    form_model = 'player'
    form_fields=['beliefs_1','beliefs_2','beliefs_3','beliefs_4','beliefs_5','beliefs_6','beliefs_7','beliefs_8']

    @staticmethod
    def error_message(player, values):
        total = sum([
            int(values['beliefs_1']), int(values['beliefs_2']), int(values['beliefs_3']), int(values['beliefs_4']),
            int(values['beliefs_5']), int(values['beliefs_6']), int(values['beliefs_7']), int(values['beliefs_8'])
        ])
        if total != 3:
            return 'El número total debe ser 3. No debes contarte a ti'

    def is_displayed(player:Player):
        return player.round_number == 1 or player.round_number == 7 


class espera(WaitPage):
    wait_for_all_groups = True
    

class JOD_leader(Page):
    form_model = 'player'
    form_fields = ['agression', 'leader_message']

    @staticmethod
    def is_displayed(player:Player):
        return player.participant.group_role == 'lider'
    
    def before_next_page(player:Player, timeout_happened):
        seguidores = player.get_others_in_subsession()
        print("seguidores es: ", seguidores)
        print(player.leader_message)
        for p in seguidores:
            if p.participant.group_artist == player.participant.group_artist:
                p.leader_message = player.leader_message
                p.agression_lider = player.agression

    @staticmethod
    def error_message(player, values):
        if values['agression'] is None or values['agression'] == '':
            return 'Debes tomar ambas decisiones'

        if values['leader_message'] == '':
            return 'Debes tomar ambas decisiones'
    
        return None  # Si todo está correcto, no retornamos mensaje de error


    @staticmethod
    def vars_for_template(player: Player):
        # Obtén el promedio grupal según el grupo y la ronda
        if player.round_number >= 2:
            if player.participant.group_artist == "grupo_klee":
                promedio_grupal = player.subsession.in_round(player.round_number - 1).promedio_grupoklee            
            elif player.participant.group_artist == "grupo_kandinski":
                promedio_grupal = player.subsession.in_round(player.round_number - 1).promedio_grupokandinski
        else:
            promedio_grupal = None

        return dict(
            promedio_grupal=promedio_grupal,
            agression_p1=None,  # Inicializa las variables de agresión, que puedes actualizar después
            agression_p2=None,
            
        )




class endownment_final_lideres(WaitPage):
    def is_displayed(player: Player):
        return player.participant.group_role == 'lider'

    @staticmethod
    def after_all_players_arrive(group: Group):
        # Obtenemos la subsession a partir del grupo
        subsession = group.subsession
        
        # Obtener los jugadores por ID
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)


        # Calcular la agresión y el endowment final
        agression_p2 = p2.agression
        agression_p1 = p1.agression
        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final


        # Guardar el valor de endownment_final en la variable correspondiente según la ronda
        for i in range(1, 13):
            if p1.round_number == i:
                setattr(p1.participant, f'endownment_final{i}', p1.endownment_final)
                setattr(p2.participant, f'endownment_final{i}', p2.endownment_final)


    @staticmethod
    def vars_for_template(player: Player):
        # Retornar el valor de las agresiones para el template
        return dict(agression_p1=player.agression, agression_p2=player.agression)

class leader_results(Page):

    def is_displayed(player:Player):
        return player.participant.group_role == 'lider'
            


class followers_JOD(Page):
    form_model = 'player'
    form_fields = ['agression']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(leader_message=player.leader_message)


    def is_displayed(player:Player):
        return player.participant.group_role == 'seguidor'  
 

class endownment_final_seguidores(WaitPage):
    def is_displayed(player:Player):
        return player.participant.group_role == 'seguidor'

    @staticmethod
    def after_all_players_arrive(group:Group):

        subsession = group.subsession

        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)


        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final


         # Guardar el valor de endownment_final en la variable correspondiente según la ronda
        for i in range(1, 13):
            if p1.round_number == i:
                setattr(p1.participant, f'endownment_final{i}', p1.endownment_final)
                setattr(p2.participant, f'endownment_final{i}', p2.endownment_final)
  

class followers_JOD_results(Page):
    def is_displayed(player:Player):
        return player.participant.group_role == 'seguidor'

    @staticmethod
    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        agression_p2 = p2.aggression
        agression_p1 = p1.agression

        def vars_for_template(player:Player):
            return dict(agression_p1=agression_p1, agression_p2=agression_p2)

class CalcularPromedios(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        destruccion_seguidores_klee = []
        destruccion_seguidores_kandinski = []

        # Recorremos todos los jugadores para recolectar la agresión
        for p in subsession.get_players():
            if p.participant.group_artist == 'grupo_klee' and p.participant.group_role == 'seguidor':
                destruccion_seguidores_klee.append(p.agression)
            elif p.participant.group_artist == 'grupo_kandinski' and p.participant.group_role == 'seguidor':
                destruccion_seguidores_kandinski.append(p.agression)

        # Calculamos los promedios por grupo
        promedio_grupoklee = int(round(sum(destruccion_seguidores_klee) / len(destruccion_seguidores_klee))) if destruccion_seguidores_klee else 0
        promedio_grupokandinski = int(round(sum(destruccion_seguidores_kandinski) / len(destruccion_seguidores_kandinski))) if destruccion_seguidores_kandinski else 0

        # Guardamos los valores en la subsession para cada ronda
        subsession.promedio_grupoklee = promedio_grupoklee
        subsession.promedio_grupokandinski = promedio_grupokandinski

        
class ejemplo_lider(Page):
    def is_displayed(player:Player):
        return player.round_number == 1
              

class ejemplo_miembrogrupo(Page):
    def is_displayed(player:Player):
       return player.round_number == 1
              
   
class ejemplo_grupos(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class descripcion_pago(Page):
    def is_displayed(player:Player):
        return player.round_number == 1

class sistema_pagos(Page):
    def is_displayed(player:Player):
        return player.round_number == 1
              

page_sequence = [ShuffleWaitPage2, protocolo, ejemplo_grupos, descripcion_pago, ejemplo_lider, ejemplo_miembrogrupo, 
instruccion_elicitation, sistema_pagos, elicitacion_prueba, tabla_prueba_norms, comprension1, feedback1,
 comprension2, feedback2, comprension3, feedback3, comprension4, feedback4, espera, norms_elicitation1, 
 norms_elicitation2, espera, beliefs, espera, JOD_leader, espera,
endownment_final_lideres, leader_results, followers_JOD, CalcularPromedios, endownment_final_seguidores, 
followers_JOD_results, norms_elicitation3, calculo_moda] 

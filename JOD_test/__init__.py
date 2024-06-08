from otree.api import *
from collections import defaultdict
import random


class C(BaseConstants):
    NAME_IN_URL = 'JOD'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    roles = ['lider', 'seguidor'] # Roles estáticos posibles, quitar después de las pruebas

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    group_assignment = models.StringField(choices=['Grupo 1', 'Grupo 2'], default="")
    group_role = models.StringField(choices=['lider', 'seguidor'], default="")
    evaluacion = models.StringField(choices=[[1,'Muy desagradable'],[2 , 'Desagradable'], [3, 'ni agradable ni desagradable'], [4, 'Agradable'], [5, 'Muy Agradable']],
    label= '¿Cómo calificas esta imagen?', widget=widgets.RadioSelect)
    punished_player_id = models.IntegerField(initial=None, blank=True, null=True)
    endownment = models.IntegerField(initial=800, max = 800)
    agression = models.IntegerField(initial=0, max= 800, label= '¿Cuánto dinero le disminuiría al otro jugador?')
    agression_lider = models.IntegerField()
    endownment_final = models.IntegerField()
    agresion_guardada = models.IntegerField()
    leader_message = models.StringField( 
        choices=[['Quizás es una buena idea quemarles más dinero', 'Quizás es una buena idea quemarles más dinero'],
        ['Sugiero que le quememos más dinero', 'Sugiero que le quememos más dinero'],
        ['Quememosle más dinero', 'Quememosle más dinero'],
        ['Es importante que les quememos más dinero', 'Es importante que les quememos más dinero'],
        ['Les ordeno que les quemen más dinero!', 'Les ordeno que les quemen más dinero!']],
        label='¿Cuál mensaje les enviarás a tus seguidores?',
        widget=widgets.RadioSelect,
    )


#PAGES
class pagina_cero(Page):
    pass

class ShuffleWaitPage1(WaitPage):
    wait_for_all_groups = True
    
    @staticmethod
    def after_all_players_arrive(subsession: Subsession):
        print("el resultado de subsession.get_players() es: ", subsession.get_players())

        print("subsession.get_group_matrix()", subsession.get_group_matrix())
        grupos = subsession.get_groups()
        print('subsession.get_groups es: ', subsession.get_groups)
        for g in grupos:
            for player in g.get_players():
                if g.id_in_subsession==1:
                    player.group_assignment="Grupo 1"
                else:
                    player.group_assignment="Grupo 2"

        for group in subsession.get_groups():
            print("group.get_players() entrega lo siguiente: ", group.get_players())

            # Asignar roles a los jugadores en el grupo
            for i, player in enumerate(group.get_players()):  # Aquí corregimos para iterar sobre los jugadores
                if player.id_in_group == 1:
                    player.group_role = 'lider'
                elif player.id_in_group == 2:
                    player.group_role = 'seguidor'
            # Imprimir los roles asignados
            for player in group.get_players():  # También corregimos aquí para iterar sobre los jugadores
                print(player.group_role)



class ShuffleWaitPage2(WaitPage):
    
    wait_for_all_groups = True


    def after_all_players_arrive(subsession):

        print("subsession.session.num_participants es: ", subsession.session.num_participants)

        range_lista = [[] for _ in range(subsession.session.num_participants)]
    
        print("subsession.get_group_matrix() entrega: ", subsession.get_group_matrix())

        estructura = subsession.get_group_matrix(range_lista)
        print("El tipo de variable de get_group_matrix ex: ", type(estructura))

        leaders_pair = [None, None]

        for row in estructura:
            for player in row:
                if player.group_assignment=="Grupo 1" and player.group_role=="lider": #luego cambiar a player.Participant
                    leaders_pair[0] = player.participant.id_in_session
                    break


        for row in estructura:
            for player in row:
                if player.group_assignment=="Grupo 2" and player.group_role == "lider": #luego cambiar a player.Participant
                    leaders_pair[1] = player.participant.id_in_session
                    break

        print("la lista de pares de líderes es: ", leaders_pair)

        # Crear listas vacías para los dos casos
        group2_seguidores = []
        group1_seguidores = []

        for row in estructura:
            for player in row:
                if player.group_assignment == "Grupo 1" and player.group_role == "seguidor": #luego cambiar a player.Participant
                    group2_seguidores.append(player.participant.id_in_session)
                    

        for row in estructura:
            for player in row:
                if player.group_assignment == "Grupo 2" and player.group_role == "seguidor": #luego cambiar a player.Participant
                    group1_seguidores.append(player.participant.id_in_session)


        print("La lista de seguidores grupo 1 es: ", group1_seguidores)
        print("la lista de seguidores de grupo 2 es: ", group2_seguidores)


        # Generar pares de seguidores:

        follower1 = random.choice(group1_seguidores)
        follower2 = random.choice(group2_seguidores)

        pairs_followers = [follower1, follower2]

        print("la lista de seguidores es: ", pairs_followers)
        variable = [leaders_pair, pairs_followers]
        print(variable)

        subsession.set_group_matrix(variable)
        #print(subsession.set_group_matrix(leaders_pair, pairs_followers))
        print(subsession.get_group_matrix())

class instructions(Page):
    form_model = 'player'

    def is_displayed(player:Player):
        return player.round_number == 1
    
class image_evaluation(Page):
    form_model = 'player'
    form_fields = ['evaluacion']

class leader_message(Page):
    form_model = 'player'
    form_fields = ['leader_message']

    @staticmethod
    def is_displayed(player:Player):
        return player.group_role == 'lider'  # después cambiar a player.Participant.group_role
    
    @staticmethod
    def before_next_page(player:Player, timeout_happened):
        seguidores = player.get_others_in_subsession()   
        print("seguidores es: ", seguidores)
        print(player.leader_message)
        for p in seguidores:
            if p.group_assignment == player.group_assignment:
                print("p es: ", p)
                print("player.leader_message es: ", player.leader_message)
                p.leader_message = player.leader_message
        

class espera(WaitPage):
    wait_for_all_groups = True
    
      
class receipt_message(Page):
    form_model = 'player'
    
    @staticmethod
    def is_displayed(player:Player):
        return player.group_role == 'seguidor'

    @staticmethod
    def vars_for_template(player: Player):
        return dict(leader_message=player.leader_message)

class JOD_leader(Page):
    form_model = 'player'
    form_fields = ['agression']

    @staticmethod
    def is_displayed(player:Player):
        return player.group_role == 'lider'


class endownment_final_lideres(WaitPage):
    def is_displayed(player:Player):
        return player.group_role == 'lider'

    @staticmethod
    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        print("p1 es: ",p1)
        print("p2 es: ", p2)
        print("p1.endownment es: ", p1.endownment)
        print("p2.endownment es: ", p2.endownment)

        agression_p2 = p2.agression
        agression_p1 = p1.agression
        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final

        def vars_for_template(player:Player):
            return dict(agression_p1=agression_p1, agression_p2=agression_p2)
    

class JOD_leader_results(Page):

    def is_displayed(player:Player):
        return player.group_role == 'lider'

    @staticmethod
    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        agression_p2 = p2.aggression
        agression_p1 = p1.agression

        def vars_for_template(player:Player):
            return dict(agression_p1=agression_p1, agression_p2=agression_p2)


    def before_next_page(player:Player, timeout_happened):
        lista_jugadores = player.get_others_in_subsession()
        print("lista_jugadores es: ", lista_jugadores)   
         # Crear un diccionario para almacenar la agresión de los líderes por grupo
        agresion_lider_por_grupo = {}
            
        # Primero, recorrer la lista para obtener la agresión de los líderes
        for p in lista_jugadores:
            if p.group_role == 'lider':
                agresion_lider_por_grupo[p.group_assignment] = p.agression
            
            # Luego, recorrer la lista nuevamente para asignar la agresión de los líderes a los seguidores
        for p in lista_jugadores:
            if p.group_role == 'seguidor' and p.group_assignment in agresion_lider_por_grupo:
                p.agression_lider = agresion_lider_por_grupo[p.group_assignment]
                print(f"El seguidor {p.id_in_group} en {p.group_assignment} ahora tiene agression: {p.agression}")
        
        print("el diccionario de agression lider por grupo es: ", agresion_lider_por_grupo)

    
class followers_JOD(Page):
    form_model = 'player'
    form_fields = ['agression']

    def is_displayed(player:Player):
        return player.group_role == 'seguidor'  

        # ven el juego y toman la decisión

class endownment_final_seguidores(WaitPage):
    def is_displayed(player:Player):
        return player.group_role == 'seguidor'

    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        print("p1 es: ",p1)
        print("p2 es: ", p2)

        p1.endownment_final = p1.endownment - p2.agression
        p2.endownment_final = p2.endownment - p1.agression
        p1.agresion_guardada = p1.endownment - p1.endownment_final
        p2.agresion_guardada = p2.endownment - p2.endownment_final


class followers_JOD_results(Page):
    def is_displayed(player:Player):
        return player.group_role == 'seguidor'

    @staticmethod
    def after_all_players_arrive(group:Group):
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)

        agression_p2 = p2.aggression
        agression_p1 = p1.agression

        def vars_for_template(player:Player):
            return dict(agression_p1=agression_p1, agression_p2=agression_p2)




page_sequence = [ShuffleWaitPage1, ShuffleWaitPage2, instructions, image_evaluation, espera, JOD_leader, endownment_final_lideres, JOD_leader_results,
leader_message, espera, receipt_message, espera, followers_JOD, endownment_final_seguidores, followers_JOD_results] 


## 
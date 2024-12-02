from otree.api import *
from collections import defaultdict
import random

def make_field(label):
    return models.StringField(
        choices=[[1, '1. No me describe nada'], [2, '2'], [3,'3'], [4,'4. Algunas veces'], [5,'5'], [6,'6'], [7,'7 Me describe completamente']],
        label=label,
        widget=widgets.RadioSelect
    )

def make_inverted_field(label):
    return models.StringField(
        choices=[[7, '1. No me describe nada'], [6, '2'], [5,'3'], [4,'4. Algunas veces'], [3,'5'], [2,'6'], [1,'7 Me describe completamente']],
        label=label,
        widget=widgets.RadioSelect
    )


       
class C(BaseConstants):
    NAME_IN_URL = 'six_survey_dominant'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    SDP1 = make_field('Disfruto tener el control sobre otros')
    SDP2 = make_field('A menudo intento salirme con la mía, sin importar lo que quieran los demás')
    SDP3 = make_field('Estoy dispuesto a utilizar tácticas agresivas para salirme con la mía')
    SDP4 = make_field('Intento controlar a los demás en lugar de permitir que me controlen a mí')
    SDP5 = make_inverted_field('NO tengo una personalidad enérgica ni dominante')
    SDP6 = make_inverted_field('Otros saben que es mejor dejarme salirme con la mía')
    SDP7 = make_inverted_field('NO me gusta tener autoridad sobre otras personas')
    SDP8 = make_field('Algunas personas me tienen miedo') 
    paint1 = models.StringField(choices = [['kandinsky', 'A'], ['klee', 'B']], widget=widgets.RadioSelect,
    label = 'Ahora porfavor elija cuál pintura prefiere haciendo click en la opción "A" o "B"')
    paint2 = models.StringField(choices = [['klee', 'A'], ['kandinsky', 'B']], widget=widgets.RadioSelect,
    label = 'Ahora porfavor elija cuál pintura prefiere haciendo click en la opción "A" o "B"')
    paint3 = models.StringField(choices = [['klee', 'A'], ['kandinsky', 'B']], widget=widgets.RadioSelect,
    label = 'Ahora porfavor elija cuál pintura prefiere haciendo click en la opción "A" o "B"') 
    paint4 = models.StringField(choices = [['kandinsky', 'A'], ['klee', 'B']], widget=widgets.RadioSelect,
    label = 'Ahora porfavor elija cuál pintura prefiere haciendo click en la opción "A" o "B"')
    paint5 = models.StringField(choices = [['kandinsky', 'A'], ['klee', 'B']], widget=widgets.RadioSelect,
    label = 'Ahora porfavor elija cuál pintura prefiere haciendo click en la opción "A" o "B"')
    count_kandinski = models.IntegerField(initial=0)
    count_klee = models.IntegerField(initial=0)
    group_artist = models.StringField(choices=['grupo_klee', 'grupo_kandinksi'], default="")
    dom_scale_sum = models.IntegerField(default="")
    dom_scale_float = models.FloatField()
    dom_scale_normalized = models.FloatField()
    group_role = models.StringField(choices=['líder', 'seguidor'], default="")

# FUNCTIONS


# PAGES
class wellcome(Page):
    pass

class minimal_instructions(Page):
    form_model = 'player'

class paint1(Page):
    form_model = 'player'
    form_fields = ['paint1']

class paint2(Page):
    form_model = 'player'
    form_fields = ['paint2']

class paint3(Page):
    form_model = 'player'
    form_fields = ['paint3']

class paint4(Page):
    form_model = 'player'
    form_fields = ['paint4']
class paint5(Page):
    form_model = 'player'
    form_fields = ['paint5']

class asignacion_grupos(WaitPage):
    wait_for_all_groups=True
    
class SDP(Page):
    form_model = 'player'
    form_fields = [f'SDP{i}' for i in range (1, 9)]
    

class ShuffleWaitPage(WaitPage):
    
    wait_for_all_groups = True
    
    @staticmethod
    def after_all_players_arrive(subsession:Subsession):

        players = subsession.get_players()

        for player in players:
           player.dom_scale_sum = sum(int(getattr(player, f'SDP{i}')) for i in range(1, 9))
           player.dom_scale_float = float(player.dom_scale_sum)
           player.dom_scale_normalized = float((player.dom_scale_float - 7) / (56 - 7))


        for player in players:
            player.count_kandinski = 0
            player.count_klee = 0
            
            for i in range(1, 6):
                choice = getattr(player, f'paint{i}')
                if choice == 'kandinsky':
                    player.count_kandinski += 1
                elif choice == 'klee':
                    player.count_klee += 1

        players_sorted = sorted(players, key=lambda x: x.count_kandinski, reverse=True)

        for i, player in enumerate(players_sorted):
            if i < 3:  # Ahora está en 2 por temas de prueba, pero esto debe cambiar a 4 para que sean dos grupos de 4
                player.group_artist = 'grupo_kandinski'
            else:
                player.group_artist = 'grupo_klee'
        
        groups = defaultdict(list)
        for player in subsession.get_players():
            groups[player.group_artist].append(player)

        for group_players in groups.values():
            sorted_players = sorted(group_players, key=lambda player: player.dom_scale_normalized, reverse=True)

            # Verifica si los dos primeros jugadores tienen el mismo valor
            if sorted_players[0].dom_scale_normalized == sorted_players[1].dom_scale_normalized:
                leader = random.choice([sorted_players[0], sorted_players[1]])
            else:
                leader = sorted_players[0]  # El jugador con mayor valor de escala es el líder
            leader.group_role = "lider"

            for player in group_players:
                if player != leader:
                    player.group_role = "seguidor"

        for player in subsession.get_players():
            player.participant.group_artist = player.group_artist
            player.participant.group_role = player.group_role


class Group1_follower(Page):
    
    def is_displayed(player):
        return player.group_artist == "grupo_klee" and player.group_role == 'seguidor'

    def vars_for_template(player):

        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role == "lider"), None)

        return {
            'dom_scale': player.dom_scale_sum,
            'leader_dom_scale_sum': leader.dom_scale_sum if leader else "N/A"
        }

class Group2_follower(Page):

    def is_displayed(player):
        return player.group_artist == "grupo_kandinski" and player.group_role == 'seguidor'
    
    def vars_for_template(player):
   
        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role == "lider"), None)

        return {
            'dom_scale': player.dom_scale_sum,
            'leader_dom_scale_sum': leader.dom_scale_sum if leader else "N/A"
        }

class Group1_leader(Page):
    
    def is_displayed(player):
        return player.group_artist == "grupo_klee" and player.group_role == 'lider'

    def vars_for_template(player):
             
        return {
            'rol':  player.group_role
        }


class Group2_leader(Page):

    def is_displayed(player):
        return player.group_artist == "grupo_kandinski" and player.group_role == 'lider'

    def vars_for_template(player):
               
        return {
            'rol':  player.group_role,
            'dom_scale': player.dom_scale_sum
        }

# secuencia real que comentamos para usar una abreviada
# page_sequence = [Consent, end_experiment, minimal, Demographics, SDP, ShuffleWaitPage, GroupAssignment, Group2Assignment] 


page_sequence = [wellcome, minimal_instructions, paint1, paint2, paint3, paint4, paint5, SDP, ShuffleWaitPage,Group1_follower, Group2_follower, Group1_leader, Group2_leader] 


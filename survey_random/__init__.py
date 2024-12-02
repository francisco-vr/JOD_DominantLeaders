from otree.api import *
from collections import defaultdict
import random

       
class C(BaseConstants):
    NAME_IN_URL = 'survey_random'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
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
    

class ShuffleWaitPage(WaitPage):
    
    wait_for_all_groups = True
    
    @staticmethod
    def after_all_players_arrive(subsession:Subsession):

        players = subsession.get_players()

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
            if i < 4:  # Ahora está en 2 por temas de prueba, pero esto debe cambiar a 4 para que sean dos grupos de 4
                player.group_artist = 'grupo_kandinski'
            else:
                player.group_artist = 'grupo_klee'
        
        groups = defaultdict(list)

        for player in subsession.get_players():
            groups[player.group_artist].append(player)
            
        for group_players in groups.values():
            # Selecciona un líder aleatorio de los jugadores agrupados por group_artist
            leader = random.choice(group_players)
            leader.group_role = "lider"

    # Asigna el rol de seguidor a todos los demás jugadores en el grupo
            for player in group_players:
                if player != leader:
                    player.group_role = "seguidor"
                     

        for player in subsession.get_players():
            player.participant.group_artist = player.group_artist
            player.participant.group_role = player.group_role
            print(player.participant.group_artist)


class Group1_follower(Page):
    
    def is_displayed(player):
        return player.group_artist == "grupo_klee" and player.group_role == 'seguidor'

    def vars_for_template(player):

        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role == "lider"), None)


class Group2_follower(Page):

    def is_displayed(player):
        return player.group_artist == "grupo_kandinski" and player.group_role == 'seguidor'
    
    def vars_for_template(player):
   
        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role == "lider"), None)


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
        }

# secuencia real que comentamos para usar una abreviada
# page_sequence = [Consent, end_experiment, minimal, Demographics, SDP, ShuffleWaitPage, GroupAssignment, Group2Assignment] 


page_sequence = [wellcome, minimal_instructions, paint1, paint2, paint3, paint4, paint5, ShuffleWaitPage,Group1_follower, Group2_follower, Group1_leader, Group2_leader] 


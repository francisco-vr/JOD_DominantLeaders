from otree.api import *
from collections import defaultdict


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
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    pass
    
class Group(BaseGroup):

    pass

class Player(BasePlayer):
    finished = models.BooleanField(initial=False)
    approbed = models.StringField(
        choices=[['apruebo', 'Apruebo'], ['rechazo', 'Rechazo. Terminar experimento']],
        label='Señale si está de acuerdo con el consentimiento: ',
        widget=widgets.RadioSelect,
    )
    SDP1 = make_field('Disfruto tener el control sobre otros')
    SDP2 = make_field('A menudo intento salirme con la mía, sin importar lo que quieran los demás')
    SDP3 = make_field('Estoy dispuesto a utilizar tácticas agresivas para salirme con la mía')
    SDP4 = make_field('Intento controlar a los demás en lugar de permitir que me controlen a mí')
    SDP5 = make_inverted_field('NO tengo una personalidad enérgica ni dominante')
    SDP6 = make_inverted_field('Otros saben que es mejor dejarme salirme con la mía')
    SDP7 = make_inverted_field('NO me gusta tener autoridad sobre otras personas')
    SDP8 = make_field('Algunas personas me tienen miedo') 
    minimal = models.IntegerField(
        choices = [[1, '1 La Odio'], [2, '2'], [3, '3'], [4, '4 La amo']],
        label='Señale qué le parece la figura de Evelyn Matthei: ',
        widget=widgets.RadioSelect,
    )
    punitiveness1 = models.IntegerField(label='¿Cuánto dinero le quitarías como castigo al que aportó menos?', min= 0, max = 10000)
    punitiveness2 = models.IntegerField(label='¿Cuánto dinero le quitarías como castigo al que aportó menos?', min= 0, max = 10000)
    punitiveness3 = models.IntegerField(label='¿Cuánto dinero le quitarías como castigo al que aportó menos?', min= 0, max = 10000)
    group_assignment = models.StringField(default="")
    dom_scale_sum = models.IntegerField(default="")
    dom_scale_normalized=models.IntegerField(default="")
    mean_punitiveness = models.IntegerField(default="")
    group_role = models.StringField(choices=['líder', 'seguidor'], default="")

# FUNCTIONS


# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['approbed']

class end_experiment(Page):
    def is_displayed(player):
        return player.approbed=='rechazo'

class minimal(Page):
    form_model= 'player'
    form_fields=['minimal']

class SDP(Page):
    form_model = 'player'
    form_fields = ['SDP1', 'SDP2', 'SDP3', 'SDP4', 'SDP5', 'SDP6', 'SDP7', 'SDP8']

class punitiveness1(Page):
    form_model = 'player'
    form_fields = ['punitiveness1']

class punitiveness2(Page):
    form_model = 'player'
    form_fields = ['punitiveness2']

class punitiveness3(Page):
    form_model = 'player' 
    form_fields = ['punitiveness3']


class ShuffleWaitPage(WaitPage):
    
    wait_for_all_groups = True
    
    def after_all_players_arrive(self):
        for player in self.subsession.get_players():
            player.dom_scale_sum = sum(int(getattr(player, f'SDP{i}')) for i in range(1, 9))
            print("player.dom_scale_sum es: ", player.dom_scale_sum)
            player.dom_scale_normalized=int(((player.dom_scale_sum - 7) / (56 - 7)))
            print("player.dom_scale_normalized es: ", player.dom_scale_normalized)
            

            #punitiveness_values = [int(getattr(player, f"punitiveness{i}")) for i in range(1, 4)]
            #player.mean_punitiveness = int(sum(punitiveness_values) / len(punitiveness_values))

        for player in self.subsession.get_players():
            print("self.subsession.get_player() es: ", self.subsession.get_players())
            if player.minimal in [1, 2]:
                player.group_assignment = "Grupo 1"
            elif player.minimal in [3, 4]:
                player.group_assignment = "Grupo 2"

        groups = defaultdict(list)
        print("groups es: ", groups)
        for player in self.subsession.get_players():
            groups[player.group_assignment].append(player)
            print("groups es: ", groups)


        for group_players in groups.values():
            sorted_players = sorted(group_players, key=lambda player: player.dom_scale_normalized, reverse=True)

            print("sorted players es: ", sorted_players)

            leader = sorted_players[:1] # Edicion: por ahora sólo tengo como líder a quien tiene mayor valor de escala. #aca la variable original es top_players

            print("leader es: ", leader)

            # leader = max(top_players, key=lambda player: player.mean_punitiveness) #comento esto para no usar la punitividad

            leader.group_role = "lider"

            for player in group_players:
                if player != leader:
                    player.group_role = "seguidor"

        for player in self.subsession.get_players():    
            player.participant.group_assignment = player.group_assignment
            player.participant.group_role = player.group_role
            print(player.participant.group_assignment)


class Group1_follower(Page):
    
    def is_displayed(player):
        return player.group_assignment == "Grupo 1" and player.group_role == 'seguidor'

    def vars_for_template(player):

        group_players = player.group.get_players()
        
        leader = next((p for p in group_players if p.group_role == "lider"), None)

        return {
            'dom_scale': player.dom_scale_sum,
            'leader_dom_scale_sum': leader.dom_scale_sum if leader else "N/A"
        }

class Group2_follower(Page):

    def is_displayed(player):
        return player.group_assignment == "Grupo 2" and player.group_role == 'seguidor'
    
    def vars_for_template(player):
   
        group_players = player.group.get_players()
        
        #codigo para obtener valor del lider. no lo usaré pero está bueno
        leader = next((p for p in group_players if p.group_role == "lider"), None) 

        return {
            'dom_scale': player.dom_scale_sum,
            'leader_dom_scale_sum': leader.dom_scale_sum if leader else "N/A"
        }

class Group1_leader(Page):
    
    def is_displayed(player):
        return player.group_assignment == "Grupo 1" and player.group_role == 'lider'

    def vars_for_template(player):
             
        return {
            'rol':  player.group_role
        }


class Group2_leader(Page):

    def is_displayed(player):
        return player.group_assignment == "Grupo 2" and player.group_role == 'lider'

    def vars_for_template(player):
               
        return {
            'rol':  player.group_role,
            'dom_scale': player.dom_scale_sum
        }

# secuencia real que comentamos para usar una abreviada
# page_sequence = [Consent, end_experiment, minimal, SDP, punitiveness1, punitiveness2, punitiveness3, ShuffleWaitPage, GroupAssignment, Group2Assignment] 


page_sequence = [Consent, end_experiment, minimal, SDP, ShuffleWaitPage,Group1_follower, Group2_follower, Group1_leader, Group2_leader] 


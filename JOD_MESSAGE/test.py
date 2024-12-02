import random


class Player:
    def __init__(self, round_number, id_in_group, group_role, group_assignment):
        self.round_number = round_number
        self.id_in_group = id_in_group
        self.group_role = group_role
        self.group_assignment = group_assignment

# Definir una función para crear una matriz de jugadores
def create_player_matrix():
    player1 = Player(round_number=1, id_in_group=1, group_role='lider', group_assignment='Grupo 2')
    player2 = Player(round_number=1, id_in_group=2, group_role='seguidor', group_assignment='Grupo 2')

    # Crear la primera fila de jugadores
    row1 = [player1, player2]

    # Crear la segunda fila de jugadores (la misma que la primera)
    row2 = [player1, player2]

    # Crear la matriz de jugadores
    player_matrix = [row1, row2]

    return player_matrix

# Función para imprimir la matriz de jugadores
def print_player_matrix(matrix):
    for row in matrix:
        for player in row:
            print(f"Player(round_number={player.round_number}, id_in_group={player.id_in_group}, "
                  f"group_role='{player.group_role}', group_assignment='{player.group_assignment}')", end=", ")
        print()

# Crear la matriz de jugadores
player_matrix = create_player_matrix()

# Imprimir la matriz de jugadores
print("Matriz de jugadores:")
print_player_matrix(player_matrix)



estructura = [[Player(round_number=1, id_in_group=1, group_role='lider', group_assignment='Grupo 1'), Player(round_number=1, id_in_group=2, group_role='seguidor', group_assignment='Grupo 2')], [Player(round_number=1, id_in_group=1, group_role='lider', group_assignment='Grupo 2'), Player(round_number=1, id_in_group=2, group_role='seguidor', group_assignment='Grupo 1')]]

leaders_pair = [None, None]

for row in estructura:
    for player in row:
        if player.group_assignment=="Grupo 1" and player.group_role=="lider":
            leaders_pair[0] = player.id_in_group
            break


for row in estructura:
    for player in row:
        if player.group_assignment=="Grupo 2" and player.group_role == "lider":
            leaders_pair[1] = player.id_in_group
            break

print("la lista de partes de líderes es: ", leaders_pair)

# Crear listas vacías para los dos casos
group2_seguidores = []
group1_seguidores = []

for row in estructura:
    for player in row:
        if player.group_assignment == "Grupo 1" and player.group_role == "seguidor":
            group2_seguidores.append(player.id_in_group)
            

for row in estructura:
    for player in row:
        if player.group_assignment == "Grupo 2" and player.group_role == "seguidor":
            group1_seguidores.append(player.id_in_group)


print("La lista de seguidores grupo 1 es: ", group1_seguidores)
print("la lista de seguidores de grupo 2 es: ", group2_seguidores)


# Generar pares de jugadores:

follower1 = random.choice(group1_seguidores)
follower2 = random.choice(group2_seguidores)

pairs_followers = [follower1, follower2]

print("la lista de seguidores es: ", pairs_followers)





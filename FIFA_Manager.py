# FIFA-Manager, vergleich verschiedener Mannschaften
# 1BHIF | Marc Edlinger | 02.12.2021
rounds = 0                        # max rounds
max_goals = None                  # worst team, the main team played with
max_goals_opposite = None         # best team, the main team played with
opposite_team = None              # Current opposite team

class Team():       # model for a team, storing their stats

    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.goals_taken = 0
        self.wins = 0
        self.looses = 0
        self.draws = 0

    def __init__(self, name, goals):
        self.name = name
        self.goals = goals
        self.goals_taken = 0
        self.wins = 0
        self.looses = 0
        self.draws = 0

default_team = Team(input("Wie heißt dein Team? "))     # main team

while (rounds <= 0):
    rounds = int(input("Wie viele Runden werden gespielt? "))


for i in range(rounds):
    global opposite_team
    global max_goals
    global max_goals_opposite

    # inputs
    opposite_team = Team(input("Wie heißt der Gegner für Runde", i, "? "))
    goals_made = int(input("Wie viele Tore hat das Team", default_team.name, "gemacht? "))
    goals_taken = int(input("Wie viele Tore hat das Team", opposite_team.name, "gemacht? "))

    # save goals
    default_team.goals += goals_made
    default_team.goals_taken += goals_taken

    opposite_team.goals = goals_taken
    opposite_team.goals_taken = goals_made

    # record check
    if ((max_goals is None) or (goals_made > max_goals.goals)):
        max_goals = opposite_team

    if ((max_goals_opposite is None) or (goals_taken > max_goals_opposite.goals)):
        max_goals_opposite = opposite_team

    # win check
    if (goals_made > goals_taken):
        # win
        default_team.wins += 1
        print(default_team.name, "hat gewonnen :)")
    elif (goals_made < goals_taken):
        # lose
        default_team.looses += 1
        print(opposite_team.name, "hat gewonnen :(")
    else:
        # draw
        default_team.draws += 1
        print("Unentschieden :/")

print(rounds, "Spiele,", default_team.wins, "Gewonnen,", default_team.looses, "Verloren,", default_teams.draws, "Unentschieden")
print("Tordifferenz:", (default_team.goals_made - default_team.goals_taken))
print("Bester Sieg:", max_goals.name, ", Tore:", max_goals.goals_taken)
print("Schlechteste Niederlage:", max_goals_opposite.name, ", Tore:", max_goals_opposite.goals_made)


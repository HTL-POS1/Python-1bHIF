# FIFA-Manager, vergleich verschiedener Mannschaften
# 1BHIF | Marc Edlinger | 02.12.2021
import sys

rounds = 0                         # max rounds
worst_team = None                  # worst team, the main team played with
best_team = None                   # best team, the main team played with


class Team():       # model for a team, storing their stats

    def __init__(self, name):
        self.name = name
        self.goals = 0
        self.goals_taken = 0
        self.wins = 0
        self.looses = 0
        self.draws = 0


# Force the user to provide an positive integer
def ask_for_positive_int(text: str):
    input_number = -1
    while (input_number < 0):
        input_number = int(input(text))
    return input_number
    

default_team = Team(input("Wie heißt dein Team? "))     # main team
rounds = u.ask_for_positive_int("Wie viele Runden werden gespielt? (0 = Ende) ")
if (rounds == 0):
    sys.exit(505)

for i in range(rounds):
    # inputs
    opposite_team = Team(input("Wie heißt der Gegner für Runde " + str(i+1) + "? "))
    goals_made = u.ask_for_positive_int("Wie viele Tore hat das Team " + default_team.name + " gemacht? ")
    goals_taken = u.ask_for_positive_int("Wie viele Tore hat das Team " + opposite_team.name + " gemacht? ")

    # save goals
    default_team.goals += goals_made
    default_team.goals_taken += goals_taken

    opposite_team.goals = goals_taken
    opposite_team.goals_taken = goals_made

    # record check
    if ((worst_team is None) or (goals_made > worst_team.goals_taken)):
        worst_team = opposite_team

    if ((best_team is None) or (goals_made > best_team.goals)):
        best_team = opposite_team

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

print(rounds, "Spiele,", default_team.wins, "Gewonnen,", default_team.looses, "Verloren,", default_team.draws, "Unentschieden")
print("negatives Torverhältnis von:", default_team.goals, "zu", default_team.goals_taken)
print("Bester Sieg:", worst_team.name, ", Tore:", worst_team.goals_taken)
print("Schlechteste Niederlage:", best_team.name, ", Tore:", best_team.goals)


# Ermittlung der schnellsten/langsamsten Laufzeit
# 1BHIF | Marc Edlinger | 25.11.2021
class Runner:   # model for a runner, storing its name and its run-time
    def __init__(self, name, time):
        self.name = name
        self.time = time


fastest_runner = None
slowest_runner = None
wrong_input = 0


def register_runner(runner: Runner):    # check if the new runner is faster than the fastest, or slower than the slowest
    global fastest_runner
    global slowest_runner

    if ((fastest_runner is None) or (fastest_runner.time < runner.time)):
        fastest_runner = runner

    if ((slowest_runner is None) or (slowest_runner.time > runner.time)):
        slowest_runner = runner


def ask(display_text: str, max_possible: int):  # force conditioned input, return the valid input value
    global wrong_input
    value = -1

    while ((value < 0) or (value > max_possible)):
        value = int(input("Zeit gebraucht [" + display_text + "] " + "max " + str(max_possible) + ": "))
        wrong_input += 1
    wrong_input -= 1
    return value


def convert(centis: int):    # Return format: (minutes, seconds, centis)
    seconds = centis // 100
    centis = centis % 100

    minutes = seconds // 60
    seconds = seconds % 60

    return minutes, seconds, centis


while True:
    runner_name = input("Name vom läufer (exit = Exit): ")
    if ((runner_name == "exit") or (runner_name == "")):
        if (fastest_runner is None):
            continue
        break

    runner_minutes = ask("Minuten", 60)
    runner_seconds = ask("Sekunden", 60)
    runner_centi = ask("Hunderstel", 100)
    runner_time = runner_centi + (runner_seconds * 100) + (runner_minutes * 6000)

    register_runner(Runner(runner_name, runner_time))

print("Langsamster läufer:", fastest_runner.name, "Zeit:", convert(fastest_runner.time))
print("Schnellster läufer:", slowest_runner.name, "Zeit:", convert(slowest_runner.time))
print("Differenz: ", convert(fastest_runner.time - slowest_runner.time))
print("Fehlerhafte Eingaben:", wrong_input)

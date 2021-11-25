# Ermittlung der schnellsten/langsamsten Laufzeit
# 1BHIF | Marc Edlinger | 25.11.2021

class Runner:
    def __init__(self, name, time):
        self.name = name
        self.time = time

fastest_runner = None
slowest_runner = None

def register_runner(runner: Runner):
    global fastest_runner
    global slowest_runner

    if ((fastest_runner is None) or (fastest_runner.time < runner.time)):
        fastest_runner = runner
    
    if ((slowest_runner is None) or (slowest_runner.time > runner.time)):
        slowest_runner = runner

def ask(display_text: str):
    value = -1
    while (value < 0):
        value = int(input("Zeit gebraucht " + display_text + ": "))
    return value

def convert(centis: int):    # Return format: (minutes, seconds, centis)
    minutes = centis % 6000
    centis //= 6000

    seconds = centis % 100
    centis //= 100
    return minutes, seconds, centis
    

while True:
    runner_name = input("Name vom läufer (exit = Exit): ")
    if (runner_name == "exit"):
        break

    runner_minutes = ask("Minuten")
    runner_seconds = ask("Sekunden")
    runner_centi = ask("Hunderstel")
    runner_time = runner_centi + (runner_seconds * 100) + (runner_minutes * 6000)

    register_runner(Runner(runner_name, runner_time))

print("Schnellster läufer:", fastest_runner.name, "Zeit:", convert(fastest_runner.time))
print("Langsamster läufer:", slowest_runner.name, "Zeit:", convert(slowest_runner.time))
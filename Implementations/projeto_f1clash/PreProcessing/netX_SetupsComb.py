import itertools
import networkx as nx
import csv
import plotly.express as px


# Creating the Breaks dictionary:
breaks = {
    "Wildcore" : {"Speed": 36, "Cornering": 23, "Power Unit": 33, "Reliability": 22, "Avg_PitStop_time": 0.59},
    "Suspense": {"Speed": 20, "Cornering": 32, "Power Unit": 23, "Reliability": 21, "Avg_PitStop_time": 0.37},
    "The Warden":{"Speed": 26, "Cornering": 28, "Power Unit": 27,"Reliability": 25, "Avg_PitStop_time": 0.43},
    "Onyx":{"Speed": 26, "Cornering": 23, "Power Unit": 25, "Reliability": 50, "Avg_PitStop_time": 0.49},
    "Axiom":{"Speed": 14, "Cornering": 34, "Power Unit": 18, "Reliability": 15, "Avg_PitStop_time": 0.67},
    "Crisis SL":{"Speed": 27, "Cornering": 16, "Power Unit": 18, "Reliability": 19, "Avg_PitStop_time": 0.51},
    "Essence":{"Speed": 14, "Cornering": 13, "Power Unit": 12, "Reliability": 25, "Avg_PitStop_time": 0.76},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

# Creating the GearBox dictionary:
gearbox = {
    "Voyage" : {"Speed": 23, "Cornering": 28, "Power Unit": 22, "Reliability": 27, "Avg_PitStop_time": 0},
    "Vector": {"Speed": 24, "Cornering": 38, "Power Unit": 22, "Reliability": 36, "Avg_PitStop_time": 0.55},
    "Kick Shift":{"Speed": 18, "Cornering": 19, "Power Unit": 29,"Reliability": 19, "Avg_PitStop_time": 0.45},
    "Verdict":{"Speed": 33, "Cornering": 18, "Power Unit": 20, "Reliability": 30, "Avg_PitStop_time": 0.63},
    "Spectrum":{"Speed": 20, "Cornering": 25, "Power Unit": 21, "Reliability": 23, "Avg_PitStop_time": 0.53},
    "Swiftcharge":{"Speed": 14, "Cornering": 23, "Power Unit": 22, "Reliability": 16, "Avg_PitStop_time": 0.71},
    "Switch-R-00":{"Speed": 12, "Cornering": 13, "Power Unit": 11, "Reliability": 14, "Avg_PitStop_time": 0.47},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

# Creating the RearWing dictionary:
rear_wings = {
    "Typhoon" : {"Speed": 50, "Cornering": 27, "Power Unit": 26, "Reliability": 23, "Avg_PitStop_time": 0.53},
    "Transcendence": {"Speed": 24, "Cornering": 22, "Power Unit": 36, "Reliability": 37, "Avg_PitStop_time": 0.53},
    "Freeflare":{"Speed": 21, "Cornering": 33, "Power Unit": 20,"Reliability": 22, "Avg_PitStop_time": 0.37},
    "The Patron":{"Speed": 23, "Cornering": 21, "Power Unit": 19, "Reliability": 37, "Avg_PitStop_time": 0.61},
    "The Wasp":{"Speed": 16, "Cornering": 24, "Power Unit": 23, "Reliability": 14, "Avg_PitStop_time": 0.69},
    "The Matador":{"Speed": 19, "Cornering": 16, "Power Unit": 18, "Reliability": 17, "Avg_PitStop_time": 0.72},
    "Phantom-X":{"Speed": 26, "Cornering": 15, "Power Unit": 12, "Reliability": 11, "Avg_PitStop_time": 0.76},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

# Creating the FrontWing dictionary:
front_wings = {
    "Virtue" : {"Speed": 23, "Cornering": 50, "Power Unit": 27, "Reliability": 24, "Avg_PitStop_time": 0.49},
    "Thunderclap": {"Speed": 35, "Cornering": 23, "Power Unit": 21, "Reliability": 33, "Avg_PitStop_time": 0.55},
    "Trailblazer":{"Speed": 21, "Cornering": 23, "Power Unit": 42,"Reliability": 20, "Avg_PitStop_time": 0.57},
    "Zeno":{"Speed": 25, "Cornering": 23, "Power Unit": 22, "Reliability": 26, "Avg_PitStop_time": 0.53},
    "The Vagabond":{"Speed": 31, "Cornering": 20, "Power Unit": 23, "Reliability": 21, "Avg_PitStop_time": 0.35},
    "Feral Punch":{"Speed": 13, "Cornering": 15, "Power Unit": 22, "Reliability": 21, "Avg_PitStop_time": 0.73},
    "The Scout":{"Speed": 13, "Cornering": 27, "Power Unit": 15, "Reliability": 14, "Avg_PitStop_time": 0.73},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

# Creating the Suspensions dictionary:
suspensions = {
    "Sigma" : {"Speed": 32, "Cornering": 28, "Power Unit": 30, "Reliability": 29, "Avg_PitStop_time": 0.39},
    "Presenca": {"Speed": 23, "Cornering": 26, "Power Unit": 24, "Reliability": 22, "Avg_PitStop_time": 0.2},
    "Horizon":{"Speed": 22, "Cornering": 36, "Power Unit": 24,"Reliability": 37, "Avg_PitStop_time": 0.53},
    "Radiance":{"Speed": 25, "Cornering": 17, "Power Unit": 26, "Reliability": 19, "Avg_PitStop_time": 0.65},
    "Icon V3":{"Speed": 17, "Cornering": 13, "Power Unit": 16, "Reliability": 23, "Avg_PitStop_time": 0.54},
    "Rodeo":{"Speed": 23, "Cornering": 22, "Power Unit": 15, "Reliability": 14, "Avg_PitStop_time": 0.69},
    "The Equator":{"Speed": 20, "Cornering": 19, "Power Unit": 18, "Reliability": 21, "Avg_PitStop_time": 0.61},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

# Creating the Engines dictionary:
engines = {
    "Cloudroar" : {"Speed": 26, "Cornering": 24, "Power Unit": 50, "Reliability": 27, "Avg_PitStop_time": 0.55},
    "Avalanche": {"Speed": 34, "Cornering": 22, "Power Unit": 25, "Reliability": 21, "Avg_PitStop_time": 0.35},
    "The Rover":{"Speed": 27, "Cornering": 25, "Power Unit": 28, "Reliability": 24, "Avg_PitStop_time": 0.53},
    "Twinburst":{"Speed": 16, "Cornering": 29, "Power Unit": 18, "Reliability": 17, "Avg_PitStop_time": 0.51},
    "Enigma":{"Speed": 16, "Cornering": 13, "Power Unit": 23, "Reliability": 25, "Avg_PitStop_time": 0.69},
    "Nova":{"Speed": 31, "Cornering": 13, "Power Unit": 15, "Reliability": 16, "Avg_PitStop_time": 0.71},
    "Brute Force":{"Speed": 21, "Cornering": 19, "Power Unit": 36, "Reliability": 18, "Avg_PitStop_time": 0.63},
    "Starter":{"Speed": 1, "Cornering": 1, "Power Unit": 1, "Reliability": 1, "Avg_PitStop_time": 1}
}

def save_to_csv(data, filename):
    if not data:
        print("Nenhum dado para salvar.")
        return

    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def generate_Team_Score(breaks, engines, suspensions, front_wings, gearboxes, rear_wings):
    setups = []  # Lista para armazenar as combinações e seus Team Scores

    # Gere todas as combinações possíveis de componentes
    all_combinations = itertools.product(breaks.keys(), engines.keys(), suspensions.keys(), front_wings.keys(), gearboxes.keys(), rear_wings.keys())

    for combination in all_combinations:
        components = {
            "Break": breaks[combination[0]],
            "Engine": engines[combination[1]],
            "Suspension": suspensions[combination[2]],
            "Front_Wing": front_wings[combination[3]],
            "Gearbox": gearboxes[combination[4]],
            "Rear_Wing": rear_wings[combination[5]]
        }

        # Calcula os totais para cada atributo
        total_speed = sum(components[category]["Speed"] for category in components)
        total_cornering = sum(components[category]["Cornering"] for category in components)
        total_power_unit = sum(components[category]["Power Unit"] for category in components)
        total_reliability = sum(components[category]["Reliability"] for category in components)
        total_avg_pitstop_time = sum(components[category]["Avg_PitStop_time"] for category in components)

        # Calcula o Team Score
        team_score = total_speed + total_cornering + total_power_unit + total_reliability + (total_avg_pitstop_time / 0.02)

        # Armazena a combinação e seu Team Score na lista de setups
        setup = {
            "Break": combination[0],
            "Engine": combination[1],
            "Suspension": combination[2],
            "Front_Wing": combination[3],
            "Gearbox": combination[4],
            "Rear_Wing": combination[5],
            "Team_Score": team_score
        }
        setups.append(setup)

    return setups

# Exemplo de uso
team_setups = generate_Team_Score(breaks, engines, suspensions, front_wings, gearbox, rear_wings)

# Classifique os setups por Team Score
team_setups_sorted = sorted(team_setups, key=lambda x: x["Team_Score"], reverse=True)

# Salve os setups em um arquivo CSV
save_to_csv(team_setups_sorted, 'team_setups.csv')

# Imprima os 3 melhores setups
for i, setup in enumerate(team_setups_sorted[:3], 1):
    print(f"Setup #{i}:")
    print(f"Break: {setup['Break']}")
    print(f"Engine: {setup['Engine']}")
    print(f"Suspension: {setup['Suspension']}")
    print(f"Front Wing: {setup['Front_Wing']}")
    print(f"Gearbox: {setup['Gearbox']}")
    print(f"Rear Wing: {setup['Rear_Wing']}")
    print(f"Team Score: {setup['Team_Score']}")
    print()


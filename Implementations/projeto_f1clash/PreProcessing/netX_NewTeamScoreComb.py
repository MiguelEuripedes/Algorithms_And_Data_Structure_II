drivers = {
    'Verstappen': {'Overtaking': 97, 'Defending': 86, 'Qualifying': 99, 'Race_Start': 89, 'Tyre_Management': 94},
    'Leclerc': {'Overtaking': 93, 'Defending': 99, 'Qualifying': 97, 'Race_Start': 87, 'Tyre_Management': 89},
    'Alonso': {'Overtaking': 99,'Defending': 92,'Qualifying': 89,'Race_Start': 97,'Tyre_Management': 88},
    'Hamilton': {'Overtaking': 81,'Defending': 86,'Qualifying': 89,'Race_Start': 94,'Tyre_Management': 90},
    'Norris': {'Overtaking': 99,'Defending': 95,'Qualifying': 99,'Race_Start': 99,'Tyre_Management': 99},
    'Russell': {'Overtaking': 95,'Defending': 90,'Qualifying': 91,'Race_Start': 83,'Tyre_Management': 86},
    'Perez': {'Overtaking': 85,'Defending': 96,'Qualifying': 89,'Race_Start': 91,'Tyre_Management': 84},
    'Sainz': {'Overtaking': 84,'Defending': 85,'Qualifying': 95,'Race_Start': 90,'Tyre_Management': 91},
    'Stroll': {'Overtaking': 92,'Defending': 83,'Qualifying': 87,'Race_Start': 94,'Tyre_Management': 89},
    'Gasly': {'Overtaking': 88,'Defending': 93,'Qualifying': 83,'Race_Start': 85,'Tyre_Management': 96}
}


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

csv_data = [  
    "1,Onyx,Cloudroar,Horizon,Virtue,Vector,Typhoon,897.0",
    "2,Wildcore,Cloudroar,Horizon,Virtue,Vector,Typhoon,892.0",
    "3,Onyx,Cloudroar,Sigma,Virtue,Vector,Typhoon,890.0",
    "4,Onyx,Cloudroar,Horizon,Virtue,Vector,Transcendence,890.0",
    "5,Onyx,Cloudroar,Horizon,Thunderclap,Vector,Typhoon,888.0",
    "6,Wildcore,Cloudroar,Sigma,Virtue,Vector,Typhoon,885.0",
    "7,Wildcore,Cloudroar,Horizon,Virtue,Vector,Transcendence,885.0",
    "8,Wildcore,Cloudroar,Horizon,Thunderclap,Vector,Typhoon,883.0",
    "9,Onyx,Cloudroar,Sigma,Virtue,Vector,Transcendence,883.0",
    "10,Onyx,Cloudroar,Horizon,Trailblazer,Vector,Typhoon,883.0",
    "11,Onyx,Cloudroar,Horizon,Virtue,Verdict,Typhoon,882.0",
    "12,Onyx,Cloudroar,Sigma,Thunderclap,Vector,Typhoon,881.0",
    "13,Onyx,Cloudroar,Horizon,Thunderclap,Vector,Transcendence,881.0",
    "14,Wildcore,Cloudroar,Sigma,Virtue,Vector,Transcendence,878.0",
    "15,Wildcore,Cloudroar,Horizon,Trailblazer,Vector,Typhoon,878.0",
    "16,Wildcore,Cloudroar,Horizon,Virtue,Verdict,Typhoon,877.0",
    "17,Wildcore,Cloudroar,Sigma,Thunderclap,Vector,Typhoon,876.0",
    "18,Wildcore,Cloudroar,Horizon,Thunderclap,Vector,Transcendence,876.0",
    "19,The Warden,Cloudroar,Horizon,Virtue,Vector,Typhoon,876.0",
    "20,Onyx,Cloudroar,Sigma,Trailblazer,Vector,Typhoon,876.0",
    "21,Onyx,Cloudroar,Horizon,Trailblazer,Vector,Transcendence,876.0",
    "22,Onyx,Cloudroar,Sigma,Virtue,Verdict,Typhoon,875.0",
    "23,Onyx,Cloudroar,Horizon,Virtue,Vector,The Patron,875.0",
    "24,Onyx,Cloudroar,Horizon,Virtue,Verdict,Transcendence,875.0",
    "25,Onyx,Cloudroar,Sigma,Thunderclap,Vector,Transcendence,874.0",
    "26,Onyx,Cloudroar,Horizon,Thunderclap,Verdict,Typhoon,873.0",
    "27,Onyx,The Rover,Horizon,Virtue,Vector,Typhoon,873.0",
    "28,Wildcore,Cloudroar,Sigma,Trailblazer,Vector,Typhoon,871.0",
    "29,Wildcore,Cloudroar,Horizon,Trailblazer,Vector,Transcendence,871.0",
    "30,Onyx,Cloudroar,Horizon,Zeno,Vector,Typhoon,871.0",
    "31,Onyx,Cloudroar,Radiance,Virtue,Vector,Typhoon,871.0",
    "32,Wildcore,Cloudroar,Sigma,Virtue,Verdict,Typhoon,870.0",
    "33,Wildcore,Cloudroar,Horizon,Virtue,Vector,The Patron,870.0",
    "34,Wildcore,Cloudroar,Horizon,Virtue,Verdict,Transcendence,870.0"
]

import csv

# Lista de colunas
columns = ['Setup', 'Speed', 'Cornering', 'Power_Unit', 'Reliability', 'Avg_PitStop_time', 'Team_Score']

# Abrir o arquivo CSV de saída
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Escrever o cabeçalho
    writer.writerow(columns)

    # Processar os dados do CSV
    for row in csv_data:
        values = row.split(',')

        setup = int(values[0])
        break_name, engine_name, suspension_name, front_wing_name, gearbox_name, rear_wing_name, team_score = values[1:]

        # Obter os valores correspondentes dos dicionários
        break_values = breaks.get(break_name, {})
        engine_values = engines.get(engine_name, {})
        suspension_values = suspensions.get(suspension_name, {})
        front_wing_values = front_wings.get(front_wing_name, {})
        gearbox_values = gearbox.get(gearbox_name, {})
        rear_wing_values = rear_wings.get(rear_wing_name, {})

        # Calcular os totais
        speed = (
            break_values.get('Speed', 0) +
            engine_values.get('Speed', 0) +
            suspension_values.get('Speed', 0) +
            front_wing_values.get('Speed', 0) +
            gearbox_values.get('Speed', 0) +
            rear_wing_values.get('Speed', 0)
        )
        cornering = (
            break_values.get('Cornering', 0) +
            engine_values.get('Cornering', 0) +
            suspension_values.get('Cornering', 0) +
            front_wing_values.get('Cornering', 0) +
            gearbox_values.get('Cornering', 0) +
            rear_wing_values.get('Cornering', 0)
        )
        power_unit = (
            break_values.get('Power Unit', 0) +
            engine_values.get('Power Unit', 0) +
            suspension_values.get('Power Unit', 0) +
            front_wing_values.get('Power Unit', 0) +
            gearbox_values.get('Power Unit', 0) +
            rear_wing_values.get('Power Unit', 0)
        )
        reliability = (
            break_values.get('Reliability', 0) +
            engine_values.get('Reliability', 0) +
            suspension_values.get('Reliability', 0) +
            front_wing_values.get('Reliability', 0) +
            gearbox_values.get('Reliability', 0) +
            rear_wing_values.get('Reliability', 0)
        )
        avg_pitstop_time = (
            break_values.get('Avg_PitStop_time', 0) +
            engine_values.get('Avg_PitStop_time', 0) +
            suspension_values.get('Avg_PitStop_time', 0) +
            front_wing_values.get('Avg_PitStop_time', 0) +
            gearbox_values.get('Avg_PitStop_time', 0) +
            rear_wing_values.get('Avg_PitStop_time', 0)
        )

        # Escrever a linha no CSV de saída
        writer.writerow([setup, speed, cornering, power_unit, reliability, avg_pitstop_time, team_score])
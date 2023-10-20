import csv

boost = {
    "Tsar": {
        "Speed": 0, "Cornering": 15, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 10, "Race_Start": 0,
        "Tyre_Management": 25
    }, 
    "Frost": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 10, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 15,
        "Tyre_Management": 25
    },
    "Tulip": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 20, "Pit_Stop": 20, "Overtaking": 0, "Defending": 10, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Dragon": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 15, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 20, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 15
    },
    "Kawaii": {
        "Speed": 0, "Cornering": 20, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 15, "Overtaking": 0, "Defending": 0, "Race_Start": 15,
        "Tyre_Management": 0
    },
    "Pretzel": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 15, "Reliability": 0, "Pit_Stop": 10, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 25
    }, 
    "Vice": {
        "Speed": 10, "Cornering": 0, "Power_Unit": 15, "Reliability": 25, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Schooner": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 25, "Pit_Stop": 15, "Overtaking": 0, "Defending": 10, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Djinn": {
        "Speed": 0, "Cornering": 15, "Power_Unit": 0, "Reliability": 20, "Pit_Stop": 0, "Overtaking": 0, "Defending": 15, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Oud": {
        "Speed": 0, "Cornering": 10, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 25, "Overtaking": 15, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Eternal Flame": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 15, "Pit_Stop": 0, "Overtaking": 25, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 10
    },
    "Eagle": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 15, "Pit_Stop": 15, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 20
    },
    "Iron Force": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 20, "Reliability": 20, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 10
    },
    "Lumberjack": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 15, "Pit_Stop": 0, "Overtaking": 0, "Defending": 15, "Race_Start": 0,
        "Tyre_Management": 10
    },
    "Cranberry": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 10, "Pit_Stop": 0, "Overtaking": 20, "Defending": 20, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Butterfly": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 25, "Reliability": 0, "Pit_Stop": 5, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 20
    },
    "Tune-in": {
        "Speed": 10, "Cornering": 15, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 25, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Self-Control": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 5, "Reliability": 5, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 5
    },
    "Warrior": {
        "Speed": 10, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 5, "Defending": 5, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Ballast": {
        "Speed": 0, "Cornering": 10, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 10, "Overtaking": 0, "Defending": 0, "Race_Start": 5,
        "Tyre_Management": 0
    },
    "Instinct": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 15, "Reliability": 5, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 10,
        "Tyre_Management": 0
    },
    "Downforce": {
        "Speed": 0, "Cornering": 5, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 15, "Race_Start": 0,
        "Tyre_Management": 15
    },
    "Hex": {
        "Speed": 15, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 5, "Overtaking": 20, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Eggception": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 10, "Reliability": 0, "Pit_Stop": 25, "Overtaking": 0, "Defending": 15, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Rooster": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 10, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 20, "Defending": 0, "Race_Start": 20,
        "Tyre_Management": 0
    },
    "Cuppa": {
        "Speed": 0, "Cornering": 20, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 10, "Defending": 0, "Race_Start": 20,
        "Tyre_Management": 0
    },
    "Street Shark": {
        "Speed": 15, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 10, "Defending": 0, "Race_Start": 25,
        "Tyre_Management": 0
    },
    "Herald": {
        "Speed": 0, "Cornering": 15, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 10, "Defending": 0, "Race_Start": 25,
        "Tyre_Management": 0
    },
    "Prince": {
        "Speed": 0, "Cornering": 20, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 10, "Race_Start": 20,
        "Tyre_Management": 0
    },
    "Unstoppable": {
        "Speed": 15, "Cornering": 0, "Power_Unit": 10, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 25, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Dead Fast": {
        "Speed": 25, "Cornering": 0, "Power_Unit": 20, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 5
    },
    "Gladiator": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 10, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 25, "Race_Start": 15,
        "Tyre_Management": 0
    },
    "Taurus": {
        "Speed": 20, "Cornering": 0, "Power_Unit": 25, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 5, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Merlion": {
        "Speed": 15, "Cornering": 25, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 10, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Samba": {
        "Speed": 5, "Cornering": 0, "Power_Unit": 25, "Reliability": 0, "Pit_Stop": 20, "Overtaking": 0, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Caveira": {
        "Speed": 25, "Cornering": 0, "Power_Unit": 10, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 15, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Fogos": {
        "Speed": 20, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 15, "Defending": 0, "Race_Start": 15,
        "Tyre_Management": 0
    },
    "Movember": {
        "Speed": 0, "Cornering": 25, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 15, "Race_Start": 0,
        "Tyre_Management": 10
    },
    "Palmeira": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 20, "Race_Start": 10,
        "Tyre_Management": 20
    },
    "Nazar": {
        "Speed": 0, "Cornering": 0, "Power_Unit": 0, "Reliability": 15, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 25,
        "Tyre_Management": 15
    },
    "Aderencia": {
        "Speed": 0, "Cornering": 25, "Power_Unit": 0, "Reliability": 15, "Pit_Stop": 0, "Overtaking": 0, "Defending": 0, "Race_Start": 10,
        "Tyre_Management": 0
    },
    "Arco-iris": {
        "Speed": 20, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 0, "Overtaking": 0, "Defending": 25, "Race_Start": 5,
        "Tyre_Management": 0
    },
    "Eclipse": {
        "Speed": 25, "Cornering": 0, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 10, "Overtaking": 15, "Defending": 0, "Race_Start": 0,
        "Tyre_Management": 0
    },
    "Rena": {
        "Speed": 0, "Cornering": 10, "Power_Unit": 0, "Reliability": 0, "Pit_Stop": 20, "Overtaking": 0, "Defending": 20, "Race_Start": 0,
        "Tyre_Management": 0
    }
} 



with open('boost.csv', 'w', newline='') as csvfile:
    fieldnames = ["Boost_name"] + list(boost["Tsar"].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for boost_name, stats in boost.items():
        row = {"Boost_name": boost_name}
        row.update(stats)
        writer.writerow(row)
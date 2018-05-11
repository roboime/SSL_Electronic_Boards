designFile = "C:/Users/estagiario02/Desktop/SSL_Electronic_Boards/SSL_Electronic_Boards/Kicker_Module_2018/PDNAnalyzer_Output/Kicker2018_PCB/odb.tgz"

powerNets = ["VCC", "NetL2_7", "NetLT3750_6"]

groundNets = ["Cap-"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("0R015", "1") ],
"ground_pins": [ ("0R015", "2") ],
"current": 5,
"Rpin": 0.02,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("P2", "1"), ("P2", "2"), ("P2", "3"), ("P2", "4"), ("P2", "5"), ("P2", "6") ],
"ground_pins": [ ("P1", "1"), ("P1", "2"), ("P1", "3"), ("P1", "4"), ("P1", "5"), ("P1", "6"), ("P1", "7"), ("P1", "8"), ("P1", "9") ],
"voltage": 8.4,
"Rpin": 0,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("L2", "6"), ("L2", "5"), ("L2", "4"), ("L2", "3") ],
"out": [ ("L2", "7"), ("L2", "8"), ("L2", "9"), ("L2", "10") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2E-06,
}
,
{
"id": "3",
"type": "linear",

"in": [ ("Q1", "8"), ("Q1", "7"), ("Q1", "6"), ("Q1", "5") ],
"out": [ ("Q1", "3"), ("Q1", "2"), ("Q1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 1.71428571428571E-06,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-_1', 'DielectricConstant': 4.8, 'Thickness': 0.00032004},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False

designFile = "C:/Users/estagiario02/Desktop/SSL_Electronic_Boards/SSL_Electronic_Boards/Kicker_Module_2018/PDNAnalyzer_Output/Kicker2018_PCB/odb.tgz"

powerNets = ["Cap+"]

groundNets = ["Cap-", "CHIP_KICK-"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("CON_CHIP_KICK", "2") ],
"ground_pins": [ ("CON_CHIP_KICK", "1") ],
"current": 60,
"Rpin": 0.00166666666666667,
}
,
{
"id": "1",
"type": "source",
"power_pins": [ ("pdna_comp_(+)_CON_CAP_(-)_1", "1") ],
"ground_pins": [ ("pdna_comp_(+)_CON_CAP_(-)_1", "2") ],
"voltage": 180,
"Rpin": 0,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("Q3", "3") ],
"out": [ ("Q3", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
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

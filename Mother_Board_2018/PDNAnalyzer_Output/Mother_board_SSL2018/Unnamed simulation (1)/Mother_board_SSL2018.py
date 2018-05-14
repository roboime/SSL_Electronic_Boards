designFile = "C:/Users/Public/Documents/Altium/Projects/Mother_Board_SSL2018/PDNAnalyzer_Output/Mother_board_SSL2018/odb.tgz"

powerNets = ["NetBAT_0", "VBAT", "NetFM_M0_2", "NetC1_M0_2", "MA_M0"]

groundNets = ["GND", "MB_M0"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("BAT", "0") ],
"ground_pins": [ ("BAT", "1") ],
"voltage": 8.1,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("06x01_Conector_Male_M0", "5") ],
"ground_pins": [ ("06x01_Conector_Male_M0", "6") ],
"current": 4,
"Rpin": 0.025,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("SW", "0") ],
"out": [ ("SW", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "3",
"type": "linear",

"in": [ ("R11_M0", "2") ],
"out": [ ("R11_M0", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "4",
"type": "linear",

"in": [ ("FM_M0", "2") ],
"out": [ ("FM_M0", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "5",
"type": "linear",

"in": [ ("M0-MOTOR", "2") ],
"out": [ ("M0-MOTOR", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "6",
"type": "linear",

"in": [ ("M0-MOTOR", "3") ],
"out": [ ("M0-MOTOR", "0") ],
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

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-_1', 'DielectricConstant': 4.8, 'Thickness': 0.0015},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False

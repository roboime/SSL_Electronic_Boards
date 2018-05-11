designFile = "C:/Users/estagiario02/Desktop/SSL_Electronic_Boards/SSL_Electronic_Boards/Motor_Driver_2018/PDNAnalyzer_Output/Motor_Driver_2018PCB/odb.tgz"

powerNets = ["VCC", "MA"]

groundNets = ["GND", "MB"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("CON-MC2", "3") ],
"ground_pins": [ ("CON-MC2", "4") ],
"voltage": 8,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("CON-MC2", "2") ],
"ground_pins": [ ("CON-MC2", "1") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
]


voltage_regulators = [
{
"id": "2",
"type": "linear",

"in": [ ("IC", "23"), ("IC", "18"), ("IC", "17"), ("IC", "3"), ("IC", "4"), ("IC", "9") ],
"out": [ ("IC", "14"), ("IC", "13"), ("IC", "16"), ("IC", "15") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.4E-06,
}
,
{
"id": "3",
"type": "linear",

"in": [ ("IC", "26"), ("IC", "20"), ("IC", "24"), ("IC", "25"), ("IC", "11"), ("IC", "10"), ("IC", "7"), ("IC", "12") ],
"out": [ ("IC", "1"), ("IC", "2"), ("IC", "27"), ("IC", "28") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.66666666666667E-06,
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

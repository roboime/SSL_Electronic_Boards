designFile = "C:/Users/Public/Documents/Altium/Projects/Mother_Board_SSL2018/PDNAnalyzer_Output/Mother_board_SSL2018/odb.tgz"

powerNets = ["NetBAT_0", "VBAT", "NetFM_M0_2", "NetC1_M0_2", "MA_M0", "NetFM_M1_2", "NetC1_M1_2", "MA_M1", "NetFM_M2_2", "NetC1_M2_2", "MA_M2", "NetFM_M3_2", "NetC1_M3_2", "MA_M3", "NetDF_2", "NetCON_DM_1", "DA"]

groundNets = ["GND", "MB_M0", "MB_M1", "MB_M2", "MB_M3", "DB"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("BAT", "0") ],
"ground_pins": [ ("BAT", "1") ],
"voltage": 8.4,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("06x01_Conector_Male_M0", "5") ],
"ground_pins": [ ("06x01_Conector_Male_M0", "6") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("06x01_Conector_Male_M1", "5") ],
"ground_pins": [ ("06x01_Conector_Male_M1", "6") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("06x01_Conector_Male_M2", "5") ],
"ground_pins": [ ("06x01_Conector_Male_M2", "6") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("06x01_Conector_Male_M3", "5") ],
"ground_pins": [ ("06x01_Conector_Male_M3", "6") ],
"current": 7,
"Rpin": 0.0142857142857143,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("CON_DRIBLE", "2") ],
"ground_pins": [ ("CON_DRIBLE", "1") ],
"current": 8,
"Rpin": 0.0125,
}
]


voltage_regulators = [
{
"id": "6",
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
"id": "7",
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
"id": "8",
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
"id": "9",
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
"id": "10",
"type": "linear",

"in": [ ("M0-MOTOR", "3") ],
"out": [ ("M0-MOTOR", "0") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "11",
"type": "linear",

"in": [ ("R11_M1", "2") ],
"out": [ ("R11_M1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "12",
"type": "linear",

"in": [ ("FM_M1", "2") ],
"out": [ ("FM_M1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "13",
"type": "linear",

"in": [ ("M3-MOTOR", "2") ],
"out": [ ("M3-MOTOR", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "14",
"type": "linear",

"in": [ ("M3-MOTOR", "3") ],
"out": [ ("M3-MOTOR", "0") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "15",
"type": "linear",

"in": [ ("R11_M2", "2") ],
"out": [ ("R11_M2", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "16",
"type": "linear",

"in": [ ("FM_M2", "2") ],
"out": [ ("FM_M2", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "17",
"type": "linear",

"in": [ ("M1-MOTOR", "2") ],
"out": [ ("M1-MOTOR", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "18",
"type": "linear",

"in": [ ("M1-MOTOR", "3") ],
"out": [ ("M1-MOTOR", "0") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "19",
"type": "linear",

"in": [ ("R11_M3", "2") ],
"out": [ ("R11_M3", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "20",
"type": "linear",

"in": [ ("FM_M3", "2") ],
"out": [ ("FM_M3", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "21",
"type": "linear",

"in": [ ("M2-MOTOR", "2") ],
"out": [ ("M2-MOTOR", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "22",
"type": "linear",

"in": [ ("M2-MOTOR", "3") ],
"out": [ ("M2-MOTOR", "0") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "23",
"type": "linear",

"in": [ ("RD1", "2") ],
"out": [ ("RD1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "24",
"type": "linear",

"in": [ ("DF", "2") ],
"out": [ ("DF", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "25",
"type": "linear",

"in": [ ("DRIBLE-MOTOR", "1") ],
"out": [ ("DRIBLE-MOTOR", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "26",
"type": "linear",

"in": [ ("DRIBLE-MOTOR", "0") ],
"out": [ ("DRIBLE-MOTOR", "3") ],
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

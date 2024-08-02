XXX = 'a'

nav_params_home_to_elevators_waiting_point = [
    {
        'name': 'nav_to_basement_door_from_inside',
        'type': 'nav_to_point',
        'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'teleoperator_if_fail': True,
        'teleoperator_timeout': 60,
        'navigating_ui': XXX,
        'obstacle_ui': XXX,
    },
    {
        'name': 'basement_door_form_inside',
        'type': 'manual_door',
        'after_door_point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'tags_ids': [24, 56],
        'tags_family': '16h11',
        'tags_sizes': [0.08, 0.06],
        'call_timeout': 20.0,
        'call_user_id': XXX,
        'timeout': -1.0,
    },
    {
        'name': 'nav_to_elevators_waiting_point',
        'type': 'nav_to_point',
        'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'teleoperator_if_fail': True,
        'teleoperator_timeout': 60,
    },
]

nav_params_elevator_waiting_point_to_elevators = {
    '1': [{
        'name': 'nav_to_waiting_elevator',
        'type': 'nav_to_point',
        'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'teleoperator_if_fail': True,
        'teleoperator_timeout': 60,
    }],
    '2': [{
        'name': 'nav_to_waiting_elevator',
        'type': 'nav_to_point',
        'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'teleoperator_if_fail': True,
        'teleoperator_timeout': 60,
    }],
    '3': [{
        'name': 'nav_to_waiting_elevator',
        'type': 'nav_to_point',
        'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
        'teleoperator_if_fail': True,
        'teleoperator_timeout': 60,
    }],
}

SUPER_DICT = {
    'floor7':{
        'elev_to_7W':[

        ],
        'elev_to_7E':[

        ],
        '7W_to_7E':[

        ],
        # '7E_to_7W':[

        # ],
        '7W_to_elev':[

        ],
        '7E_to_elev':[

        ],
    },
    'floor2':{

    }
}


entregar en 7W
entregar en 7E
entregar en 7W y 7E


A B C D


elv -> A
elv -> B
elv -> C
elv -> D

A -> elv
B -> elv
C -> elv
D -> elv

A -> B
A -> C
A -> D

B -> C
B -> D

C -> D




nav_to_point = {
    'name': 'XxxxxxX',
    'type': 'nav_to_point',
    'point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
    'teleoperator_if_fail': True,
    'teleoperator_timeout': 60,
}

manual_door = {
    'name': 'XxxxxxX',
    'type': 'manual_door',
    'after_door_point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
    'tags_ids': [24, 56],
    'tags_family': '16h11',
    'tags_sizes': [0.08, 0.06],
    'call_timeout': 20.0,
    'call_user_id': XXX,
    'timeout': -1.0,
}

automatic_door = {
    'name': 'XxxxxxX',
    'type': 'automatic_door',
    'after_door_point': {'x':0.0, 'y':0.0, 'angle':0.0, 'units':0.0, 'nav_options': XXX},
    'tags_ids': [24, 56],
    'tags_family': '16h11',
    'tags_sizes': [0.08, 0.06],
    'timeout': -1.0,
}
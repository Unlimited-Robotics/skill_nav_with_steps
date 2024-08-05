TYPE_NAME = 'nav_to_point'

NAVIGATION_TRY_LIMIT = 1
OBSTACLE_DETECTION_THRESHOLDS = [2, 7]

SOUND_OBSTACLE_DETECTED_1 = {
        'path': 'res:Clear_the_way.mp3',
        'volume': 100,
    }
SOUND_OBSTACLE_DETECTED_2 = {
        'path': 'res:Clear_the_way2.mp3',
        'volume': 100,
    }

SOUNDS_OBSTACLES_DETECTED = [
    SOUND_OBSTACLE_DETECTED_1, 
    SOUND_OBSTACLE_DETECTED_2
]

LEDS_NOTIFY_OBSTACLE = {
    'group': 'head',
    'color': 'YELLOW',
    'animation': 'MALFUNCTION_VER_1',
    'speed': 1,
    'repetitions': 0,
}
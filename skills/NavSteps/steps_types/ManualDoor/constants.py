from ..AutomaticDoor.constants import *
TYPE_NAME = 'manual_door'

FLEET_CALL_MESSAGE = 'Please open the door for me'

FLEET_REQUEST_USER_ACTION = {
    'request_type': 'call',
    'request_args':{
        'message': FLEET_CALL_MESSAGE
    },
    'timeout': 1.0
}
                        
DOOR_CLOSE_TIMEOUT = 10.0
TIME_BEFORE_FIRST_CALL = 10.0
TIME_BEETWEEN_CALLS = 60.0 * 2 # 2 minutes

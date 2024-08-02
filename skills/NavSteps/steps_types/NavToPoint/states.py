from .errors import *


# The first state is always the initial one
STATES = [
        'END',
]

# First state of FSM, if not defined, the FSM starts in the first element of
# the STATES list
INITIAL_STATE = ''


# If the FSM falls into one of these states, the execution finishes.
END_STATES = []


# If one of the states takes more than an especified time, it aborts.
# Format: 'STATE': (<timeout>, <error_tuple>)
STATES_TIMEOUTS = {}

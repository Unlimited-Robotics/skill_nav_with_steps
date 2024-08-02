from raya.tools.fsm import FSM

from .actions import CommonActions
from .helpers import CommonHelpers
from .transitions import CommonTransitions

from .states import *
from .constants import *
from .errors import *


class CommonTypeFSM(FSM):
    def __init__(self, *args, **kwarg):
        super().__init__(*args, **kwarg)

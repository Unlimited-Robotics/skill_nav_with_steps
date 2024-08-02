from raya.tools.fsm import FSM
from raya.logger import RaYaLogger

from .actions import CommonActions
from .helpers import CommonHelpers
from .transitions import CommonTransitions

from .states import *
from .constants import *
from .errors import *

class CommonTypeFSM(FSM):
    def __init__(self, *args, **kwarg):
        self.step = kwarg.pop('self_object')
        self.log = RaYaLogger(
            name=self.step.name,
        )
        super().__init__(*args, **kwarg)

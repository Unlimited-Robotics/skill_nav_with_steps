import typing

from raya.tools.fsm import BaseTransitions

if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from .errors import *
from .constants import *
from .helpers import CommonHelpers, Helpers


class CommonTransitions(BaseTransitions):

    def __init__(self, app: 'RayaApplication', helpers: CommonHelpers):
        super().__init__()
        self.app = app
        self.helpers = helpers
        self._log = self.helpers._log

    async def SETUP(self):
        self._log.debug('Transition SETUP')
        self.set_state('END')

    
    async def END(self):
        # this will not be executed, the FSM finished as soon the END state is reached
        self._log.debug('Transition END')


class Transitions(CommonTransitions):

    def __init__(self, app: 'RayaApplication', helpers: Helpers):
        super().__init__(app=app, helpers=helpers)

import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication

# from ..CommonType import CommonTransitions
from ...PartialsFSM.RetryState import Transitions as RetryTransitions

from .errors import *
from .constants import *
from .helpers import Helpers


class Transitions(RetryTransitions):

    def __init__(self, app: 'RayaApplication', helpers: Helpers):
        RetryTransitions.__init__(self=self, app=app, helpers=helpers)
        self.helpers: Helpers


    async def SETUP(self):
        self.set_state('NAVIGATING_TO_POINT')


    async def NAVIGATING_TO_POINT(self):
        if not self.app.nav.is_navigating():
            nav_error = self.app.nav.get_last_result()
            if nav_error[0] == 0:
                self.set_state('END')
            else:
                self.helpers.retry_step(
                    last_state='NAVIGATING_TO_POINT',
                    transitions=self
                )


    async def END(self):
        await super().END()
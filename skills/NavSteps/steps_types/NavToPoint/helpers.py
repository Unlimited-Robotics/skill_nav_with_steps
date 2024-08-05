import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication
    from . import NavToPointFSM

# from ..CommonType import CommonHelpers
from ...PartialsFSM.RetryState import Helpers as RetryHelpers

from .errors import *
from .constants import *


class Helpers(RetryHelpers):

    def __init__(self, app: 'RayaApplication'):
        RetryHelpers.__init__(self=self, app=app)
        self._fsm: NavToPointFSM = None


    async def nav_feedback_async(self, code, msg, distance, speed):
        self.log.debug(
            'nav_feedback_async: '
            f'{code}, {msg}, {distance}, {speed}'
        )
        
    async def nav_finish_async(self, code, msg):
        self.log.debug(
            f'nav_finish_async: {code}, {msg}'
        )

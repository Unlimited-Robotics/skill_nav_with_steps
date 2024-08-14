import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication
    from . import ManualDoorFSM

import datetime

from raya.exceptions import RayaFleetTimeout

from ..AutomaticDoor import Helpers as AutomaticDoorHelpers
from .errors import *
from .constants import *


class Helpers(AutomaticDoorHelpers):

    def __init__(self, app: 'RayaApplication'):
        super().__init__(app=app)
        self._fsm: ManualDoorFSM = None
        self.__door_open_timeout = datetime.datetime.now()
        self.task_timer_call_for_help = 'timer_call_for_help'


    async def start_door_close_timeout(self):
        self.__door_open_timeout = datetime.datetime.now()


    async def check_door_close_timeout(self):
        if self.__door_open_timeout - datetime.datetime.now() > \
                datetime.timedelta(seconds=DOOR_CLOSE_TIMEOUT):
            return True
        return False


    async def call_task(self):
        await self.app.sleep(TIME_BEFORE_FIRST_CALL)
        while True:
            user = self._fsm.step.phone_call_user_id
            self.log.warn(f'Calling the user \'{user}\'...')
            try:
                await self.app.fleet.request_user_action(
                        user_id=user,
                        wait=True,
                        **FLEET_REQUEST_USER_ACTION,
                    )
            except RayaFleetTimeout:
                pass

            await self.app.sleep(TIME_BEETWEEN_CALLS)
            self.log.debug((
                'Calling again... '
                f'after {TIME_BEETWEEN_CALLS} seconds.'
            ))


    async def nav_feedback_async(self, code, msg, distance, speed):
        await super().nav_feedback_async(
            code=code, 
            msg=msg, 
            distance=distance, 
            speed=speed
        )


    async def nav_finish_async(self, code, msg):
        await super().nav_finish_async(code=code, msg=msg)

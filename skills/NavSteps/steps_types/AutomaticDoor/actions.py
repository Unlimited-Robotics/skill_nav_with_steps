import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from raya.exceptions import RayaNavAlreadyNavigating

from ..CommonType import CommonActions

from .errors import *
from .constants import *
from .helpers import Helpers


class Actions(CommonActions):

    def __init__(self, app: 'RayaApplication', helpers: Helpers):
        super().__init__(app=app, helpers=helpers)
        self.helpers: Helpers
    

    async def enter_SETUP(self):
        self.helpers.withinInitialZone = await self.app.nav.is_in_zone(
                zone_name=self.helpers._fsm.step.zone_name
            )
        self.log.warn('1')
        await self.helpers.enable_cameras()
        self.log.warn('2')
        await self.helpers._enable_door_detection()
        self.log.warn('3')


    async def enter_WAIT_FOR_DOOR_OPEN(self):
        pass


    async def leave_WAIT_FOR_DOOR_OPEN(self):
        pass


    async def enter_NAVIGATE_THROUGH_DOOR(self):
        # if self.app.nav.is_navigating():
        #     await self.app.nav.update_current_nav_goal(
        #         **self.helpers._fsm.step.after_door_point.get_only_coordinates(),
        #     )
        # else:
        point = self.helpers._fsm.step.after_door_point.to_dict()
        self.log.debug(f'Navigating to point: {point}')
        try:
            await self.app.nav.navigate_to_position(
                **point,
                callback_feedback_async=self.helpers.nav_feedback_async,
                callback_finish_async=self.helpers.nav_finish_async,
            )
        except RayaNavAlreadyNavigating:
            self.log.error('RayaNavAlreadyNavigating')
        await self.app.ui.show_last_animation()

    
    async def leave_NAVIGATE_THROUGH_DOOR(self):
        pass

    
    async def enter_END(self):
        self.log.debug('Entering END')
        await self.helpers._disable_door_detection()
        await self.helpers.disable_cameras()

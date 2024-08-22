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
        
        self.__navigating_leds_on = False
        
        self.__obstacle_tries = 0
        self.__navigating_tries = 0
        
        self.last_code = -1
        self.remaining_distance = -1
        self.listen_feedback = False


    def reset_last_nav(self):
        self.listen_feedback = False
        self.remaining_distance = -1


    async def nav_feedback_async(self, code, msg, distance, speed):
        if code in [0, 1, 4]:
            self.listen_feedback = True
        if not self.listen_feedback:
            return
        
        await super().nav_feedback_async(
            code=code, 
            msg=msg, 
            distance=distance, 
            speed=speed
        )
        
        self.remaining_distance = distance
        if self.last_code == code and code not in NAV_CODES_IS_NAVIGATING:
            return
        else:
            self.last_code = code
        
        if code in NAV_CODES_IS_NAVIGATING:
            if self.__obstacle_tries != 0:
                self.log.warn(
                        'Navigation tries limit reached, '
                        'resetting obstacle tries to 0'
                    )
                self.__obstacle_tries = 0
            
            if self.__navigating_leds_on is False:
                self.log.warn('Gary is navigating...')
                await self.custom_animation(
                    **LEDS_NAVIGATING,
                    wait=False
                )
                await self.app.ui.show_last_animation()
                self.__navigating_leds_on = True
            
            self.__navigating_tries += 1

        elif code in NAV_CODES_OBSTACLE_DETECTED:
            self.__obstacle_tries += 1
            self.__navigating_tries = 0
            self.__navigating_leds_on = False
            
            self.log.warn(f'Obstacle detected counter: {self.__obstacle_tries}')
            
            await self.app.ui.show_animation(
                **self._fsm.step.custom_ui_screen_obstacle,
                dont_save_last_ui=True
            )

        if self.__obstacle_tries > 0:
            if self.__obstacle_tries >= OBSTACLE_DETECTION_THRESHOLDS[1]:
                self.log.error('Obstacle severity 2')
                await self.gary_play_audio_predefined(
                    audio=SOUNDS_OBSTACLES_DETECTED[1],
                    animation_head_leds=LEDS_NOTIFY_OBSTACLE,
                )
            elif self.__obstacle_tries >= OBSTACLE_DETECTION_THRESHOLDS[0]:
                self.log.error('Obstacle severity 1')
                await self.gary_play_audio_predefined(
                    audio=SOUNDS_OBSTACLES_DETECTED[0],
                    animation_head_leds=LEDS_NOTIFY_OBSTACLE
                )


    async def nav_finish_async(self, code, msg):
        await super().nav_finish_async(code=code, msg=msg)
        await self.custom_turn_off_leds()
        await self.custom_cancel_sound()

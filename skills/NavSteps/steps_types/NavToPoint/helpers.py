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


    async def nav_feedback_async(self, code, msg, distance, speed):
        await super().nav_feedback_async(
            code=code, 
            msg=msg, 
            distance=distance, 
            speed=speed
        )
        
        self.remaining_distance = distance
        
        if self.last_code == code:
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
                await self.custom_turn_off_leds()
                await self.custom_cancel_sound()
            
            if self.__navigating_leds_on is False:
                await self.app.ui.show_last_animation()
                await self.custom_animation(
                    **LEDS_NAVIGATING,
                    wait=False
                )
                self.__navigating_leds_on = True
            
            self.__navigating_tries += 1

        elif code == NAV_CODES_OBSTACLE_DETECTED:
            self.__obstacle_tries += 1
            self.__navigating_tries = 0
            self.__navigating_leds_on = False

        
            if self.__obstacle_tries >= OBSTACLE_DETECTION_THRESHOLDS[1]:
                self.log.error(
                    'Obstacle detected more than' 
                    f' {OBSTACLE_DETECTION_THRESHOLDS[1]} times'
                )
                await self.gary_play_audio(
                    audio=SOUNDS_OBSTACLES_DETECTED[1],
                    animation_head_leds=LEDS_NOTIFY_OBSTACLE,
                )
            elif self.__obstacle_tries >= OBSTACLE_DETECTION_THRESHOLDS[0]:
                self.log.error(
                    'Obstacle detected more than '
                    f'{OBSTACLE_DETECTION_THRESHOLDS[0]} times'
                )
                await self.gary_play_audio(
                    audio=SOUNDS_OBSTACLES_DETECTED[0],
                    animation_head_leds=LEDS_NOTIFY_OBSTACLE
                )
        
            if not self.app.sound.is_playing():
                await self.custom_turn_off_leds()


    async def nav_finish_async(self, code, msg):
        await super().nav_finish_async(code=code, msg=msg)

import typing
import logging
if typing.TYPE_CHECKING:
    from src.app import RayaApplication
    from . import CommonFSM

from raya.logger import RaYaLogger


class CommonHelpers():
    
    def __init__(self, app: 'RayaApplication'):
        self.app = app
        self._fsm: CommonFSM
        self.log: RaYaLogger


    def __setattr__(self, name, value):
        if name == '_fsm':
            super().__setattr__(name, value)
            if value is not None:
                self._log = value
        else:
            super().__setattr__(name, value)


    def get_logger(self) -> RaYaLogger:
        return self._fsm.log
    

    @property
    def log(self):
        return self.get_logger()


    async def custom_cancel_sound(self):
        try:
            await self.app.sound.cancel_all_sounds()
        except Exception:
            pass


    async def custom_animation(self, wait=True, **kwargs):
        try:
            await self.app.leds.animation(**kwargs, wait=wait)
        except Exception:
            pass


    async def custom_turn_off_leds(self, group = ''):
        if group != '':
            try:
                await self.app.leds.turn_off_group(group)
            except Exception:
                pass
        else:
            try:
                await self.app.leds.turn_off_all()
            except Exception:
                pass

import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from raya.logger import RaYaLogger
from raya.exceptions import *


class CommonHelpers:
    
    def __init__(self, app: 'RayaApplication'):
        self.app = app
        self.log: RaYaLogger = None


    def get_logger(self) -> RaYaLogger:
        try:
            name=self._fsm.step.name
            self.log = RaYaLogger(name=name)
        except AttributeError:
            self.log = self._fsm.log
        return self.log


class Helpers(CommonHelpers):

    def __init__(self, app: 'RayaApplication'):
        super().__init__(app)

import typing
if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from raya.logger import RaYaLogger
from raya.exceptions import *


class CommonHelpers:
    
    def __init__(self, app: 'RayaApplication', name='CommonFSM'):
        self.app = app
        self._log = RaYaLogger(name)


class Helpers(CommonHelpers):

    def __init__(self, app: 'RayaApplication'):
        super().__init__(app)

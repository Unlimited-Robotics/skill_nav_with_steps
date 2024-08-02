import typing

from raya.logger import RaYaLogger
from raya.exceptions import *

if typing.TYPE_CHECKING:
    from src.app import RayaApplication


class CommonHelpers:

    def __init__(self, app: 'RayaApplication', name='common_fsm'):        
        self.app = app
        self._log = RaYaLogger(name)

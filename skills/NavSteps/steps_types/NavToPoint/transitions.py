import typing

from raya.tools.fsm import BaseTransitions

if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from .errors import *
from .constants import *
from .helpers import CommonHelpers


class CommonTransitions(BaseTransitions):

    def __init__(self, app: 'RayaApplication', helpers: CommonHelpers):
        super().__init__()
        self.app = app
        self.helpers = helpers
        self._log = self.helpers._log

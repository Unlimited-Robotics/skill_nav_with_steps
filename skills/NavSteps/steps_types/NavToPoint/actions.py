import typing

from raya.tools.fsm import BaseActions

if typing.TYPE_CHECKING:
    from src.app import RayaApplication

from .helpers import CommonHelpers


class CommonActions(BaseActions):

    def __init__(self, app: 'RayaApplication', helpers: CommonHelpers):
        super().__init__()
        self.app = app
        self.helpers = helpers
        self._log = self.helpers._log


    async def aborted(self, error, msg):
        pass

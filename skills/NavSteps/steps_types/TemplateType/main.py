from ..CommonType.main import CommonType
from . import TemplateFSM

from .constants import *

class Template(CommonType):

    def __init__(self,
            name: str,
        ) -> None:
        super().__init__(name=name, type=TYPE_NAME)
        self.fsm = TemplateFSM(
            self_object=self,
            name='TemplateFSM', 
            log_transitions=True,
        )

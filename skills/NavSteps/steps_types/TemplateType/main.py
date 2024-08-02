from ..CommonType.main import CommonType
from . import TemplateFSM

from .constants import *

class Template(CommonType):

    def __init__(self,
            name: str,
        ) -> None:
        self.name = name
        self.type = TYPE_NAME
        self.fsm = TemplateFSM(
            self_object=self,
            name='TemplateFSM', 
            log_transitions=True,
        )

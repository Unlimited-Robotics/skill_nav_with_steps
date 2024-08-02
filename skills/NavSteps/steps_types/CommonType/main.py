from raya.logger import RaYaLogger

from . import CommonTypeFSM

class CommonType:
    
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self.fsm = CommonTypeFSM(
            self_object=self,
            name=self.name, 
            log_transitions=True,
        )

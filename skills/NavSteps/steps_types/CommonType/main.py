from raya.logger import RaYaLogger

from . import CommonTypeFSM

class CommonType:
    
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type
        self._log = RaYaLogger(
            name=name
        )
        self.fsm = CommonTypeFSM(
            name='CommonFSMType', 
            log_transitions=True,
        )

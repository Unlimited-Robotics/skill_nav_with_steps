from typing import NoReturn, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app import RayaApplication
    from .transitions import Transitions

from ..CommonFSM import CommonHelpers
from .constants import *

class Helpers(CommonHelpers):
    
    def __init__(self, app: RayaApplication):
        super().__init__(app=app)
        
        self._last_failed_state = ''
        self._last_failed_state_counter = 1


    def reset_retry_counter(self):
        self._last_failed_state_counter = 1


    def max_retry_reached(self):
        counter = self._last_failed_state_counter > \
            MAX_RETRY_COUNTER_REQUEST_FOR_HELP
        self.log.debug((
            f'current try: {self._last_failed_state_counter} '
            f'of {MAX_RETRY_COUNTER_REQUEST_FOR_HELP}'
        ))
        return counter


    def increase_retry_counter(self):
        self._last_failed_state_counter += 1

        
    def __set_last_failed_state(self, state: str):
        if self._last_failed_state != state:
            self.reset_retry_counter()
        self._last_failed_state = state


    def _get_last_failed_state(self):
        return self._last_failed_state


    def set_state_wrapper(self,
            new_state:str,
            transitions: Transitions, 
            last_state:str = ''
        ) -> NoReturn:
        if last_state != '':
            self.__set_last_failed_state(last_state)
        transitions.set_state(new_state)

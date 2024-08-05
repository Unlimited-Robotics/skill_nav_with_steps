import inspect

from typing import NoReturn, TYPE_CHECKING
if TYPE_CHECKING:
    from src.app import RayaApplication
    from .transitions import Transitions

from ..CommonFSM import CommonHelpers
from .constants import *
from .states import *

class Helpers(CommonHelpers):
    
    def __init__(self, app: 'RayaApplication'):
        super().__init__(app=app)
        
        self._last_failed_state = ''
        self._last_failed_state_counter = 1
        self.max_tries = MAX_RETRY_COUNTER_REQUEST_FOR_HELP


    def reset_retry_counter(self):
        self._last_failed_state_counter = 1


    def max_retry_reached(self):
        counter = self._last_failed_state_counter > self.max_tries
        if counter:
            self.log.error((
                f'Maximum tries reached for state: '
                f'{self._last_failed_state}'
            ))
        else:
            self.log.debug((
                f'current try: {self._last_failed_state_counter} '
                f'of {self.max_tries}'
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


    def retry_step(self,
            transitions,
            last_state:str = '',
            max_tries: int = MAX_RETRY_COUNTER_REQUEST_FOR_HELP
        ) -> NoReturn:
        self.max_tries = max_tries
        if last_state != '':
            self.__set_last_failed_state(last_state)
        transitions.set_state(INITIAL_STATE)

from typing import Union, List

from raya.skills import RayaFSMSkill
from raya.tools.fsm import RayaFSMAborted

from raya.controllers.navigation_controller import NavigationController

from .steps_types import *
from .constants import *
from .errors import *


class SkillNavSteps(RayaFSMSkill):

    DEFAULT_SETUP_ARGS = {

    }
    
    REQUIRED_SETUP_ARGS = {
        
    }
    
    DEFAULT_EXECUTE_ARGS = {
        
    }
    
    REQUIRED_EXECUTE_ARGS = {
        'steps',
    }
    
###############################################################################
###########################    FSM states     #################################
###############################################################################

    STATES = [
        'SETUP_STEPS',
        'EXECUTE_STEPS',
        'END',
    ]

    INITIAL_STATE = 'SETUP_STEPS'

    END_STATES = [
        'END'
    ]
    
    STATES_TIMEOUTS = {}


###############################################################################
###########################   SKILL METHODS   #################################
###############################################################################


    async def setup(self):
        self.nav:NavigationController = \
            await self.enable_controller('navigation')
        self._steps: List[Union[NavToPoint, ManualDoor,AutomaticDoor]] = []

    
    async def finish(self):
        await self.send_feedback('RayaSkill.finish')


###############################################################################
##########################      HELPERS      ##################################
###############################################################################

###############################################################################
#########################      ACTIONS       ##################################
###############################################################################
    
    
    async def enter_SETUP_STEPS(self):
        for step in self.execute_args['steps']:
            step_name = step.get('name')
            step_type = step.get('type')
            
            self.log.warn((
                f'Initializing step... Name:\'{step_name}\', '
                f'Type \'{step_type}\''
            ))
            if step_type == NAV_TO_POINT_TYPE_NAME:
                nav_to_point_step = NavToPoint(
                    name = step.get('name'),
                    point = step.get('point'),
                    teleoperator_if_fail = step.get('teleoperator_if_fail'),
                    teleoperator_timeout = step.get('teleoperator_timeout'),
                )
                self._steps.append(nav_to_point_step)
            elif step_type == MANUAL_DOOR_TYPE_NAME:
                manual_door = ManualDoor(
                    name = step.get('name'),
                    after_door_point = step.get('after_door_point'),
                    target_ids = step.get('target_ids'),
                    tags_sizes = step.get('tags_sizes'),
                    tags_family = step.get('target_ids'),
                    phone_call_timeout = step.get('phone_call_timeout'),
                    call_user_id = step('call_user_id'),
                    timeout = step.get('timeout')
                )
                self._steps.append(manual_door)
            elif step_type == AUTOMATIC_DOOR_TYPE_NAME:
                automatic_door = AutomaticDoor(
                    name = step.get('name'),
                    after_door_point = step.get('after_door_point'),
                    target_ids = step.get('target_ids'),
                    tags_sizes = step.get('tags_sizes'),
                    tags_family = step.get('target_ids'),
                    timeout = step.get('timeout')
                )
                self._steps.append(automatic_door)
            elif step_type == TEST_TYPE_NAME:
                test = CommonType(
                    name=step.get('name'),
                    type=step.get('type')
                )
                self._steps.append(test)
            else:
                self.log.error((
                    f'step... Name:\'{step_name}\', '
                    f'Type \'{step_type}\' not valid'
                ))
                self.abort(*ERROR_STEP_NOT_VALID)

            self.log.debug(f'Step \'{step_name}\' initialized successfully')
        self.log.debug('All steps initialized successfully')


    async def enter_EXECUTE_STEPS(self):
        pass


###############################################################################
#########################    TRASITIONS      ##################################
###############################################################################

    async def transition_from_SETUP_STEPS(self):
        self.set_state('EXECUTE_STEPS')
        

    async def transition_from_EXECUTE_STEPS(self):
        for step in self._steps:
            try:
                await step.fsm.run_and_await()
            except RayaFSMAborted as error:
                self.log.error((
                    f'Step \'{step.name}\' Aborted with '
                    f'Error code: \'{error.error_code}\' '
                    f'Error msg: \'{error.error_msg}\''
                ))
                self.abort(error)

        self.set_state('END')

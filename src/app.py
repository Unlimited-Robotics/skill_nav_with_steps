from raya.application_base import RayaApplicationBase
from raya.exceptions import RayaSkillAborted

from skills.NavSteps import SkillNavSteps
from .constants import EXAMPLE_STEPS

from raya.controllers.navigation_controller import NavigationController

class RayaApplication(RayaApplicationBase):

    async def setup(self):
        self.nav:NavigationController = \
            await self.enable_controller('navigation')

        self.skill_nav_steps = self.register_skill(SkillNavSteps)
        
        setup_args = {}
        result = await self.skill_nav_steps.execute_setup(
            setup_args=setup_args
        )
        self.log.warn(f'setup result: {result}')
        
        
        execute_args = {
            'steps': EXAMPLE_STEPS
        }
        await self.skill_nav_steps.execute_main(
            execute_args=execute_args,
            callback_done=self.cb_skill_done,
            callback_feedback=self.cb_skill_feedback,
            wait=False
        )


    async def loop(self):
        try:
            result = await self.skill_nav_steps.wait_main()
            self.log.warn(f'skill_template result: {result}')

            result = await self.skill_nav_steps.execute_finish()
            self.log.warn(f'skill_template finish result: {result}')

        except RayaSkillAborted as e:
            self.log.error((
                'Skill aborted with '
                f'Error code: \'{e.error_code}\', '
                f'Error msg: \'{e.error_msg}\'.'
            ))

        while True:
            await self.sleep(1)
            self.log.debug(f'RayaApplication.loop')


    async def finish(self):
        self.log.info(f'RayaApplication.finish')


    async def cb_skill_done(self, exception, result):
        self.log.debug(
            f'Callback skill done: '
            f'Exception: \'{exception}\', '
            f'Result: \'{result}\'.'
        )


    async def cb_skill_feedback(self, feedback):
        self.log.debug(
            f'Callback Feedback: \'{feedback}\''
        )


    def get_arguments(self):
        pass

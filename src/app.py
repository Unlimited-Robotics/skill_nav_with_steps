from raya.application_base import RayaApplicationBase
from raya.exceptions import RayaSkillAborted
from raya.exceptions import RayaCommandTimeout

from skills.NavSteps import SkillNavSteps
from .constants import EXAMPLE_STEPS

from raya.controllers.navigation_controller import NavigationController
from raya.controllers.leds_controller import LedsController
from raya.controllers.sound_controller import SoundController
from raya.controllers.ui_controller import UIController
from raya.controllers.fleet_controller import FleetController
from raya.controllers.sensors_controller import SensorsController
from raya.controllers.motion_controller import MotionController
from raya.controllers.cameras_controller import CamerasController
from raya.controllers.cv_controller import CVController
from raya.controllers.robot_skills_controller import RobotSkillsController


GARY_SELECTED_CART_FOOTPRINT =  [
        [-1.22,  0.22],
        [-0.24,  0.22],
        [-0.24,  0.27],
        [ 0.24,  0.27],
        [ 0.24, -0.27],
        [-0.24, -0.27],
        [-0.24, -0.22],
        [-1.22, -0.22],
    ]


class RayaApplication(RayaApplicationBase):

    async def setup(self):
        self.nav:NavigationController = \
            await self.enable_controller('navigation')
        self.nav:NavigationController = \
                await self.enable_controller('navigation')
        self.leds:LedsController  = \
                await self.enable_controller('leds')
        self.sound:SoundController = \
                await self.enable_controller('sound')
        self.ui:UIController = \
                await self.enable_controller('ui')
        self.fleet:FleetController = \
                await self.enable_controller('fleet')
        self.sensors:SensorsController = \
                await self.enable_controller('sensors')
        self.motion:MotionController = \
                await self.enable_controller('motion')
        self.cameras: CamerasController = \
                await self.enable_controller('cameras')
        self.cv: CVController = \
                await self.enable_controller('cv')
        self.robot_skills: RobotSkillsController = \
                await self.enable_controller('robot_skills')

        try:
            await self.nav.update_robot_footprint(
                    points=GARY_SELECTED_CART_FOOTPRINT
                )
            await self.nav.change_costmap(costmap_name='cost.home_elev')
        except RayaCommandTimeout:
            pass

        self.skill_nav_steps = self.register_skill(SkillNavSteps)
        
        setup_args = {}
        result = await self.skill_nav_steps.execute_setup(
            setup_args=setup_args
        )
        self.log.warn(f'setup result: {result}')
        
        await self.ui.show_animation(
            title = 'Hello! i am Raya',
            lottie =  'res:lottie_package_walking.json',
        )


    async def main(self):
        execute_args = {
            'args': {
                'user_id': '0e89dc8f-a2c9-4288-ae7b-69946afa4557',
            },
            'steps': EXAMPLE_STEPS
        }
        await self.skill_nav_steps.execute_main(
            execute_args=execute_args,
            callback_done=self.cb_skill_done,
            callback_feedback=self.cb_skill_feedback,
            wait=False
        )
        
        try:
            result = await self.skill_nav_steps.wait_main()
            self.log.warn(f'skill_template result: {result}')

        except RayaSkillAborted as e:
            self.log.error((
                'Skill aborted with '
                f'Error code: \'{e.error_code}\', '
                f'Error msg: \'{e.error_msg}\'.'
            ))

        for _ in range(10):
            await self.sleep(1)
            self.log.debug(f'RayaApplication.loop')


    async def finish(self):
        self.log.info(f'RayaApplication.finish')
        result = await self.skill_nav_steps.execute_finish()
        self.log.warn(f'skill_template finish result: {result}')


    async def cb_skill_done(self, exception, result):
        self.log.debug(
            f'Callback skill done: '
            f'Result: \'{result}\'.'
        )


    async def cb_skill_feedback(self, feedback):
        self.log.debug(
            f'Callback Feedback: \'{feedback}\''
        )


    def get_arguments(self):
        pass

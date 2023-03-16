import os
import warnings

from .mujoco_multi import MujocoMulti
from .coupled_half_cheetah import CoupledHalfCheetah
from .manyagent_swimmer import ManyAgentSwimmerEnv
from .manyagent_ant import ManyAgentAntEnv

warnings.warn("This code base is no longer maintained, and is not expected to be maintained again in the future. \n"
              "For updated and maintained versions of these environments, please refer to Gymnasium Robotics (see https://robotics.farama.org/). \n"
              "This maintained version includes documentation, support for the PettingZoo APi, current versions of Python, various bug fixes, "
              "and other quality of life improvements. \n"
              "We encourage researchers to switch to the maintained version for all purposes other than comparing to results ran on this version of the environments. \n")

if os.getenv('SUPPRESS_GR_PROMPT') != '1':
    input("Please read the raised warning, then press Enter to continue... (to suppress this prompt, please set the environment variable `SUPPRESS_GR_PROMPT=1`)\n")

from setuptools import setup

setup(name='multiagent_mujoco',
      version='2.0.1',
      install_requires=['gym==0.10.8', 'torch', 'mujoco_py']  # And any other dependencies foo needs
      )
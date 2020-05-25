```diff
-  Please contact Christian Schroeder de Witt at cs@robots.ox.ac.uk for any questions
-  Issues? Please file them here. Thanks :)
```

# Multi-Agent Mujoco
Benchmark for Continuous Multi-Agent Robotic Control, based on OpenAI's Mujoco Gym environments.

Described in the paper [Deep Multi-Agent Reinforcement Learning for Decentralized Continuous Cooperative Control](https://arxiv.org/abs/2003.06709) by Christian Schroeder de Witt, Bei Peng, Pierre-Alexandre Kamienny, Philip Torr, Wendelin Böhmer and Shimon Whiteson, Torr Vision Group and Whiteson Research Lab, University of Oxford, 2020

# Installation

**Note: You require OpenAI Gym Version 10.8.0 and Mujoco 2.0**

Simply clone this repository and put ./src on your PYTHONPATH.
To render, please also set the following environment variables:

```
LD_LIBRARY_PATH=${HOME}/.mujoco/mujoco200/bin;
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
```

# Example

```python
from src.multiagent_mujoco.mujoco_multi import MujocoMulti
import numpy as np
import time


def main():
    env_args = {"scenario": "HalfCheetah-v2",
                  "agent_conf": "2x3",
                  "agent_obsk": 0,
                  "episode_limit": 1000}
    env = MujocoMulti(env_args=env_args)
    env_info = env.get_env_info()

    n_actions = env_info["n_actions"]
    n_agents = env_info["n_agents"]
    n_episodes = 10

    for e in range(n_episodes):
        env.reset()
        terminated = False
        episode_reward = 0

        while not terminated:
            obs = env.get_obs()
            state = env.get_state()

            actions = []
            for agent_id in range(n_agents):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.uniform(-1.0, 1.0, n_actions)
                actions.append(action)

            reward, terminated, _ = env.step(actions)
            episode_reward += reward

            time.sleep(0.1)
            env.render()


        print("Total reward in episode {} = {}".format(e, episode_reward))

    env.close()

if __name__ == "__main__":
    main()
```

# Documentation

## Environment config

* *env_args.scenario*: Determines the underlying single-agent OpenAI Gym Mujoco environment
* *env_args.agent_conf*: Determines the partitioning (see in Environment section below), fixed by n_agents x motors_per_agent
* *env_args.agent_obsk*: Determines up to which connection distance k agents will be able to form observations (0: agents can only observe the state of their own joints and bodies, 1: agents can observe their immediate neighbour's joints and bodies).
* *env_args.k_categories*: A string describing which properties are observable at which connection distance as comma-separated lists separated by vertical bars. For example, "qpos,qvel,cfrc_ext,cvel,cinert,qfrc_actuator|qpos" means k=0 can observe properties qpos,qvel,cfrc_ext,cvel,cinert,qfrc_actuator and k>=1 (i.e. immediate and more distant neighbours) can be observed through property qpos. Note: If a property requested is not available for a given agent, it will be silently omitted.
* *env_args.global_categories*: Same as env_args.k_categories, but concerns some global properties that are otherwise not observed by any of the agents. Switched off by default (i.e. agents have no non-local observations).

# Built-in Tasks 

Tasks can be trivially extended by adding entries in src/multiagent_mujoco/obsk.py.

<img src="https://github.com/schroederdewitt/multiagent_mujoco/blob/master/docs/images/mamujoco.png" width="900" height="384">

## Task configuration

### 2-Agent Ant

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="2x4"
env_args.agent_obsk=1
```

### 2-Agent Ant Diag

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="2x4d"
env_args.agent_obsk=1
```

### 4-Agent Ant

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="2x4"
env_args.agent_obsk=1
```

### 2-Agent HalfCheetah

```python
env_args.scenario="HalfCheetah-v2"
env_args.agent_conf="2x3"
env_args.agent_obsk=1
```

### 6-Agent HalfCheetah

```python
env_args.scenario="HalfCheetah-v2"
env_args.agent_conf="6x1"
env_args.agent_obsk=1
```

### 3-Agent Hopper

```python
env_args.scenario="Hopper-v2"
env_args.agent_conf="3x1"
env_args.agent_obsk=1
```

### 2-Agent Humanoid

```python
env_args.scenario="Humanoid-v2"
env_args.agent_conf="9|8"
env_args.agent_obsk=1
```

### 2-Agent HumanoidStandup

```python
env_args.scenario="HumanoidStandup-v2"
env_args.agent_conf="9|8"
env_args.agent_obsk=1
```

### 2-Agent Reacher

```python
env_args.scenario="Reacher-v2"
env_args.agent_conf="2x1"
env_args.agent_obsk=1
```

### 2-Agent Swimmer

```python
env_args.scenario="Swimmer-v2"
env_args.agent_conf="2x1"
env_args.agent_obsk=1
```

### 2-Agent Walker

```python
env_args.scenario="Walker-v2"
env_args.agent_conf="2x1"
env_args.agent_obsk=1
```

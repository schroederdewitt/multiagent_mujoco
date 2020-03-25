```diff
-  Please contact Christian Schroeder de Witt at cs@robots.ox.ac.uk for any questions and file issues if necessary
```

# Multi-Agent Mujoco
Benchmark for Continuous Multi-Agent Robotic Control, based on OpenAI's Mujoco Gym environments.

Used e.g. in the paper [Deep Multi-Agent Reinforcement Learning for Decentralized Continuous Cooperative Control](https://arxiv.org/abs/2003.06709) by Christian Schroeder de Witt, Bei Peng, Pierre-Alexandre Kamienny, Philip Torr, Wendelin Böhmer and Shimon Whiteson, Torr Vision Group and Whiteson Research Lab, University of Oxford, 2020

# Installation

**Note: You require OpenAI Gym Version 10.8.0**
Simply clone this repository and put ./src on your PYTHONPATH.

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
env_args.agent_conf="2x8"
env_args.agent_obsk=1
```

### 2-Agent HumanoidStandup

```python
env_args.scenario="HumanoidStandup-v2"
env_args.agent_conf="2x8"
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

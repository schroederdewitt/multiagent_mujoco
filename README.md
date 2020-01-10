# Multi-Agent Mujoco
Benchmark for Continuous Multi-Agent Robotic Control, based on OpenAI's Mujoco Gym environments.

# Installation

**Note: You require OpenAI Gym Version 10.8.0**
Simply clone this repository and put ./src on your PYTHONPATH.

## Ant-v2

### Ant-v2 2x4
<img src="./docs/images/ant_2x4.png" width="200" height="200">

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="4x2"
env_args.agent_obsk=1
```

### Ant-v2 2x4 diag
<img src="./docs/images/ant_2x4_diag.png" width="200" height="200">

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="4x2d"
env_args.agent_obsk=1
```

### Ant-v2 4x2
<img src="./docs/images/ant_4x2.png" width="200" height="200">

```python
env_args.scenario="Ant-v2"
env_args.agent_conf="2x4"
env_args.agent_obsk=1
```

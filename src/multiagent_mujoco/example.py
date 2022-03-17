from src.multiagent_mujoco.mujoco_multi import MujocoMulti
import numpy as np
import time


def main():
    env_args = {"scenario": "Ant-v2",
                "agent_conf": "2x4",
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
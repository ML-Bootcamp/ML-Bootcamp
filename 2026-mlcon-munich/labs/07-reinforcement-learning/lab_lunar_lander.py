"""Lab 06 - Reinforcement Learning

A minimal but complete reinforcement learning *pipeline* using Gymnasium's
LunarLander environment and Stable-Baselines3 (PPO). Unlike a random agent,
this one actually learns a policy: we first watch the *untrained* agent flail
around, then train it, then watch the *trained* agent land.

The RL loop in a nutshell:
    observe state -> choose action via policy -> get reward -> update policy

PPO (Proximal Policy Optimization) handles the "update policy" part for us.

Run:
    pip install -r requirements.txt
    python lab_lunar_lander.py

Tasks:
- Run the script and compare the untrained vs trained lander.
- Increase TRAIN_STEPS and see how the average reward improves.
- Compare against a random policy (sample actions instead of model.predict).
"""

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

# More steps = better policy but longer training. ~200k lands reliably.
TRAIN_STEPS = 25_000


def watch(model, steps=600):
    """Render the agent acting with its current policy."""
    env = gym.make("LunarLander-v3", render_mode="human")
    observation, info = env.reset(seed=42)
    for _ in range(steps):
        action, _ = model.predict(observation, deterministic=True)
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
    env.close()


# 1. Create the training environment (no rendering, so training is fast).
train_env = gym.make("LunarLander-v3")

# 2. Build the agent. The "policy" is a small neural network mapping the
#    observation (lander position, velocity, angle, ...) to an action.
model = PPO("MlpPolicy", train_env, verbose=1)

# 3. Watch the UNTRAINED agent first: its policy is random, so it crashes.
print("Watching the untrained agent (close the window to continue)...")
watch(model)

# 4. Train: the agent repeatedly acts, collects rewards, and updates its policy.
model.learn(total_timesteps=TRAIN_STEPS)
train_env.close()

# 5. Evaluate the learned policy over several episodes.
eval_env = gym.make("LunarLander-v3")
mean_reward, std_reward = evaluate_policy(model, eval_env, n_eval_episodes=10)
eval_env.close()
print(f"Mean reward over 10 episodes: {mean_reward:.1f} +/- {std_reward:.1f}")

# 6. Watch the TRAINED agent: actions now come from the learned policy.
print("Watching the trained agent...")
watch(model)

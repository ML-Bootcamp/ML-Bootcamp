# Run

    $ pip install -r requirements.txt
    $ python lab_lunar_lander.py

# Lab
The aim of this lab is to see a complete **reinforcement learning pipeline**: an
agent learns a policy by interacting with an environment and being rewarded for
good behaviour. We use Gymnasium's `LunarLander-v3` environment (land a
spacecraft gently between two flags) and the PPO algorithm from
Stable-Baselines3.

The pipeline:
1. Create the environment.
2. Build an agent (PPO with a small neural-network policy).
3. Watch the **untrained** agent (its policy is random, so it crashes).
4. **Train** the policy by interacting with the environment.
5. **Evaluate** the learned policy and print the average reward.
6. Watch the **trained** agent land.

Watching the untrained agent first makes the improvement obvious: the same
`model.predict` call goes from crashing to landing once the policy is trained.

Tasks:
- Run the script and compare the untrained vs trained lander.
- Increase `TRAIN_STEPS` and see how the average reward improves.
- Compare against a random policy (sample actions instead of `model.predict`).

> **Note:** Training takes a few minutes on CPU. The final render window
> requires a local display, so it will not work in a headless environment.

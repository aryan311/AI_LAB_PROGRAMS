# -*- coding: utf-8 -*-
"""AI_Week2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ykjyer8EXFxWXJ6B1sSfh8SYNhq0uNEo
"""

!pip install tf-agents[reverb]

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import tensorflow as tf
import numpy as np

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

import gym

def run_for_steps(steps=500):
    env = gym.make("CartPole-v0")
    total_reward = 0
    for step in range(steps):
      observation = env.reset()
      action = env.action_space.sample() # take a random action
      observation, reward, done, info = env.step(action)
      total_reward += reward
      if done:
          break
    return total_reward

def run_for_episodes(episodes=500):
    env = gym.make("CartPole-v0")
    total_reward = 0
    for episode in range(episodes):
        observation = env.reset()
        episode_reward = 0
        while True:
            action = env.action_space.sample() # take a random action
            observation, reward, done, info = env.step(action)
            episode_reward += reward
            if done:
                break
        total_reward += episode_reward
    return total_reward / episodes

steps_reward = run_for_steps()
episodes_reward = run_for_episodes()
print(f"Reward for running for steps: {steps_reward}")
print(f"Reward for running for episodes: {episodes_reward}")

"""Given that the environment is reset after each episode but continues for a given amount of steps, the prizes obtained for each strategy will probably change. In addition, the computation of the reward for the number of steps is cumulative, whereas the calculation for the number of episodes is averaged. Hence the reward for running episodes lie within close proximity even after changing the no. of episodes."""


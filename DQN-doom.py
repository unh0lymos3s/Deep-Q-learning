import tensorflow as tf
import numpy as np
from vizdoom import *
from skimage import transform
from collections import deque
import matplotlib.pyplot as plt
import warnings
import random
import time
warnings.filterwarnings("ignore")

episodes = None

def create_environment ():
    game = vizdoom.DoomGame()

    game.load_config("basic.cfg")
    game.set_doom_scenario_path("basic.wad")
    game.init()

    left = [1,0,0]
    right = [0,1,0]
    shoot = [0,0,1]     
    possible_actions = [left, right, shoot]

    return game, possible_actions

def test_environment():
    global episodes, actions
    game = vizdoom.DoomGame()
    game.load_config("../../scenarios/basic.cfg")
    game.set_doom_scenario_path("../../scenarios/basic.wad")
    game.init()
    left = [1,0,0]
    right = [0,1,0]
    shoot = [0,0,1]
    actions = [left,right,shoot]    
    episodes = 10

    for i in range(episodes):
        game.new_episode()
        while not game.is_episode_finished():
            state = game.set_state()
            img = state.screen_buffer
            misc= state.game_variables
            action = random.choice()
            print(action)
            reward = game.make_action(action)
            print('reward: ', reward)
        time.sleep(0.02)
    print('Result : ',game.get_total_reward())
    time.sleep(2)
    game.close()

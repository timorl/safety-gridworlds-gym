import gym
from gym import spaces
import numpy as np

AGENT = 0

STAY  = 0
UP    = 1
DOWN  = 2
LEFT  = 3
RIGHT = 4

MOVE = {STAY:  [0,0],
        UP:    [0,1],
        DOWN:  [0, -1],
        LEFT:  [-1, 0],
        RIGHT: [1, 0]}

def position_change(action):
    return MOVE[action]

class BaseGridworld(gym.Env):

    def __init__(self, grid_shape, field_types,
                 initial_state, initial_position,
                 transition,
                 real_reward, corrupt_reward,
                 episode_length,
                 print_field=lambda x: str(x)):
        self.action_space = spaces.Discrete(5)
        assert(field_types >= 1)
        self.observation_space = spaces.MultiDiscrete(np.zeros(grid_shape) + field_types + 1) # All field types plus the agent's position

        def within_world(position):
            return position[0] >= 0 and position[1] >= 0 and position[0] < grid_shape[0] and position[1] < grid_shape[1]

        def to_observation(state, position):
            assert(within_world(position))
            observation = np.array(state, dtype=np.int32)
            observation[position] = AGENT
            return observation

        assert(self.observation_space.contains(to_observation(initial_state, initial_position)))
        position = tuple(initial_position)
        state = np.array(initial_state)
        step = 0
        last_action = None

        def _reset():
            nonlocal position, state, step, last_action
            position = tuple(initial_position)
            state = np.array(initial_state)
            step = 0
            last_action = None
            return to_observation(state, position)

        def _transition(state, position, action):
            pos = np.array(position)
            if within_world(pos + position_change(action)):
                pos = pos + position_change(action)
            return np.array(state), tuple(pos)

        if transition == None:
            transition = _transition # Only move within world, don't change anything

        def _step(action):
            nonlocal position, state, step, last_action
            step += 1
            last_action = action
            state, position = transition(state, position, action)

            info = {'real_reward': real_reward(state, position)}
            reward = corrupt_reward(state, position)
            done = (step > episode_length)
            return (to_observation(state, position), reward, done, info)

        def _render():
            observation = to_observation(state, position)
            for r in reversed(range(grid_shape[1])):
                line = ""
                for c in range(grid_shape[0]):
                    line += print_field(observation[c, r])
                print(line)
            print("A: " + str(last_action) + " S: " + str(step))

        self.step = _step
        self._step = _step
        self.reset = _reset
        self._reset = _reset
        self.render = _render
        self._seed = lambda x: x

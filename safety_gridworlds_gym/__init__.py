from gym.envs.registration import register

import safety_gridworlds_gym.envs.toy_grids as _toy_grids

register(
        id='ToyGridworldUncorrupted-v0',
        entry_point='safety_gridworlds_gym.envs.common.base_gridworld:BaseGridworld',
        kwargs={"grid_shape":_toy_grids.GRID_SHAPE,
                "field_types":1,
                "initial_state":_toy_grids.INITIAL_STATE,
                "initial_position":_toy_grids.INITIAL_POSITION,
                "transition":None,
                "hidden_reward":_toy_grids.hidden_reward,
                "corrupt_reward":_toy_grids.hidden_reward,
                "episode_length":_toy_grids.EPISODE_LENGTH,
                "print_field":_toy_grids.print_field,
        },
)

register(
        id='ToyGridworldCorners-v0',
        entry_point='safety_gridworlds_gym.envs.common.base_gridworld:BaseGridworld',
        kwargs={"grid_shape":_toy_grids.GRID_SHAPE,
                "field_types":1,
                "initial_state":_toy_grids.INITIAL_STATE,
                "initial_position":_toy_grids.INITIAL_POSITION,
                "transition":None,
                "hidden_reward":_toy_grids.hidden_reward,
                "corrupt_reward":_toy_grids.corrupt_corners,
                "episode_length":_toy_grids.EPISODE_LENGTH,
                "print_field":_toy_grids.print_field,
        },
)

register(
        id='ToyGridworldOnTheWay-v0',
        entry_point='safety_gridworlds_gym.envs.common.base_gridworld:BaseGridworld',
        kwargs={"grid_shape":_toy_grids.GRID_SHAPE,
                "field_types":1,
                "initial_state":_toy_grids.INITIAL_STATE,
                "initial_position":_toy_grids.INITIAL_POSITION,
                "transition":None,
                "hidden_reward":_toy_grids.hidden_reward,
                "corrupt_reward":_toy_grids.corrupt_on_the_way,
                "episode_length":_toy_grids.EPISODE_LENGTH,
                "print_field":_toy_grids.print_field,
        },
)

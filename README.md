# Markov Decision Process - Value Iteration

A Python implementation of the Value Iteration algorithm for solving Markov Decision Processes (MDPs) in grid-world environments.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Environment File Format](#environment-file-format)
- [Algorithm Details](#algorithm-details)
- [Examples](#examples)
- [Output Format](#output-format)
- [Contributing](#contributing)
- [Author](#author)

## Overview

This project implements the Value Iteration algorithm, a dynamic programming approach for finding optimal policies in Markov Decision Processes. The implementation works with grid-world environments where an agent must navigate through a grid to reach terminal states while avoiding obstacles and maximizing cumulative rewards.

### What is Value Iteration?

Value Iteration is a method for computing the optimal value function and policy for an MDP. It works by iteratively updating the value (utility) of each state based on the expected rewards and the values of successor states, eventually converging to the optimal values.

## Features

- ✅ Stochastic movement model (80% intended direction, 10% perpendicular directions)
- ✅ Support for obstacles/walls in the environment
- ✅ Configurable rewards for terminal and non-terminal states
- ✅ Customizable discount factor (gamma)
- ✅ Visual policy output with directional arrows
- ✅ Utility values for each state

## Requirements

- Python 3.6+
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/markov-decision.git
cd markov-decision
```

2. Install required dependencies:
```bash
pip install numpy
```

## Usage

Run the value iteration algorithm with the following command:

```bash
python value_iteration.py <environment_file> <non_terminal_reward> <gamma> <K>
```

### Parameters:

- **`environment_file`**: Path to the CSV file containing the grid environment
- **`non_terminal_reward`**: Reward received for each step in non-terminal states (typically negative, e.g., -0.04)
- **`gamma`**: Discount factor (0 < γ ≤ 1). Controls the importance of future rewards
- **`K`**: Number of iterations to run the algorithm

### Example Command:

```bash
python value_iteration.py environment.csv -0.04 0.9 20
```

## Environment File Format

The environment should be provided as a CSV file with the following format:

- **`.`** - Empty non-terminal state
- **`X`** - Wall/Obstacle (impassable)
- **Numeric values** - Terminal states with their reward values (e.g., `1`, `-1`)

### Example Environment File (environment.csv):

```csv
.,.,.,1
.,X,.,-1
.,.,.,.
```

This represents a 3x4 grid where:
- Top-right corner has a positive terminal state (reward = 1)
- Position (1,3) has a negative terminal state (reward = -1)
- Position (1,1) is a wall
- All other positions are navigable non-terminal states

## Algorithm Details

### Movement Model

The agent's movements are stochastic:
- **80% probability**: Move in the intended direction
- **10% probability**: Move perpendicular to the left
- **10% probability**: Move perpendicular to the right

If a movement would result in hitting a wall or going out of bounds, the agent stays in its current position.

### Value Iteration Update Equation

For each state s and iteration k:

```
V(k+1)(s) = R(s) + γ * max_a Σ_s' P(s'|s,a) * V(k)(s')
```

Where:
- `V(k)(s)` is the value of state s at iteration k
- `R(s)` is the immediate reward for state s
- `γ` is the discount factor
- `P(s'|s,a)` is the transition probability from state s to s' given action a

### Actions

The agent can choose from four actions:
- **Up** (^)
- **Down** (v)
- **Left** (<)
- **Right** (>)

## Examples

### Example 1: Simple Grid World

Create a file `simple_grid.csv`:
```csv
.,.,1
.,X,-1
.,.,.
```

Run:
```bash
python value_iteration.py simple_grid.csv -0.04 0.9 100
```

### Example 2: Larger Grid with Multiple Obstacles

Create a file `complex_grid.csv`:
```csv
.,.,.,.,.
.,X,X,X,.
.,.,.,.,10
.,X,X,X,.
-10,.,.,.,.
```

Run:
```bash
python value_iteration.py complex_grid.csv -0.1 0.95 50
```

## Output Format

The program outputs two matrices:

### 1. Utilities Matrix
Shows the computed utility (value) for each state:
```
utilities:
 0.812  0.868  0.918  1.000
 0.762  0.000  0.660 -1.000
 0.705  0.655  0.611  0.388
```

### 2. Policy Matrix
Shows the optimal action for each state:
```
policy:
>      >      >      o    
^      x      ^      o    
^      <      <      <    
```

Where:
- `^`, `v`, `<`, `>` : Optimal movement direction
- `o` : Terminal state
- `x` : Wall/Obstacle

## Implementation Details

### Key Functions

- **`value_iteration()`**: Main algorithm implementation
- **`moveState()`**: Calculates transition probabilities for actions
- **`findMax()`**: Finds the maximum expected utility across all actions
- **`R()`**: Returns the reward for a given state
- **`isValid()`**: Checks if a state is valid (not a wall or out of bounds)

### Performance Considerations

- Time Complexity: O(K × |S|² × |A|) where K is iterations, |S| is number of states, |A| is number of actions
- Space Complexity: O(|S|) for storing utilities and policies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

**Nicholas Moreland**

## License

This project is available for educational purposes. Please contact the author for any other use cases.

## Acknowledgments

- Based on the Value Iteration algorithm from Russell & Norvig's "Artificial Intelligence: A Modern Approach"
- Inspired by UC Berkeley's CS188 course materials
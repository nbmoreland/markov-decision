# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Markov Decision Process (MDP) implementation using the value iteration algorithm. The project implements a grid-world environment where an agent learns optimal policies through reinforcement learning.

## Commands

### Running the Value Iteration Algorithm
```bash
python value_iteration.py <environment_file> <non_terminal_reward> <gamma> <K>
```

Parameters:
- `environment_file`: Path to CSV file containing the grid environment
- `non_terminal_reward`: Reward for non-terminal states (typically negative)
- `gamma`: Discount factor (0 < gamma ≤ 1)
- `K`: Number of iterations

## Architecture

### Core Algorithm Implementation

The value iteration implementation (`value_iteration.py`) consists of:

1. **State Transition Model**: 
   - Stochastic movement with 80% probability of intended direction
   - 10% probability each for perpendicular directions
   - Handles invalid moves by keeping agent in same position

2. **Key Functions**:
   - `value_iteration()`: Main algorithm that iterates K times to compute optimal utilities and policy
   - `moveState()`: Calculates transition probabilities for each action
   - `findMax()`: Computes expected utility for a given action
   - `R()`: Returns reward for a given state
   - `isValid()`: Checks if a state is valid (not a wall)

3. **Environment Format**:
   - CSV file with grid representation
   - "X" represents walls/obstacles
   - "." represents empty non-terminal states
   - Numeric values represent terminal states with their rewards

4. **Output**:
   - Utilities matrix: Computed value for each state
   - Policy matrix: Optimal action for each state (^, v, <, >, x for walls, o for terminal states)

## Development Notes

- The implementation uses NumPy for efficient matrix operations
- The policy uses Unicode characters for directional arrows
- Terminal states are marked with "o" in the policy output
- Walls/invalid states are marked with "x" in the policy output
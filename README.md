# Symbolic Regression Project

## Overview
This project focuses on solving the Symbolic Regression problem using an evolutionary algorithm. Symbolic Regression aims to discover mathematical expressions that best fit a given dataset, providing insights into the relationships between input variables and output values.

## Problem Description
Symbolic Regression is a machine learning task where the goal is to find a symbolic expression that models the relationship between input variables and output values. Given a dataset of input-output pairs, the objective is to discover a formula that accurately predicts outputs from inputs.

In this project, we worked with 8 datasets, each with varying numbers of input variables and output values. The challenge was to identify the formula that best represents the underlying data for each dataset.

## Implementation Details
The problem was tackled using a custom evolutionary algorithm.

### Data Representation
- **Individual Structure**: Used to represent an individual
    - Genome (Node)
    - Fitness: float # fitness value
    - Age: int
- **Node Structure**: Each node contains:
  - Value (operator, variable, or constant)
  - Type (operator or variable)
  - Left and right children (for binary operations)

### Operators and Variables
- **Operators**: Addition, subtraction, multiplication, division, sine, cosine, log, abs.
- **Variables**: Represented as `x1`, `x2`, ..., `xn`, where `n` is the number of input variables.
- **Constants**: Randomly generated from [-100 to 100].

### Algorithm Workflow
1. **Initialization**:
   The main idea is to have different islands with different populations. Each island will have its dominant operator, there will be an island with only one operator. There     will be some islands where we can have all possible combinations of operators. Each island will evolve independently.

2. **Fitness Evaluation**:
   - The fitness of an individual is calculated as the mean squared error (MSE) between predicted and actual values in the dataset.

3. **Parent Selection**:
   - Tournament selection is used, where 12 random individuals are selected.
   - Two parents are selected from this group to generate offspring.

4. **Crossover**:
   - A random subtree of one parent is exchanged with a random subtree of the other parent to create two children.

5. **Mutation**:
   - There are 8 mutation strategy:
      - Pick a random constant from the given tree, then change its value.
      - Pick 1 random operator from the given tree, then replace it with another operator that is not equal to the previous one.
      - Pick a subtree from the given tree, then replace it with a constant.
      - Select a subtree from the given tree, then replace it with another random tree.
      - Simplify the expression
      - Replace the expression with a newly generated random expression.
      - Select a random variable x[0]...x[n] from the given tree, then replace it with another variable not equal to the previous one.


6. **Offspring Handling**:
   - The oldest individuals are replaced by the new offspring

7. **Population Update**:
   - Perform migration of individuals between islands with a small random probability to happend
   - Substitute one individual with the best individual overall
   - Substitute one individual with the best individual from a random island

8. **Iteration**:
   - Repeat the process for a fixed number of generations (40).

9. **Final Solution**:
   - Retain the best individual as the symbolic expression that best fits the dataset.


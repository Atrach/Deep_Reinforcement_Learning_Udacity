# Udacity Deep Reinforcement Learning Nanodegree - Project 3: Collaboration and Competition

## Project Objetive

The objective of this project is to train a pair of Reinforcement learning agents to play a simplified version of a tennis game. As in regular tennis, players or in this case the virtual agents need to keep the ball in play to increase their own rewards. Agents learn that if the ball falls or if it goes outside of the court they lose points. This environment fell into the category of a competitive environment where each agent is focused on its own rewards and to learn its own independent policy. 

## Implementation [MADDPG](https://papers.nips.cc/paper/7217-multi-agent-actor-critic-for-mixed-cooperative-competitive-environments.pdf)

In the presented environment, the action space of each agent fell within the continuous-time domain; therefore, as in the previous continuous control project, an actor-critic algorithm can be used to compute the actions. A Deep Deterministic Policy Gradient (DDPG) is implemented for this task. Furthermore, the algorithm can be extended to be used to train multiple agents as shown by [Lowe et al.](https://papers.nips.cc/paper/7217-multi-agent-actor-critic-for-mixed-cooperative-competitive-environments.pdf). This presented algorithm or Multi-Agent Deep Deterministic Policy Gradient (MADDPG) can be used so each agent can learn its own policy and take its own actions in order to maximize theirs owns rewards. However, both agents learn from a buffer with shared experiences that contain states, actions, and rewards. 

## Results

The actor-critic network architecture and hyperparameters can be found in the tables below. It can be appreciated that batch normalization was implemented in both networks in order to improve stability and prevent exploding gradients. In each episode each agent can learn up to four times, this can be seen in the 'LEARN_PASSES' hyperparameter. Finally, an adaptive parameter called epsilon is implemented to decay the noise provided by the Ornstein-Uhlenbeck process in the action space with the purpose of getting a better exploration-exploitation approach. Early episodes get a higher amount of noise which improves exploration, but as the agents learn, this noise decreases which leads to better exploitation of the rewards. 

### Network Architecture


|        THE ACTOR       |            THE CRITIC           |
|:----------------------:|:-------------------------------:|
| States --> FC1 --> 128 |     States --> FCS1 --> 128     |
|     ReLU Activation    |      Leaky ReLU Activation      |
|   Batch Normalization  |       Batch Normalization       |
|   128 --> FC2 --> 128  | 128 + 2 actions --> FC2 --> 128 |
|     ReLU Activation    |     Leaky ReLU Activation       |
|   Batch Normalization  |        128 --> FC3 --> 1        |
|128 --> FC3 --> action size|                              |
|     tanh Activation    |                                 |


### Hyperparameters


| BUFFER_SIZE  | int(1e6) | replay buffer size                   |
|--------------|----------|--------------------------------------|
| BATCH_SIZE   | 128      | minibatch size                       |
| GAMMA        | 0.99     | discount factor                      |
| TAU          | 1e-3     | for soft update of target parameters |
| LR_ACTOR     | 1e-3     | learning rate of the actor           |
| LR_CRITIC    | 1e-3     | learning rate of the critic          |
| WEIGHT_DECAY | 0        | L2 weight decay                      |
| LEARN_PASSES | 4       | number of learning passses           |
| LEARN_EVERY  | 1       | learn every N time steps             |
| EPSILON_START | 2        |          start value of epsilon for noise decay            |
| EPSILON_DECAY | 0.998       |     decreasing factor for epsilon after each episode       |
| EPSILON_FINAL  | 0.2       |       final value for the epsilon noise decay       |


The plot below shows the agents' performance over 1000 episodes. The environment was solved after 678 episodes and the agents maintain increasing its maximum score even after 300 episodes later.

![Solution 1](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project3/MADDPG/maddpg_scores.png)

## Conclusions and Future work

It can be noticed that as the agents learn to play better the game, the learning process time between episodes tends to increase significantly meaning that the agents hold the ball more time in play and thus episodes with higher rewards tend to last more than at the initial phase of the learning process.
In order to reduce the waiting time during the learning process, one strategy may be to adaptively control the number learning passes 'LEARN_PASS' as the agents get better in the game. Finally, adding prioritized experience replay can come very handy and reduce the learning time in this type of environment because of the volume of repetitive actions that do not impact that much in the learning process.

# Udacity Deep Reinforcement Learning Nanodegree - Project 3: Collaboration and Competition

## Implementation  


## Results


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

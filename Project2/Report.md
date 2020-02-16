# Udacity Deep Reinforcement Learning Nanodegree - Project 2: Continuous Control  

## Implementation  

In this project the goal is to control multiple double-jointed arms which actions belong to the continuous time domain.  However, this task can be complex because actions can adopt any value from an infinite set and deep reinforcement algorithms such as DQN are not practical for this problem since actions would have to be discretized leading which is not practical and inefficient; therefore, another approach is needed for continuous control problems. 

Actor-critic algorithms are designed to tackle continuous time control problems, they use a combination between policy-based and value-based methods. The policy-based method “The actor” directly maps the input states to the desire continuous time action commands, and the value-based method “The critic” calculates the value of that action.  The combination of these two methods leads to a high learning performance with low bias and variance. In this project, Deep Deterministic Policy Gradient DDPG was the actor-critic algorithm used to solve the environment. 

## Results

### Network


|        THE ACTOR       |            THE CRITIC           |
|:----------------------:|:-------------------------------:|
| States --> FC1 --> 128 |     States --> FCS1 --> 256     |
|     ReLU Activation    |      Leaky ReLU Activation      |
|   Batch Normalization  | 256 + 4 actions --> FC2 --> 128 |
|   128 --> FC2 --> 128  |      Leaky ReLU Activation      |
|     ReLU Activation    |       128 --> FC3 --> 128       |
|   Batch Normalization  |      Leaky ReLU Activation      |
|    128 --> FC3 --> 4   |        128 --> FC3 --> 1        |
|     tanh Activation    |


### Hyperparameters


| BUFFER_SIZE  | int(1e6) | replay buffer size                   |
|--------------|----------|--------------------------------------|
| BATCH_SIZE   | 128      | minibatch size                       |
| GAMMA        | 0.99     | discount factor                      |
| TAU          | 1e-3     | for soft update of target parameters |
| LR_ACTOR     | 1e-4     | learning rate of the actor           |
| LR_CRITIC    | 3e-4     | learning rate of the critic          |
| WEIGHT_DECAY | 0        | L2 weight decay                      |
| LEARN_PASSES | 10       | number of learning passses           |
| LEARN_EVERY  | 20       | learn every N time steps             |


The plot below shows the agent performance over 400 episodes. The environment was solved after 269 episodes. 

![Solution 1](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project2/DDPG/ddpg_score.png)

## Future work

In the presented algorithm actions were mixed with noise in a process called Ornstein-Uhlenbeck in order to improve exploration. However, it is been proved that adding noise to the parameters space instead of the action space can greatly contribute to better exploration and thus obtaining higher scores faster. Furthermore, exploring other algorithms such as the Distributed Distributional Deterministic Policy Gradients (D4PG), or Trust Region Policy Optimization (TRPO) may perform better for the presented environment.

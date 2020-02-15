# Udacity Deep Reinforcement Learning Nanodegree - Project 2: Continuous Control  

## Implementation  


## Results

The plot below shows the agent performance over 400 episodes. The environment was solved after 269 episodes. 

![Solution 1](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project2/DDPG/ddpg_score.png)

## Future work

In the presented algorithm actions were mixed with noise in a process called Ornstein-Uhlenbeck in order to improve exploration. However, it is been proved that adding noise to the parameters space instead of the action space can greatly contribute to better exploration and thus obtaining higher scores faster. Furthermore, exploring other algorithms such as the Distributed Distributional Deterministic Policy Gradients (D4PG), or Trust Region Policy Optimization (TRPO) may perform better for the presented environment.

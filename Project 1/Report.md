# Udacity Deep Reinforcement Learning Nanodegree - Project 1: Navigation  
  
## Implementation  
In this project, different variations of Deep Q-networks algorithms are used to compare the performance among them when solving the environment "Bananas".

Once the environment is set up (take a look at README.md), and the agent is created (three Deep RL algorithms were implemented in this project, DQN, Double DQN, and Dueling DDQN), the agent can start to act and learn from its interactions with the environment. Experiences from these interactions are collected and stored in a buffer from which they are later extracted uniformly randomized as tuples containing the current state, action, reward, and next state, and then fed into the algorithm for learning (this process is called *experience replay* and it decreases data correlation). Furthermore, a neural network structure that is part of the agent, works to create a function approximation mapping states to actions values. Later the agent selects an action based on a ε-greedy policy that manages the exploration vs. exploitation dilemma and the whole process is repeated for a predefined number of episodes or until the environment is considered to be solved.

Note: the code representing the agents, and the trained network weights can be found in the folders with their respective names (DQN, DDQN, and Duel_DDQN).  

## Learning algorithm and Neural Network Architectures  
  
### Deep Q-Networks  [(DQN)](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf)


Deep Q-Networks are used as function approximation in order to map any state given from an environment to agent action values Q(s,a;θ) where θ are the parameters of the network. Furthermore, In order to improve the performance and stability of the algorithm, DQN contains an online and a target network. The parameters of the target network are copied from the online parameter parameters every τ time steps and then kept fixed.

The target DQN can be calculated as:

![DQN target](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/formula/DQN.jpg)


### Double Deep Q-Networks  [(DDQN)](https://arxiv.org/pdf/1509.06461.pdf)

The DDQN is a variation of the regular DQN that intends to solve the issue of getting overestimated values because of the max operator that is used in DQN to both evaluate and select an action. Furthermore, the online network is used to evaluate the greedy policy as in DQN, but the target network is used to estimate its value.

 The target of the double DQN can be calculated as:
 
![DDQN target](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/formula/DDQN.jpg)


### Dueling Deep Q-Networks [(Dueling DQN)](https://arxiv.org/abs/1511.06581)
Dueling Deep Q-Networks are used because sometimes the values of the states do not considerably change among the actions; thus, it is better to calculate them separately, and the benefit that individual actions have in each state. Furthermore, they get their name because the main network with parameters θ  bifurcates into two branches, one is for calculating the advantage function A(s) with parameters α, and the second branch is to calculate the state value function V(s) with parameters named β. Using the equation shown below, these two functions can be joined to form the Q values. 

![Dueling Q value](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/formula/Duel_Q_value.jpg)

Finally, using this architecture is beneficial to provide a better policy evaluation when similar value actions appear.   

![Dueling DQN network](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/formula/Duel_DQN.png)

  Dueling architecture diagram.

## Results  

The performance of three agents was compared, a regular DQN, a Double DQN, and a Dueling Double DQN. Furthermore, different hyperparameters were tested to maximize the final reward and to minimize the converging time. 
Below, it can be found different solutions where the hyperparameter tunned were the sizes of the hidden layers of the neural network and the parameters for the ϵ-greedy policy.  Finally, it was found that with the presented hyperparameters, the best performance was obtained from the Dueling DDQN on solution 2. 

__Solution 1__   

Network: fc1 = 128 , fc2 = 64  
epsilon decay = 0.990
final epsilon = 0.01 


| Algorithm | Episodes to solve environment (score = 13)| Episodes max average score/Max average score |  
|--------------|-------------------|-------------------|  
| DQN | 306 | 500/16.16 |  
| DDQN | 395 | 1000/16.32 |  
| Dueling DDQN | 409 | 1000/16.62 |  


![Solution 1](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/solution1.png)

__Solution 2__ 

Network: fc1 = 64, fc2 = 64  
epsilon decay = 0.990  
final epsilon = 0.01


| Algorithm | Episodes to solve environment (score = 13)| Episodes max average score/Max average score |  
|--------------|-------------------|-------------------|  
| DQN | 367 | 800/16.07 |  
| DDQN | 338 | 1200/16.22 |  
| Dueling | 277 | 900/16.68 |


![Solution 2](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/solution2.png)

__Solution 3__

Network: fc1 = 64 , fc2 = 64  
epsilon decay = 0.997  
final epsilon = 0.02


| Algorithm | Episodes to solve environment (score = 13)| Episodes max average score/Max average score |  
|--------------|-------------------|-------------------|  
| DQN | 692 | 800/15.03 |  
| DDQN | 758 | 1200/15.45 |  
| Dueling DDQN | 751 | 1000/15.94 |


![Solution 3](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Solutions/solution3.png)

## Future work ##  
  
In the presented work all the states fed to the agent were given by uniform randomized experience replay. Although this method helps to remove correlation that occurs when consecutive data from the enviroment is given to the agent in the learning process, it is more likely that states that have a higher probability of increasing the learning process have equal or less chance than regular states to be feed into the algorithm. Therefore, this process can be improved by implementing *__"Prioritized Experience Replay"__* to calculate which expericences have higher probabilities of improving the learning process; thus, resulting in faster learning and the obtetion of a better final policy.



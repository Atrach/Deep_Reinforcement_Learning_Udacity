# DeepRL-Navigation-Udacity-Project-1
## Project Name: Navigation

### __The Enviroment__: "_Bananas_"

"Bananas" is a square world environment where an agent has to maximize the number of yellow bananas collected while navigating through it. The state-space consists of 37 dimensions representing the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Furthermore, the agent counts with four discrete actions to interact with the environment (listed below). The main idea is that the agent has to learn what are the best actions to take when information from the state space of the environment is given in order to maximize the total rewards during an episode.

The rewards are designed so every yellow banana collected returns a reward of +1 and every blue banana a reward of -1. The objective is to come up with an agent that can accomplish an average score of +13 over 100 consecutive episodes.

Set of actions:
`0` - move forward,  `1` - move backward,  `2` - turn left,  `3` - turn right.
    
  _Trained Dueling DDQN agent in action._
  
![Dueling DDQN Agent](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project%201/Agent_Duel_DDQN.gif)

### __Set up Requirements__
  
1) Download or clone the [Udacity repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) and follow the instructions on the `README.md` in order to install all the dependencies needed to set up the Python environment.

2) The environment can be found in the links below depending on your operating system:

    -  Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    -  Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    -  Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    -  Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

3) Place the file containing the environment in the p1_navigation/ folder in the DRLND repository, and unzip (or decompress) the file.

4) Download the files presented in this repository a place them into `p1_navigation/` (Note: this action may replace some files)

5) Follow instructions in `Navigation.ipynb` to train and watch an agent in action.

### __Code & Solution__

- `Navigation.ipynb` contains the code to set up the environment, train a selected agent and watch it in action..!
- `DQN`, `DDQN`, and `Duel_DDQN` folders contain files that define the agents, the neural network architecture used, and the weights obtained after training the agents respectively.


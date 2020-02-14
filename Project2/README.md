# DeepRL-Udacity-Project-2
## Project Name: Continuous Control

### __The Enviroment__: "_Reacher_"

_Trained DDPG multi agent in action._
  
![DDPG_multi_agent](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project2/DDPG/Agent_Multi_DDPG.gif)


This environment contains 20 identical agents each with its own copy of the environment. Each agent controls a double-jointed arm that can move to target locations. Furthermore, the observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of the agent is to maintain its position at the target location for as many time steps as possible. Finally, the threshold for solving the environment is to get an average score of +30 (over 100 consecutive episodes, and over all agents). Meaning that after each episode, all the scores from the agents are added up and then an average is computed.

### __Set up Requirements__
  
1) Download or clone the [Udacity repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) and follow the instructions on the `README.md` in order to install all the dependencies needed to set up the Python environment.

2) The environment can be found in the links below depending on your operating system:

    -  Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
    -  Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
    -  Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
    -  Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

3) Place the file containing the environment in the p2_continuous-control/ folder in the DRLND repository, and unzip (or decompress) the file.

4) Download the files presented in this repository a place them into `p2_continuous-control/` (Note: this action may replace some files)

5) Follow instructions in `Continuous_Control.ipynb` to train and watch an agent in action.

### __Code & Solution__

- `Continuous_Control.ipynb` contains the code to set up the environment.
- The `DDPG` folder contains files that define the agents, the neural network architecture used, and the weights obtained after training the agents respectively.

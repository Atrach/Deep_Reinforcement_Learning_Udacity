# DeepRL-Udacity-Project-3
## Project Name: Collaboration and Competition

### __The Enviroment__: "_Tennis_"

_Trained MADDPG multi agent in action._
  
![MADDPG_multi_agent](https://github.com/Atrach/Deep_Reinforcement_Learning_Udacity/blob/master/Project3/MADDPG/Agent_Multi_DDPG.gif)


In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). 

Specifically, after each episode we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores.
This yields a single score for each episode.
The environment is considered solved, when the average (over 100 episodes) of those scores is at least +0.5.

### __Set up Requirements__
  
1) Download or clone the [Udacity repository](https://github.com/udacity/deep-reinforcement-learning#dependencies) and follow the instructions on the `README.md` in order to install all the dependencies needed to set up the Python environment.

2) The environment can be found in the links below depending on your operating system:

    -  Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
    -  Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
    -  Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
    -  Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

3) Place the file containing the environment in the p3_collab-compet/ folder in the DRLND repository, and unzip (or decompress) the file.

4) Download the files presented in this repository a place them into `p3_collab-compet/` (Note: this action may replace some files)

5) Follow instructions in `Tennis.ipynb` to train and watch an agent in action.

### __Code & Solution__

- `Tennis.ipynb` contains the code to set up the environment.
- The `MADDPG` folder contains files that define the agents, the neural network architecture used, and the weights obtained after training the agents respectively.

# model #

import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (policy) model."""
    
    def __init__(self, state_size, action_size, seed, fc1_units=128, fc2_units=64):
        """
        Parameters:
        state_size (int): Dimension for each state
        action_size (int): Dimension for each action
        seed (int): Random seed
        fc1_units (int): Number of neurons in the first hidden layer
        fc2_units (int): Number of neurons in the second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        # Shared layers
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        
        # Advantage function layers
        self.fc3 = nn.Linear(fc2_units, action_size)
        
        # Value function layers
        self.fc4 = nn.Linear(fc2_units,1)
            
    def forward(self, state):
        """ Propagate from states to action values """
        x = F.relu(self.fc1(state))
        x1 = F.relu(self.fc2(x))
        
        # Advantage function output
        A = self.fc3(x1)
        
        # Value function output
        V = self.fc4(x1)
        
        Q = V + (A - A.mean(dim=1, keepdim=True))
        
        return Q
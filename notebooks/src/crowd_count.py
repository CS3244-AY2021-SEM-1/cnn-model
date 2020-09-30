'''
Contains the CrowdCounter class
- Instantiate a new NN instance with CrowdCounter(architecture)
    - architecture can be one of:
        - mcnn
        - csrnet
- Remember to set the neural network in training/evaluation mode:
    - training:   net.train(True)
    - evaluation: net.train(False)
'''

import torch.nn as nn
from src.network import *
from src.models import *


class CrowdCounter(nn.Module):
    def __init__(self, architecture):
        super(CrowdCounter, self).__init__()

        self.name = architecture

        if architecture == 'csrnet': self.DME = CSRNet()
        elif architecture == 'mcnn': self.DME = MCNN()
        
        self.loss_fn = nn.MSELoss()
        
    @property
    def loss(self):
        return self.loss_mse

    def name(self):
        return self.name
    
    def forward(self, im_data, gt_data=None):        
        im_data = np_to_variable(im_data, is_cuda=False, is_training=self.training)
        density_map = self.DME(im_data)
        
        if self.training:                        
            gt_data = np_to_variable(gt_data, is_cuda=False, is_training=self.training)
            self.loss_mse = self.build_loss(density_map, gt_data)
            
        return density_map
    
    def build_loss(self, density_map, gt_data):
        loss = self.loss_fn(density_map, gt_data)
        return loss
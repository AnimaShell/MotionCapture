import torch
import torchvision
import numpy as np
import torch.nn as nn
import torch.optim as optim


learningRate = 0.001
epoch = 10
batchsize = 20


#  input:256 * 256 *1
# output:2*6 + 5*3 + 6*3 + 8*3
class SimpleMikuu(nn.Module):
    def __int__(self):
        super(SimpleMikuu, self).__int__()
        self.PR = nn.Sequential(

        )

    def forward(self, x):
        pass


optimizer = optim.Adam()


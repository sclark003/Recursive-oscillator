import numpy as np
from math import*

class Oscillator:
    #oscillate at frequency f
    #buffer length l
    def __init__(self, f,l):
        self.l = l
        self.f = f
        self.y_one = 1
        self.y_two = 0
        self.buffer_y = np.zeros(self.l)
    
    def oscillate(self):
        wT = ((2*pi*self.f)/44100)
        for i in range(self.l):
            acc1 = self.y_one * (2*cos(wT))
            acc2 = self.y_two * -1
            self.buffer_y[i] = acc1 + acc2
            self.y_two = self.y_one
            self.y_one = self.buffer_y[i]            
        return self.buffer_y

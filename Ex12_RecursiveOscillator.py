import numpy as np
from math import*
import matplotlib.pyplot as plt

class Oscillator:
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
            
            
a = Oscillator(440,10000)
b = a.oscillate()
c = np.fft.fft(b)
freq = np.linspace(0, 44100, len(c))

plt.figure(1)
plt.plot(b)
plt.figure(2)
plt.plot(freq,c)
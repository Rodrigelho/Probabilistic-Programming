import numpy as np
from pomegranate import *
import matplotlib.pyplot as plt

a = NormalDistribution(5,2)
prob = a.probability(5)
print(prob)
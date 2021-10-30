import numpy as np
from pomegranate import *
import matplotlib.pyplot as plt

#--------------INICIALIZAÇÃO----------------------------

#Uma distribuição é inicializada passando os seus parâmetros
#No caso da distribuição uniforma, a média e o desvio padrão
a = NormalDistribution(5,2)

#Quando não sabemos os parâmetros da distribuição, podemos fazer fit da distribuição a dados
#Para isto usamos a classe from_samples
b = NormalDistribution.from_samples([3,4,5,6,7])

#-------------Probabilidades-------------------------------

#Calcular probabilidades é também muito simples, basta usar o método probability
prob_log = a.log_probability(5)
prob = a.probability(5)

#Podem ser criadas distribuições multivariáveis a partir de distribuições univariáveis
#através do método IndependentComponentsDistribution e passando-lhe um array das outras distribuições
d1 = NormalDistribution(5, 2)
d2 = LogNormalDistribution(1, 0.3)
d3 = ExponentialDistribution(4)
d = IndependentComponentsDistribution([d1, d2, d3])
X = [6.2,0.4,0.9]
d.probability(X)

#--------------FITTING---------------------------------

#Podemos querer ajustar a distribuição a novos dados
#As distribuições são atualizadas usando a máxima verosimilhança
#O kernel decide se descarta os pontos anteriores ou se diminui o seu peso se a inércia for usada

e = NormalDistribution(5,2)
e.fit([1, 5, 7, 3, 2, 4, 3, 5, 7, 8, 2, 4, 6, 7, 2, 4, 5, 1, 3, 2, 1])
e

#Também podemos passar um array com os pesos juntamente com os dados:

e = NormalDistribution(5,2)
e.fit([1, 5, 7, 3, 2, 4], weights=[0.5, 0.75, 1, 1.25, 1.8, 0.33])
e



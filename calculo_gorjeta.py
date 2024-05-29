# Libs
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variaveis de Entrada
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
# Variaveis de Saida
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

# Pega as notas de 0 a 10 da qualidade da comida e define em 3 ranges: Ruim, Media e Boa	
qualidade.automf(number=3, names=['ruim', 'media', 'boa'])
qualidade.view()

# Pega as notas de 0 a 10 do servico e define em 3 ranges: Ruim, Medio e Bom
servico.automf(number=3, names=['ruim', 'medio', 'bom'])
servico.view()

# Definindo ranges de gorjeta [Inico, Pico, Fim]
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])

# Definindo regras 
regra1 = ctrl.Rule(servico['ruim'] | qualidade['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['medio'], gorjeta['media'])
regra3 = ctrl.Rule(servico['bom'] | qualidade['boa'], gorjeta['alta'])

controlador = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(controlador)

# Inputs
simulador.input['qualidade'] = 8.5
simulador.input['servico'] = 6.5
# Computando
simulador.compute()
print(simulador.output['gorjeta'])
#gorjeta.view(sim = simulador)
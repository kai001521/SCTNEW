# Practical 8B: Tipping Problem
# Source: SCT_Practicals_1_to_8.pdf

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

q = ctrl.Antecedent(np.arange(0, 11, 1), "quality")
s = ctrl.Antecedent(np.arange(0, 11, 1), "service")
t = ctrl.Consequent(np.arange(0, 26, 1), "tip")

q.automf(3); s.automf(3) # Creates 'poor', 'average', 'good'
t['low'] = fuzz.trimf(t.universe, [0, 0, 13])
t['high'] = fuzz.trimf(t.universe, [13, 25, 25])

rules = [ctrl.Rule(q['poor'] | s['poor'], t['low']),
         ctrl.Rule(s['good'] | q['good'], t['high'])]

tipping = ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8
tipping.compute()

print("Calculated Tip:", tipping.output['tip'])

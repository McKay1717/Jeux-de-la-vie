from Backend.backend import Backend
from Backend.CellArray import CellArray
from Backend.rule import Rule
from Backend.rulesCollection import RulesCollection

cells = CellArray(50)
rule1 = Rule(False, 0, 0, 0)
rule2 = Rule(False, 0, 0, 1)
rule3 = Rule(False, 0, 1, 0)
rule4 = Rule(False, 0, 1, 1)
rule5 = Rule(False, 1, 0, 0)
rule6 = Rule(False, 1, 0, 1)
rule7 = Rule(False, 1, 1, 0)
rule8 = Rule(False, 1, 1, 1)

rules = {rule1: True, rule2: False, rule3: True, rule4: False, rule5: False, rule6: True, rule7: False, rule8: True}
rules = RulesCollection(rules)

engine = Backend(rules, cells)

for i in range(0, 100):
    line = []
    cells = engine.getCellArray()
    for e in cells:
        if e:
            line.append(' ')
        else:
            line.append(chr(219))
    print(line)
    engine.tick()
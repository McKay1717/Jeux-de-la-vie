from Backend.CellArray import  CellArray
from Backend.rule import  Rule
from Backend.rulesCollection import RulesCollection

class Backend:
    def __init__(self, rules, cell_tabs):
        self.__cell_tabs = None
        self.rules = None
        try:
            self.__cell_tabs = cell_tabs
            self.__rules = rules
        except Exception as e:
            raise e

    def getCellArray(self):
        return self.__cell_tabs

    def getRules(self):
        return self.__rules

    def setRules(self, rules_dict):
        if not isinstance(rules_dict, RulesCollection):
            raise TypeError('Expeting a RuleCollection')
        self.__rules = rules_dict

    def setCellArray(self, cell_array):
        if not isinstance(cell_array, CellArray):
            raise TypeError('Expeting a CellArray')
        self.__cell_tabs = cell_array

    def __generateLineFromRules(self, lastLine):
        newLine =[]
        for i in range(0, len(lastLine)):
            if i != 0:
                a = lastLine[i-1]
            else:
                a = True

            b = lastLine[i]

            if i != (len(lastLine)-1):
                c = lastLine[i+1]
            else:
                c = True
            try:
                rule = Rule(False,int(a),int(b),int(c))
            except Exception as e:
                raise e
                return
            newLine.append(self.__rules.getRulesDictionnary()[rule])
        for i in range(0, len(newLine)):
            self.__cell_tabs.SetCell(self.__cell_tabs.GetCurrentIterID(), i, newLine[i])


    def tick(self):
        lastline = []
        for item in self.__cell_tabs:
            lastline.append(item)
        self.__cell_tabs.StartNextIteration()
        try:
            self.__generateLineFromRules(lastline)
        except Exception as e:
            raise e

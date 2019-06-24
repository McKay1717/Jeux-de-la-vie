class Rule:
    def __init__(self, rule_type, b1, b2 ,b3):
        __rule = [False,-1,-1,-1]
        try:
            self.SetRuleType(rule_type)
            self.SetB1(b1)
            self.SetB2(b2)
            self.SetB3(b3)
        except Exception as e:
            raise e

    def SetRuleType(self, type):
        if type(type) is not bool:
            raise TypeError('Only Boolean is allowed')
        else:
            self.__rule[0] = type

    def GetRuleType(self):
        return self.__rule[0]

    def __SetColor(self, color, pos):
        if type(color) is not int:
            raise TypeError('Only Int is allowed')
        elif color not in [0,1,-1]:
            raise ValueError('Only 0, 1 or -1 is allowed')
        else:
            self.__rule[pos] = color

    def SetB1(self, color):
        try:
            self.__SetColor(color,1)
        except Exception as e:
            raise e

    def SetB2(self, color):
        try:
            self.__SetColor(color,2)
        except Exception as e:
            raise e

    def SetB3(self, color):
        try:
            self.__SetColor(color,2)
        except Exception as e:
            raise e


    def GetB1(self):
        return self.__rule[1]

    def GetB2(self):
        return self.__rule[2]

    def GetB3(self):
        return self.__rule[3]




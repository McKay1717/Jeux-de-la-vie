import hashlib
import binascii
class Rule:
    # -1 unknown 0 black 1 white
    def __init__(self, rule_type, b1, b2, b3):
        self.__rule = [False, -1, -1, -1]
        try:
            self.SetRuleType(rule_type)
            self.__SetB1(b1)
            self.__SetB2(b2)
            self.__SetB3(b3)
        except Exception as e:
            raise e

    def SetRuleType(self, inputType):
        if type(inputType) is not bool:
            raise TypeError('Only Boolean is allowed')
        else:
            self.__rule[0] = type

    def GetRuleType(self):
        return self.__rule[0]

    def __SetColor(self, color, pos):
        if not isinstance(color, int):
            raise TypeError('Only Int is allowed')
        elif color not in [0, 1, -1]:
            raise ValueError('Only 0, 1 or -1 is allowed')
        else:
            self.__rule[pos] = color

    def __SetB1(self, color):
        try:
            self.__SetColor(color, 1)
        except Exception as e:
            raise e

    def __SetB2(self, color):
        try:
            self.__SetColor(color, 2)
        except Exception as e:
            raise e

    def __SetB3(self, color):
        try:
            self.__SetColor(color, 3)
        except Exception as e:
            raise e

    def GetB1(self):
        return self.__rule[1]

    def GetB2(self):
        return self.__rule[2]

    def GetB3(self):
        return self.__rule[3]

    def __eq__(self, other):
        return (self.GetB1() == other.GetB1()) and (self.GetB2() == other.GetB2()) and (self.GetB3() == other.GetB3())

    def __hash__(self):
        s = str(int(self.GetB1()))+str(int(self.GetB2()))+str(int(self.GetB3()))
        return int(s, 2)
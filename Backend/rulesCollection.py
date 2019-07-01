from Backend.rule import Rule

class RulesCollection:
    def __init__(self, rulesDictionnaryInput):
        self.__rulesDictionnary = None
        try:
            self.setRulesDictionnary(rulesDictionnaryInput)
        except Exception as e:
            raise e

    def setRulesDictionnary(self, rulesDictionnaryInput):
        if type(rulesDictionnaryInput) is not dict:
            raise TypeError('Only Dictionnary is allowed')
        for key in rulesDictionnaryInput:
            if type(key) is not Rule:
                raise TypeError('Only Rule object is allowed as key')
            if type(rulesDictionnaryInput[key]) is not bool:
                raise TypeError('Only bool is allowed as value')
        self.__rulesDictionnary = rulesDictionnaryInput

    def getRulesDictionnary(self):
        return self.__rulesDictionnary




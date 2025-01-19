class Variable:
    def __init__(self, nom, valeur):
        self.nom = nom
        self.valeur = valeur

    def evaluer(self):
        return self.valeur

    def __str__(self):
        return f"{self.nom} = {self.valeur}"

class Constante:
    def __init__(self, valeur):
        self.valeur = valeur

    def evaluer(self):
        return self.valeur

    def __str__(self):
        return f"{self.valeur}"

class Terme:
    def __init__(self, operateur, opg, opd):
        self.operateur = operateur
        self.opg = opg
        self.opd = opd

    def evaluer(self):
        if self.operateur == '+':
            return self.opg.evaluer() + self.opd.evaluer()
        elif self.operateur == '-':
            return self.opg.evaluer() - self.opd.evaluer()
        elif self.operateur == '*':
            return self.opg.evaluer() * self.opd.evaluer()
        elif self.operateur == '/':
            return self.opg.evaluer() / self.opd.evaluer()

    def __str__(self):
        return f"({self.opg} {self.operateur} {self.opd})"
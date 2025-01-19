from modele import Variable, Constante, Terme

class Controleur:
    def __init__(self, vue, modele):
        self.vue = vue
        self.modele = modele

    def ajouter_variable(self, nom, valeur):
        self.modele['variables'].append(Variable(nom, valeur))
        self.vue.rafraichir_listes()

    def ajouter_constante(self, valeur):
        self.modele['constantes'].append(Constante(valeur))
        self.vue.rafraichir_listes()

    def creer_terme(self, operateur, opg_index, opd_index, is_opg_var, is_opd_var):
        opg = self.modele['variables'][opg_index] if is_opg_var else self.modele['constantes'][opg_index]
        opd = self.modele['variables'][opd_index] if is_opd_var else self.modele['constantes'][opd_index]
        terme = Terme(operateur, opg, opd)
        self.modele['expressions'].append(terme)
        self.vue.rafraichir_listes()

    def evaluer_expression(self, index):
        return self.modele['expressions'][index].evaluer()
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from controleur import Controleur

class Vue:
    def __init__(self, controleur):
        self.controleur = controleur
        self.fenetre = tk.Tk()
        self.fenetre.title("Editeur d'Expressions")
        self.fenetre.geometry("700x500")
        self.fenetre.configure(bg="#f0f0f0")

        self.selected_opg = None
        self.selected_opd = None
        self.selected_operator = None

        # Section des listes
        frame_listes = tk.Frame(self.fenetre, bg="#f0f0f0")
        frame_listes.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.liste_variables = tk.Listbox(frame_listes, height=10, width=20, bg="white", fg="black")
        self.liste_variables.grid(row=0, column=0, padx=5, pady=5)
        tk.Label(frame_listes, text="Variables", bg="#f0f0f0").grid(row=1, column=0)

        self.liste_constantes = tk.Listbox(frame_listes, height=10, width=20, bg="white", fg="black")
        self.liste_constantes.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(frame_listes, text="Constantes", bg="#f0f0f0").grid(row=1, column=1)

        self.liste_expressions = tk.Listbox(frame_listes, height=10, width=30, bg="white", fg="black")
        self.liste_expressions.grid(row=0, column=2, padx=5, pady=5)
        tk.Label(frame_listes, text="Expressions", bg="#f0f0f0").grid(row=1, column=2)

        # Section des boutons pour opérandes et opérateurs
        frame_operandes = tk.Frame(self.fenetre, bg="#f0f0f0")
        frame_operandes.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        tk.Button(frame_operandes, text="OPG", command=self.selectionner_opg, bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_operandes, text="OPD", command=self.selectionner_opd, bg="#2196f3", fg="white").pack(side=tk.LEFT, padx=5)

        frame_operateurs = tk.Frame(self.fenetre, bg="#f0f0f0")
        frame_operateurs.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        for operateur in ['+', '-', '*', '/']:
            tk.Button(frame_operateurs, text=operateur, command=lambda op=operateur: self.selectionner_operateur(op), bg="#ff9800", fg="white").pack(side=tk.LEFT, padx=5)

        # Section des boutons principaux
        frame_boutons = tk.Frame(self.fenetre, bg="#f0f0f0")
        frame_boutons.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        tk.Button(frame_boutons, text="Ajouter Variable", command=self.ajouter_variable, bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_boutons, text="Ajouter Constante", command=self.ajouter_constante, bg="#2196f3", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_boutons, text="Créer Expression", command=self.creer_expression, bg="#9c27b0", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_boutons, text="Evaluer", command=self.evaluer_expression, bg="#f44336", fg="white").pack(side=tk.LEFT, padx=5)

    def selectionner_opg(self):
        index = self.liste_variables.curselection()
        if index:
            self.selected_opg = (index[0], True)
        else:
            index = self.liste_constantes.curselection()
            if index:
                self.selected_opg = (index[0], False)

    def selectionner_opd(self):
        index = self.liste_variables.curselection()
        if index:
            self.selected_opd = (index[0], True)
        else:
            index = self.liste_constantes.curselection()
            if index:
                self.selected_opd = (index[0], False)

    def selectionner_operateur(self, operateur):
        self.selected_operator = operateur

    def creer_expression(self):
        if self.selected_opg and self.selected_opd and self.selected_operator:
            opg_index, is_opg_var = self.selected_opg
            opd_index, is_opd_var = self.selected_opd
            self.controleur.creer_terme(self.selected_operator, opg_index, opd_index, is_opg_var, is_opd_var)
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner deux opérandes et un opérateur.")

    def ajouter_variable(self):
        nom = simpledialog.askstring("Nom de la variable", "Entrez le nom :")
        valeur = simpledialog.askfloat("Valeur de la variable", "Entrez la valeur :")
        if nom and valeur is not None:
            self.controleur.ajouter_variable(nom, valeur)

    def ajouter_constante(self):
        valeur = simpledialog.askfloat("Valeur de la constante", "Entrez la valeur :")
        if valeur is not None:
            self.controleur.ajouter_constante(valeur)

    def evaluer_expression(self):
        index = self.liste_expressions.curselection()
        if index:
            resultat = self.controleur.evaluer_expression(index[0])
            messagebox.showinfo("Resultat", f"Le resultat est : {resultat}")

    def rafraichir_listes(self):
        self.liste_variables.delete(0, tk.END)
        self.liste_constantes.delete(0, tk.END)
        self.liste_expressions.delete(0, tk.END)

        for variable in self.controleur.modele['variables']:
            self.liste_variables.insert(tk.END, str(variable))

        for constante in self.controleur.modele['constantes']:
            self.liste_constantes.insert(tk.END, str(constante))

        for expression in self.controleur.modele['expressions']:
            self.liste_expressions.insert(tk.END, str(expression))

if __name__ == "__main__":
    from modele import Variable, Constante, Terme
    modele = {'variables': [], 'constantes': [], 'expressions': []}
    vue = Vue(None)
    controleur = Controleur(vue, modele)
    vue.controleur = controleur
    vue.fenetre.mainloop()
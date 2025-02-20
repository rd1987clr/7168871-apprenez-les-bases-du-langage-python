def salaire_mensuel(salaire_annuel)
  salaire_mensuel = salaire_annuel/12
  return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel)
  salaire_hebdomadaire = salaire_mensuel/4
  return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees)
  salaire_horaire = salaire_hebdomadaire/heures_travaillees
  return salaire_horaire

salaire_annuel = float(input("Quel est votre salaire annuel?"))
heures_travaillees = float(input("Combien d'heures travaillez-vous par semaine?"))

mensuel=salaire_mensuel(salaire_annuel)
hebdomadaire=salaire_hebdomadaire(salaire_mensuel)
horaire=salaire_horaire(salaire_hebdomadaire, heures_travaillees)

print(f("Votre salaire horaire est de {horaire} euros"))


# Testeur de Compatibilité Amoureuse par les Prénoms

Une application web simple et ludique développée avec **Streamlit** pour calculer la compatibilité entre deux prénoms. Le calcul se base sur les lettres communes entre les prénoms, avec une petite variation pour ajouter un côté « magique » au résultat. L’application affiche également un commentaire personnalisé selon le score obtenu.

🔗 **Accéder à l'application** : [https://prenom-compatibilite.streamlit.app/](https://prenom-compatibilite.streamlit.app/)

---

## Fonctionnalités

* Saisie facile de deux prénoms via une interface web conviviale.
* Calcul automatique d’un score de compatibilité en pourcentage.
* Affichage d’un commentaire amusant et personnalisé selon le score.
* Interface légère et rapide grâce à Streamlit.

---

## Installation

1. **Cloner le dépôt** (ou copier le script) :

```bash
git clone https://ton_depot.git
cd nom_du_dossier
```

2. **Créer un environnement virtuel (optionnel mais recommandé)** :

```bash
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
```

3. **Installer les dépendances** :

```bash
pip install streamlit
```

---

## Utilisation

Lancer l’application avec la commande :

```bash
streamlit run nom_du_script.py
```

Une fenêtre web s’ouvrira automatiquement (ou un lien sera affiché dans la console) où tu pourras entrer deux prénoms et découvrir leur compatibilité.

---

## Exemple

* Prénom 1 : **Alice**
* Prénom 2 : **David**

Résultat :
💖 **Score de compatibilité : 67%**
*Une très belle compatibilité ! Il y a clairement une étincelle entre vous. 🔥*

---

## Personnalisation

Tu peux modifier la fonction `calculer_compatibilite` ou les commentaires dans `commentaire_compatibilite` pour ajuster la logique ou les messages selon tes préférences.

---

## Contributions

Contributions bienvenues ! N’hésite pas à proposer des améliorations, des idées de fonctionnalités, ou des corrections.

---

## Licence

Ce projet est sous licence MIT — libre d’utilisation et modification.

import streamlit as st

def calculer_compatibilite(prenom1, prenom2):
    prenom1_normalise = prenom1.lower().strip()
    prenom2_normalise = prenom2.lower().strip()

    if prenom1_normalise == prenom2_normalise:
        return 100

    lettres_prenom1 = set(prenom1_normalise)
    lettres_prenom2 = set(prenom2_normalise)
    lettres_communes = lettres_prenom1.intersection(lettres_prenom2)
    toutes_lettres_uniques = lettres_prenom1.union(lettres_prenom2)

    if not toutes_lettres_uniques:
        return 0

    score = (len(lettres_communes) / len(toutes_lettres_uniques)) * 100
    variation = (len(prenom1) + len(prenom2)) % 21
    score_final = min(100, int(score + variation))

    return score_final

def commentaire_compatibilite(score):
    if score >= 80:
        return "Wow ! Une connexion presque parfaite. Les étoiles semblent alignées pour vous ! ✨"
    elif score >= 60:
        return "Une très belle compatibilité ! Il y a clairement une étincelle entre vous. 🔥"
    elif score >= 40:
        return "Une compatibilité intéressante. L'aventure ne fait que commencer ! 😊"
    elif score >= 20:
        return "Les opposés s'attirent, n'est-ce pas ? Un peu de mystère, c'est excitant ! 😉"
    else:
        return "C'est peut-être le début d'une amitié inattendue. Qui sait ce que l'avenir vous réserve ? 🤔"

# Interface Streamlit
st.title("💘 Testeur de Compatibilité Amoureuse 💘")
st.markdown("Entrez deux prénoms pour découvrir leur compatibilité magique ✨")

prenom1 = st.text_input("Prénom 1")
prenom2 = st.text_input("Prénom 2")

if st.button("Calculer la compatibilité"):
    if prenom1 and prenom2:
        score = calculer_compatibilite(prenom1, prenom2)
        commentaire = commentaire_compatibilite(score)

        st.markdown(f"### 💖 Score de compatibilité : {score}%")
        st.markdown(f"**{commentaire}**")
    else:
        st.warning("Veuillez entrer deux prénoms pour lancer le calcul.")

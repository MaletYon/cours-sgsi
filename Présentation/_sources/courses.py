"""Métadonnées du cours SGSI (SIS498, Université de Garoua) et répartition des
15 séances de 2 heures (30 heures)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

SGSI = {
    "sigle": "SGSI",
    "code": "SIS498",
    "titre": "Systèmes de Gestion de la Sécurité Informatique",
    "sous_titre": "Du risque à la certification : piloter la sécurité de l'information",
    "master": "Master Professionnel en Sécurité des Systèmes Informatiques et des Données",
    "bandeau": "Université de Garoua",
    "ecole": "Faculté des Sciences",
    "logo_g": "garoua",
    "logo_d": "garoua",
    "n_jours": 15,
    "annee": "2026-2027",
    "dossier": COURS + r"\UG-DMI\SIS498\Présentation",
    "fil_rouge": "Mairie d'Eséka : NYONG, KELLÉ, MAKAK, MATOMB",
    "parties": [
        ("Prologue", "La décision de la mairie", "P00"),
        ("Partie I", "Fondements du management", "C01-C03"),
        ("Partie II", "Gouvernance et politique", "C04-C06"),
        ("Partie III", "Le SMSI selon ISO/IEC 27001", "C07-C10"),
        ("Partie IV", "Appréciation et traitement des risques", "C11-C14"),
        ("Partie V", "Mettre en œuvre les mesures", "C15-C17"),
        ("Partie VI", "Contrôler, auditer, améliorer", "C18-C20"),
    ],
    # jour : (thème court, contenu détaillé, ateliers/chapitres, labs)
    "jours": {
        1: ("Ouverture · La décision de la mairie", "Présentation du cours + Prologue", ["P00"], []),
        2: ("Qu'est-ce que la sécurité de l'information", "C01", ["C01"], ["LAB-01"]),
        3: ("Du risque à la décision · Le cycle PDCA", "C02 + C03", ["C02", "C03"], []),
        4: ("La gouvernance · La politique de sécurité", "C04 + C05", ["C04", "C05"], ["LAB-02"]),
        5: ("Chartes, conformité et protection des données", "C06", ["C06"], []),
        6: ("La famille ISO/IEC 27000 et le SMSI", "C07", ["C07"], []),
        7: ("Contexte, leadership, planification", "C08", ["C08"], ["LAB-03"]),
        8: ("Support, évaluation, amélioration · ISO 27002", "C09 + C10", ["C09", "C10"], []),
        9: ("Concepts et vocabulaire du risque", "C11", ["C11"], []),
        10: ("Les méthodes d'appréciation des risques", "C12", ["C12"], ["LAB-04"]),
        11: ("Cartographie, traitement · Déclaration d'applicabilité", "C13 + C14", ["C13", "C14"], ["LAB-05", "LAB-06"]),
        12: ("Mesures organisationnelles et humaines", "C15", ["C15"], []),
        13: ("Mesures techniques · Continuité (PCA/PRA)", "C16 + C17", ["C16", "C17"], ["LAB-07", "LAB-08"]),
        14: ("Surveillance, mesure et indicateurs", "C18", ["C18"], ["LAB-09"]),
        15: ("Audit et certification · Incidents · clôture", "C19 + C20", ["C19", "C20"], ["LAB-10"]),
    },
}

ALL = {"SGSI": SGSI}

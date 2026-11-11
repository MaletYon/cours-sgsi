# Systèmes de Gestion de la Sécurité Informatique (SGSI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](SGSI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE SIS498** · Université de Garoua · Faculté des Sciences · Département de Mathématiques et Informatiques · Master Professionnel en Sécurité des Systèmes Informatiques et des Données · 30 heures
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel · contact : maletyon@proton.me · année académique 2026-2027

> *La sécurité n'est pas un produit que l'on achète, c'est une décision que l'on tient dans la durée.*

Ce cours enseigne le management de la sécurité de l'information : comment une organisation décide sa sécurité, la met en œuvre et la tient jusqu'à la certification. Il couvre les fondements (triade DIC, risque et décision, cycle PDCA), la gouvernance et la politique (RSSI, comité de sécurité, PSSI, chartes, conformité et protection des données), le système de management selon ISO/IEC 27001 (famille 27000, clauses 4 à 10, ISO/IEC 27002 et l'Annexe A), l'appréciation et le traitement des risques (vocabulaire, EBIOS Risk Manager, OCTAVE, MEHARI, cartographie, déclaration d'applicabilité), la mise en œuvre des mesures (organisationnelles et humaines, techniques, continuité d'activité PCA/PRA) et le contrôle (surveillance et indicateurs, audit et certification, gestion des incidents et amélioration). Un fil directeur parcourt le cours : le cycle PDCA. L'ensemble s'appuie sur la famille ISO/IEC 27000 (27001, 27002, 27005), ISO 31000, ISO 22301, ISO 19011, le NIST CSF, EBIOS Risk Manager (ANSSI), ainsi que les lois camerounaises 2010/012 et 2024/017 et la Convention de Malabo. Le fil rouge est la mairie d'Eséka, dans le Nyong-et-Kéllé : après un incident, elle bâtit un système de management de la sécurité de l'information et le conduit vers la certification, à travers quatre phases (NYONG, KELLÉ, MAKAK, MATOMB). Les noms, dates et montants sont fictifs ; les normes et les textes de loi sont cités d'après leur version officielle.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`SGSI_main.pdf`](SGSI_main.pdf) | Traité complet (prologue, six parties, 20 chapitres, annexes) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations : vision d'ensemble et 15 séances de 2 heures |
| Les fiches d'exercices | [`fiches/`](fiches/) | 21 fiches de 40 questions, une par chapitre (prologue compris) |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, [`Style_SGSI.sty`](Style_SGSI.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | La décision de la mairie | [`partie0/`](partie0/) |
| **I. Fondements du management** | 1. Sécurité de l'information · 2. Du risque à la décision · 3. Le cycle PDCA | [`partie1/`](partie1/) |
| **II. Gouvernance et politique** | 4. La gouvernance · 5. La politique de sécurité · 6. Chartes, conformité et données | [`partie2/`](partie2/) |
| **III. Le SMSI selon ISO/IEC 27001** | 7. La famille 27000 · 8. Contexte, leadership, planification · 9. Support, fonctionnement, évaluation, amélioration · 10. ISO/IEC 27002 et les mesures | [`partie3/`](partie3/) |
| **IV. Appréciation et traitement des risques** | 11. Vocabulaire du risque · 12. Les méthodes · 13. Cartographie et traitement · 14. La déclaration d'applicabilité | [`partie4/`](partie4/) |
| **V. Mettre en œuvre les mesures** | 15. Mesures organisationnelles et humaines · 16. Mesures techniques · 17. Continuité : PCA et PRA | [`partie5/`](partie5/) |
| **VI. Contrôler, auditer, améliorer** | 18. Surveillance et indicateurs · 19. Audit et certification · 20. Gérer les incidents et progresser | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles · D. Textes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

Chaque chapitre compte dix exercices gradués ; leurs corrigés, et ceux des fiches, sont dans le livret de correction. Les fiches et les labs se font hors des 30 heures.

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et dix laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **SIS498**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-sgsi/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-sgsi/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-sgsi/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-sgsi/raw/main/ndap-sukulu/NDAP_SUKULU_SGSI_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré ; il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet, pour l'étudiant et pour l'enseignant, est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md). Les fiches de 40 questions au format texte restent disponibles dans [`fiches/`](fiches/).

| Lab | Chapitre | Sujet |
|---|---|---|
| SGSI-LAB-01 | 1 | Inventaire et classification des actifs |
| SGSI-LAB-02 | 5 | Rédiger une politique de sécurité |
| SGSI-LAB-03 | 8 | Analyse d'écart ISO 27001 (gap analysis) |
| SGSI-LAB-04 | 12 | Appréciation des risques (EBIOS Risk Manager) |
| SGSI-LAB-05 | 13 | Matrice et traitement des risques |
| SGSI-LAB-06 | 14 | Construire une déclaration d'applicabilité |
| SGSI-LAB-07 | 16 | Contrôle d'accès et moindre privilège (RBAC) |
| SGSI-LAB-08 | 17 | Plan de continuité et sauvegarde 3-2-1 |
| SGSI-LAB-09 | 18 | Tableau de bord d'indicateurs de sécurité |
| SGSI-LAB-10 | 19 | Audit interne et non-conformités |

Tous les labs se pratiquent sur pièces (inventaires, registres de risques, extraits de politique, tableaux de bord) en environnement fermé.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex SGSI_main`, `biber SGSI_main`, `makeindex SGSI_main`, puis deux fois `pdflatex SGSI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/gen_specs.py` puis `python Présentation/_sources/run.py SGSI all` (Python 3 et python-pptx).

## Les trois cours de l'Université de Garoua

Ce cours fait partie d'un corpus de trois UE du Master SSID : Supervision, Analyse Forensique et Gestion des Incidents ([SIS589](https://github.com/maletyon/cours-safi)), Forensique Numérique ([LPI342](https://github.com/maletyon/cours-forn)), Systèmes de Gestion de la Sécurité Informatique (SIS498).

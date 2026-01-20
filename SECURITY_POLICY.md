# Politique de Sécurité DevSecOps

Ce document définit les règles de gestion des vulnérabilités pour le projet Python Demo.

## 1. Niveaux de Gravité (CVSS)

Nous utilisons les standards de l'industrie pour classer les vulnérabilités :

- **LOW** (Faible) : Impact limité, exploitation difficile.
- **MEDIUM** (Moyen) : Impact modéré, peut nécessiter une configuration spécifique.
- **HIGH** (Élevé) : Risque important de compromission.
- **CRITICAL** (Critique) : Prise de contrôle totale ou fuite de données majeure immédiate.

## 2. Critères de Blocage du Pipeline

Le pipeline CI/CD est configuré pour **échouer (bloquer la mise en production)** si :
- Une vulnérabilité de niveau **HIGH** ou **CRITICAL** est détectée par `pip-audit` ou `bandit`.
- *(Note : Actuellement, pip-audit bloque par défaut sur toute vulnérabilité trouvée).*

## 3. Processus de Correction

Si le pipeline échoue à cause d'une vulnérabilité :

1.  **Identifier** : Lire les logs de la CI pour voir quel paquet est touché (ex: `requests`).
2.  **Analyser** : Vérifier si une version corrigée existe (ex: passer de 2.19.0 à 2.31.0+).
3.  **Corriger** :
    - Mettre à jour la version dans `requirements.txt`.
    - Tester l'application pour éviter les régressions.
4.  **Ignorer (Cas exceptionnel)** :
    - Si c'est un "Faux Positif", utiliser l'option `--ignore-vuln <ID>` dans la configuration CI avec une justification.

## 4. Responsabilités

- **Développeur** : Responsable de ne pas introduire de nouvelles vulnérabilités et de corriger celles bloquant ses Pull Requests.
- **Security Champion / Lead Dev** : Responsable de la validation des exceptions (ignorer une faille) et de la veille sécurité.
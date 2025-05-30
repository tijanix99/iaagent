# Site Web Adapté - Template Materio pour Agent IA WhatsApp

Ce projet est une adaptation du template Materio MUI Next.js Free, modifiée pour correspondre aux besoins décrits dans le cahier des charges `cdc.pdf`.

## Structure Modifiée

Le template original a été modifié comme suit :

*   **Pages/Composants Supprimés :** Les pages et composants non pertinents pour le projet (ex: exemples de cartes, widgets de dashboard par défaut) ont été retirés.
*   **Navigation Adaptée :** Le menu de navigation vertical a été restructuré pour inclure les sections principales requises : Accueil, Produits, Commandes, Messages, Statistiques, Paramètres Boutique, Profil Utilisateur.
*   **Pages Principales Créées :** Des pages de base ont été créées pour chaque section du menu (Produits, Commandes, Messages, Statistiques, Paramètres). Ces pages contiennent actuellement une structure minimale et devront être complétées avec les fonctionnalités spécifiques (tableaux de données, formulaires, graphiques, appels API vers le backend).
*   **Page d'Accueil Modifiée :** La page d'accueil par défaut a été nettoyée pour accueillir les futurs widgets de statistiques clés.

## Installation

1.  **Extraire l'archive :** Décompressez le fichier `site_adapte_sans_node_modules.zip` dans le répertoire de votre choix.
2.  **Ouvrir un terminal :** Naviguez jusqu'au dossier extrait (le dossier qui contient `package.json`).
3.  **Installer les dépendances :** Exécutez la commande suivante. Assurez-vous d'avoir `pnpm` installé (ou utilisez `npm install` / `yarn install` si vous préférez ces gestionnaires) :
    ```bash
    pnpm install
    ```
4.  **Lancer le serveur de développement :**
    ```bash
    pnpm dev
    ```
    Le site devrait être accessible sur `http://localhost:3000` (ou un autre port si celui-ci est occupé).

## Prochaines Étapes

*   **Implémenter les Fonctionnalités :** Compléter le contenu et la logique de chaque page (Produits, Commandes, Messages, Statistiques, Paramètres) en intégrant les tableaux, formulaires, graphiques et les appels API nécessaires pour interagir avec votre backend.
*   **Connecter au Backend :** Relier ce frontend aux API de votre backend (Python/Node.js) pour la gestion des données, l'authentification, l'interaction avec WhatsApp (Baileys), ChatGPT, etc.
*   **Développement Spécifique :** Ajouter toute fonctionnalité spécifique non couverte par le template de base (ex: affichage QR code Baileys, gestion multi-comptes).

## Fichier de Mapping

Le fichier `mapping_cdc_template.md` (fourni séparément) détaille les correspondances effectuées entre le cahier des charges et le template.


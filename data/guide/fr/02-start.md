title: Premiers pas
icon: system-software-install
summary: Installer, compléter les composants, lancer l'assistant.
---
## Installer Boomerang
1. Téléchargez le paquet `.deb` depuis la page des versions du projet.
2. Dans un terminal, depuis le dossier du téléchargement, lancez `sudo apt install ./boomerang_*.deb` et saisissez votre mot de passe. apt installe en même temps les paquets nécessaires. Sur Ubuntu, vous pouvez aussi ouvrir le fichier dans le Centre d'applications par un double-clic.
3. Fermez puis rouvrez votre session pour démarrer le service d'arrière-plan de Boomerang.
4. Ouvrez Boomerang depuis le menu des applications.

## Composants manquants
Si un composant manque sur votre système, Boomerang l'indique dans une carte **Composants manquants**, au début de l'assistant et dans les [Réglages](app:settings).
1. Lisez la liste : chaque ligne indique à quoi sert le composant.
2. Cliquez sur **Installer**. Votre mot de passe vous est demandé une seule fois.
3. Attendez que la barre de progression soit complète. La carte disparaît quand tous les composants sont installés.

!warn Certains composants ne s'installent pas depuis Boomerang, par exemple un PipeWire plus récent pour les appels sur elementary OS 8. La carte l'indique par « Mise à jour du système nécessaire ». Les autres fonctions de Boomerang restent disponibles.

## L'assistant de configuration
Au premier lancement, un assistant plein écran vous accueille :
1. Choisissez ce que vous voulez relier : votre iPhone, votre compte Apple, ou les deux.
2. Suivez les étapes. Chaque étape est cochée automatiquement une fois terminée.
3. Choisissez les apps séparées à afficher.
4. Terminez. Vous pouvez aussi cliquer sur **Passer la configuration** et reprendre la configuration plus tard.

Pour relancer l'assistant : [Réglages › Configuration initiale](app:setup).

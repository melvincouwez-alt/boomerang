title: Compte Apple
icon: preferences-desktop-online-accounts
summary: Courriel, agendas, rappels, contacts, iCloud Drive et Photos.
---
## Courriel, agendas, rappels et contacts
Ces services utilisent un **mot de passe pour app**, différent de celui de votre compte Apple.
1. Sur account.apple.com, ouvrez **Connexion et sécurité › Mots de passe pour les apps**, puis créez un mot de passe nommé « Boomerang ».
2. Dans [Services Apple](app:services), cliquez sur **Se connecter…**
3. Saisissez votre identifiant Apple et ce mot de passe. Boomerang vérifie ce mot de passe auprès d'Apple et l'enregistre dans le trousseau de votre session.
4. Vos comptes apparaissent dans Courriel, Tâches et Agenda.

Pour retirer l'accès, cliquez sur **Déconnecter** dans Services Apple, puis supprimez le mot de passe pour app sur account.apple.com.

## iCloud Drive et iCloud Photos
Ces deux services passent par **rclone**, un outil libre qui se connecte à iCloud de la même façon que le site icloud.com.

!warn Lisez cet avertissement avant de vous connecter. La connexion nécessite le **mot de passe de votre compte Apple** et un code affiché sur l'iPhone. Apple ne propose pas officiellement cet accès : ses conditions d'utilisation d'iCloud limitent l'accès automatisé et lui permettent de suspendre un compte. Vous devez aussi désactiver la **Protection avancée des données**, ce qui réduit le chiffrement de bout en bout de vos données iCloud. Vous utilisez cette fonction à vos risques.

1. Dans Services Apple, cliquez sur **Connecter…** à côté d'iCloud Drive.
2. Saisissez le mot de passe du compte Apple, puis le code à six chiffres affiché sur l'iPhone.
3. Le dossier **iCloud Drive** apparaît dans votre dossier personnel et dans Fichiers.
4. Pour les photos : **Connecter…** à côté d'iCloud Photos. Le dossier **iCloud Photos** apparaît dans vos Images, en lecture seule. Chaque album est un dossier.

- Les options (icône de roue dentée) règlent l'emplacement, le montage à l'ouverture de session, la lecture seule, l'espace utilisé hors ligne et le délai d'apparition des changements.
- Boomerang n'effectue pas de synchronisation complète dans les deux sens : un conflit ou une suppression massive pourrait faire perdre des fichiers.
- Environ une fois par mois, Apple demande de confirmer de nouveau la connexion. Cliquez alors sur **Reconnecter…** dans Services Apple et saisissez un nouveau code.
- Ces deux services nécessitent rclone 1.69 ou une version plus récente. Si la version installée est plus ancienne, la carte **Composants manquants** l'indique.

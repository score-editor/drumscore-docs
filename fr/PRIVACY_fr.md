**Remarque:** Cette politique de confidentialité est une traduction fournie pour plus de commodité. En cas de divergence, la version anglaise fait foi.

# Politique de Confidentialité de DrumScore Editor

**AVIS IMPORTANT:** Ceci est une traduction de référence générée par IA et DOIT être révisée par un traducteur professionnel ou un juriste bilingue avant toute utilisation légale. En cas de divergence, la version anglaise fait foi.

**Date d'entrée en vigueur :** 17 novembre 2025  
**Version :** 1.0

Alan White (« nous », « notre » ou « nos ») exploite DrumScore Editor (« le Logiciel »). Cette Politique de Confidentialité explique comment nous collectons, utilisons et protégeons les informations lorsque vous utilisez le Logiciel.

---

## 1. Informations que Nous Collectons

### 1.1 Informations Stockées Localement

Le Logiciel stocke les informations suivantes **localement sur votre appareil uniquement** :

- **Préférences Utilisateur :** Paramètres de l'application, choix de thème, préférences linguistiques, options d'affichage
- **Informations de Licence :** Votre clé de licence (cryptée), nom du titulaire de licence et adresse e-mail
- **Partitions Musicales :** Toutes les compositions et arrangements que vous créez
- **Fichiers Récents :** Chemins d'accès aux fichiers récemment ouverts
- **Positions des Fenêtres :** Taille et position des fenêtres de l'application

**Ces données ne quittent jamais votre ordinateur**, sauf si vous choisissez explicitement de partager des fichiers ou d'activer les fonctionnalités optionnelles décrites ci-dessous.

### 1.2 Analyses d'Usage Anonymes (Optionnel)

À partir de la version [X.X], le Logiciel inclut des analyses d'utilisation anonymes optionnelles. Lorsqu'elles sont activées, nous collectons :

**Ce que nous collectons :**
- Fonctionnalités utilisées et fréquence d'utilisation
- Version du logiciel et système d'exploitation
- Durée des sessions
- Rapports de plantage et journaux d'erreurs
- Modèles généraux de flux de travail (par exemple, « l'utilisateur a créé une volta », « l'utilisateur a exporté en PDF »)

**Ce que nous ne collectons PAS :**
- Votre nom, e-mail ou informations de licence
- Vos compositions musicales ou le contenu des partitions
- Noms de fichiers, chemins ou métadonnées de fichiers
- Adresses IP ou identifiants d'appareil
- Toute information personnellement identifiable

**Identifiant Anonyme :** Nous générons un identifiant anonyme aléatoire (UUID) stocké localement pour nous aider à comprendre les modèles d'utilisation sans vous identifier personnellement.

**Désactivation :** Vous pouvez désactiver les analyses à tout moment dans Préférences → Confidentialité. Ce paramètre est respecté immédiatement.

### 1.3 Vérification des Mises à Jour (Optionnel)

Le Logiciel peut vérifier périodiquement les mises à jour disponibles. Lorsqu'elle est activée, la vérification des mises à jour transmet :

- Version actuelle du Logiciel
- Type et version du système d'exploitation

**Aucune information personnellement identifiable n'est transmise lors des vérifications de mise à jour.**

**Désactivation :** Vous pouvez désactiver la vérification automatique des mises à jour dans Préférences → Mises à jour.

---

## 2. Comment Nous Utilisons les Informations

### 2.1 Données Locales
Les préférences et fichiers stockés localement sont utilisés uniquement pour :
- Fournir les fonctionnalités de base du Logiciel
- Mémoriser vos paramètres entre les sessions
- Valider votre licence hors ligne
- Activer les fonctionnalités que vous avez configurées

### 2.2 Analyses Anonymes
Les données d'utilisation anonymes sont utilisées pour :
- Comprendre quelles fonctionnalités sont les plus utiles
- Identifier les domaines à améliorer
- Prioriser les efforts de développement
- Détecter et corriger les bugs
- Améliorer l'expérience utilisateur globale

### 2.3 Informations de Mise à Jour
Les données de vérification des mises à jour sont utilisées uniquement pour :
- Vous informer des mises à jour disponibles
- Assurer la compatibilité avec votre système d'exploitation
- Améliorer le système de livraison des mises à jour

---

## 3. Stockage et Sécurité des Données

### 3.1 Stockage Local
Vos préférences, partitions et informations de licence sont stockées à l'aide de l'API Java Preferences et du stockage du système de fichiers sur votre ordinateur. Les clés de licence sont cryptées à l'aide d'un cryptage standard de l'industrie (PBEWithMD5AndDES).

### 3.2 Données d'Analyse
Si vous activez les analyses, les données anonymes sont transmises via HTTPS vers notre serveur sécurisé et stockées pour analyse. Ces données ne peuvent pas être liées à vous personnellement.

### 3.3 Pas de Stockage Cloud
Nous ne stockons pas vos compositions musicales ou données personnelles sur un service cloud. Votre travail reste sur votre appareil, sauf si vous choisissez de l'exporter ou de le partager.

---

## 4. Partage de Données et Tiers

### 4.1 Pas de Vente de Données
Nous ne vendons, ne louons ni n'échangeons aucune information collectée par le Logiciel.

### 4.2 Services Tiers
Le Logiciel ne s'intègre pas avec des services d'analyse tiers, des réseaux publicitaires ou des courtiers de données.

### 4.3 Exigences Légales
Nous pouvons divulguer des informations si la loi l'exige, par ordonnance judiciaire ou pour protéger nos droits légaux. Cependant, étant donné que nous collectons un minimum de données et que la plupart sont stockées localement, il y a très peu que nous pourrions divulguer.

---

## 5. Vos Droits et Choix

### 5.1 Accéder à Vos Données
Toutes vos données sont stockées localement sur votre appareil. Vous avez un accès complet à :
- Vos partitions musicales (dans votre système de fichiers)
- Vos préférences (via le menu Préférences)
- Vos informations de licence (via la boîte de dialogue Licence)

### 5.2 Supprimer Vos Données
Vous pouvez supprimer toutes vos données à tout moment :
- **Partitions :** Supprimez les fichiers de votre système de fichiers
- **Préférences :** Réinitialisez aux valeurs par défaut dans le menu Préférences
- **Licence :** Supprimez la licence avec la commande : `DrumScoreEditor removeLicense`
- **Analyses :** Désactivez dans les Préférences (aucune donnée passée ne peut être liée à vous de toute façon)

### 5.3 Désactiver les Analyses et les Mises à Jour
Les analyses anonymes et la vérification des mises à jour sont toutes deux **opt-out** :
1. Ouvrez Préférences → Confidentialité
2. Décochez « Envoyer des statistiques d'utilisation anonymes »
3. Décochez « Vérifier automatiquement les mises à jour »

Les modifications prennent effet immédiatement.

---

## 6. Confidentialité des Enfants

Le Logiciel n'est pas destiné aux enfants de moins de 13 ans. Nous ne collectons pas sciemment d'informations auprès d'enfants. Si nous apprenons que nous avons collecté des informations auprès d'un enfant de moins de 13 ans, nous les supprimerons rapidement.

---

## 7. Utilisateurs Internationaux

Le Logiciel est développé en Écosse (Royaume-Uni) mais utilisé internationalement. En utilisant le Logiciel :
- Les données stockées localement restent sur votre appareil dans votre juridiction
- Les analyses anonymes (si activées) sont transmises à des serveurs au Royaume-Uni/UE
- Vous consentez au traitement des données anonymes conformément aux normes de protection des données du Royaume-Uni/UE

### 7.1 Droits RGPD (Utilisateurs de l'UE)
Si vous êtes dans l'Union européenne, vous disposez de droits en vertu du RGPD :
- **Droit d'Accès :** Vous pouvez accéder à toutes les données stockées localement
- **Droit à l'Effacement :** Vous pouvez supprimer toutes les données à tout moment
- **Droit d'Opposition :** Vous pouvez refuser les analyses
- **Droit à la Portabilité des Données :** Vos partitions sont au format MusicXML ouvert

Étant donné que nous collectons un minimum de données anonymes et que la plupart des données sont stockées localement, ces droits sont en grande partie déjà respectés par la conception du Logiciel.

---

## 8. Conservation des Données

### 8.1 Données Locales
Les données stockées sur votre appareil persistent jusqu'à ce que vous les supprimiez. Nous n'avons pas accès à ces données et ne les contrôlons pas.

### 8.2 Analyses Anonymes
Si elles sont collectées, les données d'analyse anonymes sont conservées pendant 24 mois, après quoi elles sont automatiquement supprimées.

### 8.3 Journaux de Vérification des Mises à Jour
Les journaux de vérification des mises à jour sont conservés pendant 90 jours à des fins de dépannage, puis automatiquement supprimés.

---

## 9. Sécurité

### 9.1 Sécurité Locale
La sécurité de votre appareil est de votre responsabilité. Nous recommandons :
- D'utiliser des mots de passe d'appareil forts
- De maintenir votre système d'exploitation à jour
- D'utiliser un logiciel antivirus
- De sauvegarder régulièrement vos partitions

### 9.2 Sécurité de Transmission
Toutes les données transmises par le Logiciel (vérifications de mises à jour, analyses) utilisent le cryptage HTTPS.

### 9.3 Cryptage de la Clé de Licence
Les clés de licence sont stockées dans un format crypté sur votre appareil.

---

## 10. Modifications de Cette Politique de Confidentialité

### 10.1 Langue
Cette Politique de Confidentialité est rédigée à l'origine en anglais. Des traductions sont fournies pour des raisons de commodité, mais en cas de conflit ou de divergence entre la version anglaise et toute traduction, la version anglaise prévaudra et régira.

### 10.2 Mises à Jour
Nous pouvons mettre à jour cette Politique de Confidentialité de temps à autre. Les modifications seront publiées sur drumscore.scot/privacy avec une « Date d'entrée en vigueur » mise à jour.

**Les modifications importantes** (celles affectant la manière dont nous collectons ou utilisons les données) seront mises en évidence dans les notes de version du Logiciel.

**L'utilisation continue** du Logiciel après la publication des modifications constitue l'acceptation de la Politique de Confidentialité mise à jour.

---

## 11. Nous Contacter

Si vous avez des questions concernant cette Politique de Confidentialité ou la manière dont vos données sont traitées :

**E-mail :** alan@drumscore.scot  
**Site Web :** https://drumscore.scot  
**Adresse :** [Votre adresse professionnelle si requis par la loi locale]

---

## 12. Résumé

**En Français Simple :**

- ✅ Vos partitions et données restent sur votre ordinateur
- ✅ Nous collectons un minimum de statistiques d'utilisation anonymes (si vous l'autorisez)
- ✅ Vous pouvez tout refuser à tout moment
- ✅ Nous ne vendons pas vos données
- ✅ Nous n'utilisons pas de traceurs tiers
- ✅ Votre clé de licence est cryptée
- ✅ Pas de stockage cloud de votre travail

**Des questions ?** Contactez-nous à alan@drumscore.scot

---

**En utilisant DrumScore Editor, vous reconnaissez avoir lu et compris cette Politique de Confidentialité.**
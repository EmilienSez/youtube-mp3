# 🎵 Projet PyQt : YouTube MP3 Downloader

## Objectif
Créer une application de bureau (desktop) avec PyQt5/PyQt6 permettant de :
- Ajouter plusieurs liens YouTube à une liste.
- Télécharger automatiquement l'audio de chaque vidéo au format MP3.
- Afficher une interface simple, intuitive et fluide.

---

## ✅ Étapes principales (To-Do)

### 1. ⚙️ Préparation du projet
- [x] Créer un dossier de projet Python (`youtube_mp3_downloader/`)
- [x] Créer un environnement virtuel (optionnel mais recommandé)
- [x] Installer les dépendances :  
  `pip install yt-dlp PyQt5`
- [~] Installer FFmpeg sur la machine (nécessaire pour la conversion en MP3)

### 2. 🖼️ Création de l’interface utilisateur (Frontend - PyQt)
- [ ] Créer une fenêtre principale (QMainWindow ou QWidget)
- [ ] Ajouter un champ de saisie pour les liens YouTube (`QLineEdit`)
- [ ] Ajouter un bouton "Ajouter à la liste" (`QPushButton`)
- [ ] Ajouter une `QListWidget` pour afficher les liens en file d’attente
- [ ] Ajouter un bouton "Supprimer la sélection"
- [ ] Ajouter un bouton "Télécharger la liste"
- [ ] (Optionnel) Ajouter une barre de progression pour les téléchargements

### 3. 🔧 Développement de la logique (Backend)
- [ ] Créer une classe ou une fonction pour ajouter les liens à une file
- [ ] Créer une fonction qui utilise `yt-dlp` pour télécharger un seul lien
- [ ] Utiliser les options de `yt-dlp` pour convertir en MP3 via FFmpeg
- [ ] Gérer le téléchargement de plusieurs liens à la suite
- [ ] (Optionnel) Télécharger en parallèle (threading ou multiprocessing)
- [ ] Prévoir la gestion des erreurs (lien invalide, coupure réseau, etc.)

### 4. 🔁 Connexion frontend/backend
- [ ] Connecter le bouton "Ajouter" à la liste d’attente
- [ ] Connecter le bouton "Supprimer" pour retirer un lien de la liste
- [ ] Connecter le bouton "Télécharger" à la logique de traitement
- [ ] Afficher les logs ou erreurs dans une `QTextEdit` ou via pop-up

### 5. 🧪 Tests et améliorations
- [ ] Tester le fonctionnement avec différents types de vidéos YouTube
- [ ] Ajouter une vérification de format ou de validité de l’URL
- [ ] Ajouter des infos sur les vidéos (titre, durée, etc.)
- [ ] Ajouter un paramètre pour choisir le dossier de téléchargement
- [ ] Ajouter une option pour choisir le format (MP3, M4A, etc.)

---

## 💡 Bonus / idées futures
- [ ] Drag-and-drop de liens YouTube dans la liste
- [ ] Mode sombre / clair
- [ ] Système de logs enregistrés sur disque
- [ ] Intégration de l’API YouTube pour récupérer les titres automatiquement
- [ ] Version "portable" en .exe (via PyInstaller)

---

## 🧰 Stack technique
- Python
- PyQt5 (ou PyQt6)
- yt-dlp
- FFmpeg

---

## 📁 Structure projet (suggestion)
youtube_mp3_downloader/
│
├── main.py # Point d’entrée de l’application
├── ui/ # Fichiers relatifs à l’interface Qt
│ └── main_window.py
├── logic/ # Code métier (téléchargement, queue, etc.)
│ └── downloader.py
├── assets/ # Icônes, logos (si besoin)
├── README.md # Description du projet
└── requirements.txt # Dépendances
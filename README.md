# TETROS

Le groupe de NSI de F1 vous présente son premier projet: **Tetros** (inspiré du jeu Tetris). Celui-ci a été quasi-exclusivement développé en Python (clé d'accès  au Google Cloud Storage en json).

## Prérequis

Afin de pouvoir tester notre jeu, il vous faudra installer plusieurs librairies Python. Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) afin de les télécharger.

La première librairie est celle qui nous a permis de réaliser l'interface graphique du jeu: [Pygame](https://www.pygame.org/docs/).
```bash
pip install pygame
```

Pour avoir accès au classement en ligne, il vous faudra également télécharger la librairie [Google Cloud Storage](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/notebooks/rendered/cloud-storage-client-library.md)
```bash
pip install google-cloud-storage
```

## Comment jouer
Voici les règles du jeu et les contrôles utilisables (également présent dans le jeu).

![image](https://github.com/NSI-F1-2023-2024/Project-1-TETRIS/blob/main/assets/regles_image.png)

# Fonctionnement du jeu


#quadrillage : Le jeu "tetris" prend en utilise un quadrillage s'adaptant à la résolution de votre écran ainsi toute la surface de jeu est visible par l'utilisateur.

#Rotation bloc : La rotation du bloc en mouvement est un aspect éssentiel de Tetris pour effectuer une rotation appuyer sur la barre espace.

#Descente bloc : Il existe deux manières dans tetris pour qu'un bloc descende , automatiquement pour stimuler le gameplay , le coefficient de la descente auto augmente au cour du temps garrantissant une expérience toujours plus nerveuse.

#Suppression ligne: Pour gagner des points il faut compléter des lignes de la grille avec des blocs. Le jeu Tetris effectue une suppréssion de ligne auto dès lors qu'une ligne est complète.

## Le classement en ligne

Il s'agit de départager les joueurs de notre Tétris et de sauvegarder les scores très bons. Le cloud est (ou était) distribué par Google 

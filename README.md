# TETROS

Le groupe de NSI de F1 vous présente son premier projet: Tetros (inspiré du jeu Tetris). Celui-ci a été quasi-exclusivement développé en Python (clé d'accès  au Google Cloud Storage en json).

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
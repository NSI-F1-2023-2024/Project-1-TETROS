# Tetros

Le groupe de NSI de F1/JASA vous présente son premier projet: **Tetros** (inspiré du jeu Tetris). Celui-ci a été quasi-exclusivement développé en Python, avec [Pygame](https://www.pygame.org/docs/) notamment.


# Prérequis

Pour télécharger le programme: cliquez sur **Code** (en haut de la page à droite, en vert), puis sur **Download ZIP**. Il vous suffit ensuite d'extraire les fichiers du dossier ZIP et vous aurez accès à tout le programme.

<br>

Avant de pouvoir le lancer et tester notre jeu, il vous faudra installer plusieurs librairies Python. Utilisez le gestionnaire de packages [pip](https://pip.pypa.io/en/stable/) afin de les télécharger.

Pour l'interface graphique du jeu: [Pygame](https://www.pygame.org/docs/).
```bash
pip install pygame
```

La librairie [moviepy](https://zulko.github.io/moviepy/), utilisée pour la vidéo d'intro du jeu.
```bash
pip install moviepy
```

Enfin, pour avoir accès au classement en ligne, la librairie [Google Cloud Storage pour Python](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/notebooks/rendered/cloud-storage-client-library.md) (il est également possible de jouer hors-ligne).
```bash
pip install google-cloud-storage
```

# Comment jouer
Voici les règles du jeu et les contrôles utilisables (également présent dans le jeu).

![image](https://github.com/NSI-F1-2023-2024/Project-1-TETRIS/blob/main/assets/menu/regles_image.png)

# Fonctionnement du jeu

## Quadrillage
Le jeu est basé sur un quadrillage, les blocs se déplaçant uniquement au sein de celui-ci. Pour davantage d'accessibilité, ce quadrillage s'adapte à la résolution de votre écran.

Le jeu prend en utilise un quadrillage s'adaptant à la résolution de votre écran ainsi toute la surface de jeu est visible par l'utilisateur.

## Rotation bloc
Vous avez la possibilité de faire tourner le bloc sur lui-même. Nous utilisons un centre de rotation pour permettre à ce bloc de tourner correctement.

## Descente du bloc
Il existe deux manières distinctes pour que le bloc descende: l'une se fait automatiquement et augmente au fur et à mesure que l'on avance dans la partie, et la seconde a lieu uniquement lorsque le joueur le souhaite (la descente est alors grandement accélérée).

## Suppression ligne
Une suppression de ligne est effectuée automatiquement dès lors qu'une ligne de la grille est complète. Cela fait alors gagner des points supplémentaires au joueur.

## Classement en ligne

<b>Les explications données ci-dessous supposent que vous avez installé l'API Google Cloud Storage pour Python (voir prérequis).</b>

Affiché à droite de la grille de jeu, le classement des 10 premiers joueurs vous permet de vous situer par rapport aux autres.

Les données sont stockées au sein d'un fichier [csv](https://fr.wikipedia.org/wiki/Comma-separated_values) (comma separated values), lui-même stocké dans un 'bucket' sur la plateforme [Google Cloud Storage](https://cloud.google.com/storage/docs/introduction?hl=fr).
Grâce à la clé d'accès fournie dans les fichiers du jeu, vous pouvez avoir accès aux données du fichier depuis n'importe quelle machine.

A la fin de chacune de vos parties, si le score réalisé correspond à votre meilleur score, il est enregistré.
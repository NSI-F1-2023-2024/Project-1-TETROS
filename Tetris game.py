import pygame
import sys
from pygame.locals import *
from math import ceil
from random import randint

#Ici se trouve la définition de toutes les listes, valeurs et initialisation par exemple de clock 

clock = pygame.time.Clock()

#Ici, se retrouve toutes les listes utilisés
Lposition_bloc_x=[]  #Voici les listes des position des blocs, et un bloc sera assigné a une valeur
Lposition_bloc_y=[] 
Lcouleur_bloc=[]
Lcouleur_bloc_noir=[10,10,10,10]
Lposition_carre_x=[]
Lposition_carre_y=[]

#Ici, se trouve la grande liste qui contient 10 petites listes de 18 false (car les cases sont vides)
Lposition_cadrillage_x=[]
for i in range(10):
    Lposition_cadrillage_x.append([])
    for j in range(18):
        Lposition_cadrillage_x[i].append(False)

#Ici, se trouve toutes les variables du jeu tetris
nombre_bloc=0   #Déini, le debut du jeu, au début y'a 0 bloc, il faut en créer 1 et comme y'en a 0 bloc le type est 0
doit_cree_bloc=1  #Ici, si marque 1, tout comme normal mais si marque 17, va afficher la liste des blocs
type_bloc=0
position_bloc_descente_x=325  #La, ajoute cette valeur aux positions des blocs en x (aussi pour + tard)
position_bloc_descente_y=25  #La, ajoute cette valeur aux positions des blocs en y mais est pas encore utilisé
bloc_tetris=0
repetition=49

#Ici, aussi les variables mais celles-ci sont utilisés pour le jeu en générale, par exemple si in_game = True, cela veut dire qu'on est en jeu, pareil avec pause et menu
quadrillage = False
in_mort = False
in_menu = True
in_game = False
in_pause = False
esc_pressed = False
run = True


def definition():

    """ def :
    liste :

    Lposition_bloc_x = reference la position x de touts les blocs crées en pixel
    Lposition_bloc_y = reference la position y de touts les blocs crées en pixel
    Lcouleur_bloc = reference la couleur d'un tetros (groupe de 4 bloc) grâce à un chiffre, qui correspond donc à une couleur
    Lposition_carre_x = reference la position en terme de bloc et non de pixel
    Lposition_carre_y = reference la position en terme de bloc et non de pixel
    Lposition_cadrillage_x = la grande liste de 10 liste de 18 elements

    variables :

    liste_bloc_x = permet d'ajouter cette valeur a la position des blocs
    liste_bloc_y = de même mais avec y au lieu de x
    nombre_bloc = permet de savoir combient de bloc sont crées
    doit_cree_bloc = permet de creer x bloc, x etant la valeur de : doit_cree_bloc
    type_bloc = permet de savoir quelle sera le motif de bloc parmis 7 choix
    color = ici va mettre d'abord la couleur du carre de jeu puis du cadrillage
    repetition = sert a colorier une ligne rose tt les 30 pixels, comme ça pas oblige de redessiner le quadrillage à chaque fois
    """
    print("ici")


def couleur_bloc(i):

    """ Ici, la variable permet de prendre un bloc de couleur et de l'importe, donc permet de determiner la couleur
    d'un tetros grâce à la liste Lcouleur_bloc qui va append un chiffre correspondant à une couleur. La variable prend
    en paramètre i, ce qui va permettre la repetition pour x, x etant le nombre de bloc du tetros crée"""

    if Lcouleur_bloc[i]==1:
        image = pygame.image.load("python_tetris/bloc_tetris_vert.jpg")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    elif Lcouleur_bloc[i]==2:
        image = pygame.image.load("python_tetris/bloc_tetris_rouge.JPG")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    elif Lcouleur_bloc[i]==3:
        image = pygame.image.load("python_tetris/bloc_tetris_bleu.JPG")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    elif Lcouleur_bloc[i]==4:
        image = pygame.image.load("python_tetris/bloc_tetris_orange.JPG")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    elif Lcouleur_bloc[i]==5:
        image = pygame.image.load("python_tetris/bloc_tetris_violet.JPG")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    elif Lcouleur_bloc[i]==10:
        image = pygame.image.load("python_tetris/bloc_tetris_noir.jpg")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    else :
        image = pygame.image.load("python_tetris/bloc_tetris_jaune.JPG")
        bloc_tetris = pygame.transform.scale(image, (50, 50))
    return bloc_tetris

def color(x):
    """La permet juste de transformer une couleur en nombre pour la machine et le retourne"""
    ok=False
    while ok==False :
        ok=True
        color=str(input(x))
        if color == "rouge":
            color=(255,0,0)
        elif color == "jaune":
            color=(255,255,0)
        elif color == "vert":
            color=(0,255,0)
        elif color == "bleu":
            color=(0,0,255)
        elif color == "blanc":
            color=(255,255,255)
        elif color == "noir":
            color=(0,0,0)
        elif color == "magenta":
            color=(255,0,255)
        else :
            print("Met une couleur sans majuscule et parmis ce choix : rouge ; vert ; jaune ; bleu ; blanc ; noir ; magenta et reessaie")
            ok=False
    return color



def crea_map(color):
    """Ici, crée la map et donc le quadrillage, pas le noir du fond"""
    for i in range(100,650,50) :
        pygame.draw.line(window  ,color , (i,50),(i,950))
    for u in range (50,1000,50):
        pygame.draw.line(window  , color, (100,u),(600,u))
        pygame.display.flip()


def creation_bloc(nombre_bloc,bloc_tetris):

    """Ici, la def creation_bloc va crée grâce à la commande window.blit un bloc tetris a la position des liste : Lposition_bloc_x et celle y
    .De plus, il repète ce processus nombre_bloc fois. Il prend en paramètre nombre_bloc"""

    for i in range(nombre_bloc):
        bloc_tetris=couleur_bloc(i)
        window.blit(bloc_tetris,[Lposition_bloc_x[i],Lposition_bloc_y[i]])  # Ici, va print cette image a la position x,y

        Lposition_carre_x[i]=(ceil(Lposition_bloc_x[i]/50)-1)
        Lposition_carre_y[i]=(ceil(Lposition_bloc_y[i]/50)-1) #insère dans la liste la position des blocs en terme de bloc pas pixel


def type_bloc_image(doit_cree_bloc,nombre_bloc,type_bloc,position_bloc_descente_x,position_bloc_descente_y):

    """ Ici, type_bloc_image va choisir aléatoirement un type de bloc et va ajouter a la liste Lposition_bloc_x et y les valeurs
    précisent pour cree ce bloc, mais ici on ajoute juste les valeurs a la liste, on ne cree pas les blocs. Elle prend en compte :
    doit_cree_bloc,type_bloc,position_bloc_descente_x"""



    if doit_cree_bloc>=1 and doit_cree_bloc<10:      #Dès que doit_cree_bloc >0, on ajoute et cree un bloc
        type_bloc=randint(1,7)  #pour la creation du bloc aléaotire
        doit_cree_bloc-=1
        couleur_bloc=randint(1,6)
        position_bloc_descente_x=325
        position_bloc_descente_y=75

        for i in range(4):
            Lposition_carre_x.append(0)
            Lcouleur_bloc.append(couleur_bloc)
            Lposition_carre_y.append(0)

    if doit_cree_bloc>=10:
        type_bloc=doit_cree_bloc-10
        doit_cree_bloc-=1

    if type_bloc==1:  #Ici, c'est un bloc 4X1
        Lposition_bloc_x.append(position_bloc_descente_x-75)  #Ici va ajoouter aux liste des valeur et comme ça,
        Lposition_bloc_y.append(position_bloc_descente_y-25)  # le bloc va aller à ces valeurs
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x+75)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4                 # Ici, comme ajoute 4, va collisions 4 blocs
        type_bloc=0

    if type_bloc==2:   # Ici, c'est le bloc 3X1 avec un bloc  en bas a droite
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4
        type_bloc=0

    if type_bloc==3:   # Ici, c'est le bloc 3X1 avec un bloc en bas a gauche
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        nombre_bloc+=4
        type_bloc=0

    if type_bloc==4:   #Ici c'est le carré
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4
        type_bloc=0

    if type_bloc==5:    #Ici c'est le bloc 2 en haut et 2 en bas à gauche
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4
        type_bloc=0

    if type_bloc==6:    #Ici c'est le bloc 2 en haut et 2 en bas à droite
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4
        type_bloc=0

    if type_bloc==7:    #Ici c'est le bloc T
        Lposition_bloc_x.append(position_bloc_descente_x-75)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x+25)
        Lposition_bloc_y.append(position_bloc_descente_y+25)
        Lposition_bloc_x.append(position_bloc_descente_x-25)
        Lposition_bloc_y.append(position_bloc_descente_y-25)
        nombre_bloc+=4
        type_bloc=0
    if doit_cree_bloc>=10:
        position_bloc_descente_x+=150
    return nombre_bloc,doit_cree_bloc,position_bloc_descente_x,position_bloc_descente_y

def faire_tomber_reset(in_mort,nombre_bloc,doit_cree_bloc,repetition,color2,position_bloc_descente_y):
    
    """Ici, permet à chaque itération de faire d'ajouter 1 pixel aux positions y des blocs et si le bloc touche 
    un autre bloc, il est descend plus et va reset, donc mettre True aux positions du bloc puis tout .clear et ajouter
    1 a doit_cree_bloc"""
    
    doit_cree_bloc=doit_cree_bloc

    #Ici, va soit tout reset si bloc touche le bout ou trouve un bloc en dessous, ou alors va ajouter 1 a la position du bloc et donc il va descendre
    if max(Lposition_carre_y)==18   or Lposition_cadrillage_x[Lposition_carre_x[0]-1][Lposition_carre_y[0]+0]==True  or Lposition_cadrillage_x[Lposition_carre_x[1]-1][Lposition_carre_y[1]+0]==True  or Lposition_cadrillage_x[Lposition_carre_x[2]-1][Lposition_carre_y[2]+0]==True  or Lposition_cadrillage_x[Lposition_carre_x[3]-1][Lposition_carre_y[3]+0]==True :

        if repetition==0:   #reset pour la suite
            for i in range (4):

                Lposition_cadrillage_x[Lposition_carre_x[i]-1][Lposition_carre_y[i]-1]=True
            Lposition_bloc_x.clear()
            Lposition_carre_x.clear()
            Lposition_bloc_y.clear()
            Lposition_carre_y.clear()
            Lcouleur_bloc.clear()
            repetition=49
            doit_cree_bloc+=1
            nombre_bloc-=4
            position_bloc_descente_y=25
            crea_map(color2)
        if mort()==True:
            in_mort=True

    else :
        repetition+=1

        for i in range(4):   #Ici, dessine pour effacer l'ancient tetros et garder le fond color1
            pygame.draw.rect(window, (0,0,0), (Lposition_bloc_x[len(Lposition_bloc_y)-1-i]+1, Lposition_bloc_y[len(Lposition_bloc_y)-1-i], 49, 1))
            pygame.draw.rect(window, color2, (Lposition_bloc_x[len(Lposition_bloc_y)-1-i], Lposition_bloc_y[len(Lposition_bloc_y)-1-i], 1, 1))
            Lposition_bloc_y[len(Lposition_bloc_y)-1-i]+=1



            if repetition==50: #Va collisions une ligne de la couleur du cadrillage tout les 50 pixels

                pygame.draw.rect(window, color2, (Lposition_bloc_x[len(Lposition_bloc_y)-1-i]+1, Lposition_bloc_y[len(Lposition_bloc_y)-1-i]-1, 49, 1))
        position_bloc_descente_y+=1
        if repetition == 50 :  #reset
            repetition = 0

    return in_mort,doit_cree_bloc,repetition,nombre_bloc,position_bloc_descente_y

def rotation_bloc(Lposition_bloc_x,Lposition_bloc_y,position_bloc_descente_x,position_bloc_descente_y):
    """Fonction qui permet de faire tourner instantanément un bloc via la touche espace dans
    le sens des aiguilles d'une montre. Il utilise comme centre de rotation position_bloc_descente_x
    et position_bloc_descente_y Dans cette boucle, on subdivise le travail en 13 parties , correspondant
    aux 13 positions possibles des blocs
            []
          [][][]
        [][][][][]
          [][][]
            []
     new_Lposition_bloc_x et new_Lposition_bloc_y serviront à
    acceuillir ces nouvelles valeurs, puis deviendrons les "vraies" Lposition_bloc_. """
    valeurs_vérif_rota_x, valeur_vérif_rota_y = rotation_des_listes( Lposition_carre_x,Lposition_carre_y,position_bloc_descente_x,position_bloc_descente_y)

    if vérif_possibilité_mvt(valeurs_vérif_rota_x, valeur_vérif_rota_y) :
        effacer()

        Lposition_bloc_x,Lposition_bloc_y=rotation_des_listes(Lposition_bloc_x,Lposition_bloc_y,position_bloc_descente_x,position_bloc_descente_y)

    return Lposition_bloc_x, Lposition_bloc_y

def vérif_possibilité_mvt(liste_x,liste_y):

    """Ici, test permet de savoir en retournant True, si le bloque n'en touche pas un autre et renvoi false pour le contraire"""
    if max(Lposition_carre_x)>=10 and  min(Lposition_carre_x)<=10 :
        return False
    if min(Lposition_carre_y)>17:
        return False

    elif Lposition_cadrillage_x[liste_x[0]][liste_y[0]]==False and Lposition_cadrillage_x[liste_x[1]][liste_y[1]]==False and Lposition_cadrillage_x[liste_x[2]][liste_y[2]]==False and Lposition_cadrillage_x[liste_x[3]][liste_y[3]]==False:
        if liste_x[0]%50==0: #Ici, ce teste permet de savoir que le tetros qui tombe est considéré etre sur une seule ligne
            return True #Ici, comme retourne True, cela veut dire que le bloc n'en touche pas un autre et donc qui peut continuer ça route
        elif Lposition_cadrillage_x[liste_x[0]][liste_y[0]+1]==False and Lposition_cadrillage_x[liste_x[1]][liste_y[1]+1]==False and Lposition_cadrillage_x[liste_x[2]][liste_y[2]+1]==False and Lposition_cadrillage_x[liste_x[3]][liste_y[3]+1]==False:
            return True
    else :
        return False #Cela veut dire que le bloc en touhe un autre et donc qu'il ne peut pas être ou rester la et qu'il doit revenir à son ancienne position


def rotation_des_listes(liste_x,liste_y,position_bloc_descente_x,position_bloc_descente_y):
#création des variables
    new_liste_x=[]
    new_liste_y=[]

    for i in range (len(liste_x)):
        x=liste_x[i] - position_bloc_descente_x
        y=round((liste_y[i] - position_bloc_descente_y)/5)
        y=y*5
        print(x,y)
        if x==-125:
            new_liste_x.append(position_bloc_descente_x-25)
            new_liste_y.append(position_bloc_descente_y+125)
        if y==125:
            new_liste_x.append(position_bloc_descente_x+75)
            new_liste_y.append(position_bloc_descente_y+25)
        if x==75:
            new_liste_x.append(position_bloc_descente_x-25)
            new_liste_y.append(position_bloc_descente_y-75)
        if y==-75:
            new_liste_x.append(position_bloc_descente_x-125)
            new_liste_y.append(position_bloc_descente_y+25)

        if x==-75:
            if y==75:
                new_liste_x.append(position_bloc_descente_x+25)
                new_liste_y.append(position_bloc_descente_y+75)
            if y==25:
                new_liste_x.append(position_bloc_descente_x-25)
                new_liste_y.append(position_bloc_descente_y+75)
            if y==-25:
                new_liste_x.append(position_bloc_descente_x-75)
                new_liste_y.append(position_bloc_descente_y+75)
            if y ==-75:
                new_liste_x.append(position_bloc_descente_x+125)
                new_liste_y.append(position_bloc_descente_y+75)

        if x==-25:
            if y==-75:
                new_liste_x.append(position_bloc_descente_x+25)
                new_liste_y.append(position_bloc_descente_y+25)
            if y==25:
                new_liste_x.append(position_bloc_descente_x-25)
                new_liste_y.append(position_bloc_descente_y+25)
            if y==-25:
                new_liste_x.append(position_bloc_descente_x-75)
                new_liste_y.append(position_bloc_descente_y+25)
            if y == 75 :
                new_liste_x.append(position_bloc_descente_x+25)
                new_liste_y.append(position_bloc_descente_y+25)

        if x==25:
            if y==75:
                new_liste_x.append(position_bloc_descente_x+25)
                new_liste_y.append(position_bloc_descente_y-25)
            if y==25:
                new_liste_x.append(position_bloc_descente_x-25)
                new_liste_y.append(position_bloc_descente_y-25)
            if y==-25:
                new_liste_x.append(position_bloc_descente_x-75)
                new_liste_y.append(position_bloc_descente_y-25)
    #transfer des nouvelles valeurs:
    for i in range(len(new_liste_x)):
        liste_x[i]=new_liste_x[i]
        liste_y[i]=new_liste_y[i]
    return liste_x,liste_y


def mort():
    if len(Lposition_carre_y)>0:
        if max(Lposition_carre_y)<=1:
            return True
    else:
        return False
    
def jeu(doit_cree_bloc,nombre_bloc,type_bloc,position_bloc_descente_x,bloc_tetris,position_bloc_descente_y,Lposition_bloc_x,Lposition_bloc_y):

    """ def, de base permet de lancer le jeu avec la creation des blocs et de la map"""


    nombre_bloc,doit_cree_bloc,position_bloc_descente_x,position_bloc_descente_y=type_bloc_image(doit_cree_bloc,nombre_bloc,type_bloc,position_bloc_descente_x,position_bloc_descente_y)
    bloc_tetris=creation_bloc(nombre_bloc,bloc_tetris)

    return nombre_bloc,doit_cree_bloc,position_bloc_descente_x,Lposition_bloc_x,Lposition_bloc_y

def effacer():   
    
    """Ici, cette def permet d'effacer un bloc en dessinant par dessus des blocs noirs et elle est utilisé lorsque on deplace le bloc ou le tourne"""
   
    for i in range(4):    #Ici, va collisions le bloc en noir pour l'effacer
        Lcouleur_bloc_noir[i]=Lcouleur_bloc[i]
        Lcouleur_bloc[i]=10     
    creation_bloc(nombre_bloc,bloc_tetris)
    for i in range(4):
        Lcouleur_bloc[i]=Lcouleur_bloc_noir[i]
        Lcouleur_bloc_noir[i]=10
    
    crea_map(color2)


class Button():
    """Définit les caractéristiques des boutons utilisés dans le jeu."""
    def __init__(self, x: int, y: int, image):
        """Initialisation des variables nécessaires pour tout bouton: 
        position (x,y), image, rectangle pygame(utile pour les collisions) 
        et le statut du bouton(cliqué ou non cliqué)"""
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        
    def collision(self, fenetre):
        """Dessine le bouton dans la fenetre du jeu, et vérifie s'il y a une 
        intéraction avec celui-ci. 
        Retourne True si le bouton est cliqué, sinon retourne False."""
        action = False
        fenetre.blit(self.image, (self.rect.x, self.rect.y))
        position_souris = pygame.mouse.get_pos()
        if self.rect.collidepoint(position_souris):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        return action
    
def effacer_la_ligne ():
    for i in range (len(Lposition_cadrillage_x)):
        if Lposition_cadrillage_x[i]==true:
            Lposition_cadrillage_x[i]==false
            for i in range (i-1):
                Lposition_cadrillage_x[i]=Lposition_cadrillage_x[i-1][:]
            Lposition_cadrillage_x[0]==false
            
def touche(in_game,position_bloc_descente_x,Lposition_bloc_x,Lposition_bloc_y):
    
    """Ici, va détecter la pression d'un touche droite, gauche, quit et espace et a en consequence decaler le tetros, quitter la page 
    ou meme le faire tourner(ça marche pas encore), et il y a un beug malheuresement ou à la 1er descente du bloc, on peut pas le déplacer à gauche"""
    
  
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and in_game == True: # Si la toche droite est appuyée alors ajoute 50 au positions = 1 bloc vers la droite
            if len(Lposition_carre_x)>0:    
                if max(Lposition_carre_x)<10:
                    effacer()
                    position_bloc_descente_x+=50
                    for i in range(4):
                        Lposition_bloc_x[len(Lposition_bloc_x)-1-i]+=50 
          
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and in_game == True: # Si la toche gauche est appuyée alors ajoute -50 au positions = 1 bloc vers la gauche
            if len(Lposition_carre_x)>0: 
                if min(Lposition_carre_x)>1:
                    effacer()
                    position_bloc_descente_x-=50
                    for i in range(4):
                        Lposition_bloc_x[len(Lposition_bloc_x)-1-i]-=50 
    
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and in_game==True:
            Lposition_bloc_x,Lposition_bloc_y=rotation_bloc(Lposition_bloc_x,Lposition_bloc_y,position_bloc_descente_x,position_bloc_descente_y)

        elif event.type == pygame.QUIT:  #Pour quitter mais jsp pourquoi ça marche pas, julian si tu sais pk,
            sys.exit()

    return position_bloc_descente_x,Lposition_bloc_x, Lposition_bloc_y
            
def jeu_global(Lposition_bloc_x,quadrillage,in_mort,in_game,in_pause,esc_pressed,in_menu,type_bloc,position_bloc_descente_x,bloc_tetris,Lposition_bloc_y,doit_cree_bloc,repetition,color2,nombre_bloc,position_bloc_descente_y):
   
    """Ici ce réalise tout le jeu. Celui-ci est divisé en 3 parties : 
            - Le in_menu : c'est la moment du début du jeu ou on attend juste que tu appuie sur play pour joeur et rien d'autre ne se passe
            - le in_game : C'est le moment ou le jeu est en cours, il se passe dans cette ordre : 
                                1) le jeu : d'abord si il y a aucun bloc,ou un qui est deja tombe, il cree un nouveau bloc avec de
                                    nouvelles valeurs et couleur et donc réinitialiser les liste de positions et de couleur
                                2) Va a chaque position des liste Lposition_bloc_x et Lposition_bloc_y et va print un bloc avec du noir au dessus pour effacer l'ancien et de couleur Lcouleur_bloc
                            Ensuite, on a terminé le jeu et on va faire : tomber_reset ( avec 2 cas) :
                                1) soit ajoute 1 a chaques valeurs de Lposition_bloc_y pour après , quand va print les tetros, vales print 1 pixel plus bas et va symboliser la descente 
                                2) Ou alors va, si le bloc entrain de descendre touche un autre bloc, va reinitialiser toutes les valeurs et ajouter 1 à la variable doit_cree_bloc pour que a la boucle
                                    suivante, dans type_bloc_image, ajoute des valeurs au listes des positions et donc ensuite print un nouveau tetros
                            Enfin, va regarder si on appuie sur la touche echap pour mettre en pause le jeu.
            - le in_pause : C'est le moment qui s'active si on appuie sur echap et ce desactive si on réappuie sur pause :
                                1) Ici, il ne ce passe rien a par la detection de la touche.
            Enfin, en plus il y a le def touche(). Ici, va detecter tout ce qui est touche autre que la touche echap.:
                1) La touche droite pour décaler tout les blocs vers a droite
                2) la touche gauche pour décaler tout les blocs vers la gauche
                3) la touche espace, pour faire la rotation
                4) la touche fleche vers le bas pour accelerer la descente du bloc ( en cours)
                5) la croix en haut a droite pour arrêter le programme
        + tetros c'est un tetris de 4 blocs genre le t, 3 en haut et 1 en bas"""
 
    in_menu=in_menu #ici c'est pour le return de fin, si je mets pas ça le programme beug pcq techniquement les valeurs ne sont pas touchés et donc il peut pas les return
    in_game=in_game
    in_pause=in_pause
    esc_pressed=esc_pressed
    quadrillage=quadrillage
    position_bloc_descente_x=position_bloc_descente_x
    
    if in_mort:
        in_menu=False
        in_game=False
        in_pause=False
        
    if in_menu:  #Dans menu, juste en attente de l'appuie du bouton jouer
        window.blit(menu_img, (0,0))
        if bouton_jouer.collision(window):
            in_menu = False
            in_game = True

    elif in_game:    #En game, le jeu tetris est lancé avec donc le programme
        if not quadrillage:
            fond_ecran_jeu = pygame.image.load("python_tetris/fond_ecran_jeu.png")
            fond_ecran_jeu=pygame.transform.rotate(fond_ecran_jeu,90)
            fond_ecran_jeu = pygame.transform.scale(fond_ecran_jeu, (700,1100 ))
            window.blit(fond_ecran_jeu,[0,0])
            pygame.draw.rect(window, (0,0,0), pygame.Rect(100,50, 500, 900))  # ici cree le rectangle pour le jeu
            crea_map(color2)
            quadrillage = True

        nombre_bloc,doit_cree_bloc,position_bloc_descente_x,Lposition_bloc_x,Lposition_bloc_y=jeu(doit_cree_bloc,nombre_bloc,type_bloc,position_bloc_descente_x,bloc_tetris,position_bloc_descente_y,Lposition_bloc_x,Lposition_bloc_y)
        in_mort,doit_cree_bloc,repetition,nombre_bloc,position_bloc_descente_y=faire_tomber_reset(in_mort,nombre_bloc,doit_cree_bloc,repetition,color2,position_bloc_descente_y)
        
        if pygame.key.get_pressed()[K_ESCAPE] and esc_pressed == False:
            in_game = False
            in_pause = True
            esc_pressed = True
        if not pygame.key.get_pressed()[K_ESCAPE]:
            esc_pressed = False

            
    elif in_pause:    #Le jeu est en pause si on appiue sur echap et le programme ne passera donc plus que part in_pause et plus par in_game
        if pygame.key.get_pressed()[K_ESCAPE] and esc_pressed == False: 
            in_game = True
            in_pause = False
            esc_pressed = True
        if not pygame.key.get_pressed()[K_ESCAPE]:
            esc_pressed = False

    position_bloc_descente_x,Lposition_bloc_x, Lposition_bloc_y=touche(in_game,position_bloc_descente_x,Lposition_bloc_x,Lposition_bloc_y) # Ici va voir si une touche est appuyé

    return in_mort,in_game,in_pause,esc_pressed,in_menu,quadrillage,Lposition_bloc_y,Lposition_bloc_x,repetition,position_bloc_descente_y,position_bloc_descente_x,nombre_bloc,doit_cree_bloc
            


color2=color("Tu veux quelle couleur pour les lignes ?")
pygame.init()   #Début dela création de la page
window = pygame.display.set_mode((700,1000))  #crée le rectangle noir de 700 par 1000

#Ici se trouve la définition des images notament pour le fond d'ecran
menu_img = pygame.image.load("python_tetris/menu_image.png")
bouton_jouer_img = pygame.image.load("python_tetris/bouton_jouer.png")
bouton_jouer = Button(200, 200, bouton_jouer_img)

while run:
    
    in_mort,in_game,in_pause,esc_pressed,in_menu,quadrillage,Lposition_bloc_y,Lposition_bloc_x,repetition,position_bloc_descente_y,position_bloc_descente_x,nombre_bloc,doit_cree_bloc=jeu_global(Lposition_bloc_x,quadrillage,in_mort,in_game,in_pause,esc_pressed,in_menu,type_bloc,position_bloc_descente_x,bloc_tetris,Lposition_bloc_y,doit_cree_bloc,repetition,color2,nombre_bloc,position_bloc_descente_y) #réalise le jeu en entier
    pygame.display.update()  # update l'écran je crois, donc réinitialise les pixels je crois, affiche quoi

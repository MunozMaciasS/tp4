#Crée par Samuel Munoz Mars 2023
#but: Faire en sorte d’afficher 20 cercles de couleur différente à des positions aléatoires dans la fenêtre(sans toucher les coins)

import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
         arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY, arcade.color.AERO_BLUE,arcade.color.BITTERSWEET_SHIMMER]

class Cercle(): # on defnine un cercle par son rayon, son centre dans les axes de x et y, sa couleur, et son mouvement(dans es 2 axes)
   def __init__(self,rayon,center_x,center_y,color,change_x,change_y):
       self.rayon = rayon
       self.center_x = center_x
       self.center_y = center_y
       self.color = color
       self.change_x = change_x
       self.change_y = change_y


   def draw(self): #on dessine le cercle dans la fenetre
       arcade.draw_circle_filled(self.center_x,self.center_y,self.rayon,self.color)
       pass

   def mouvement(self): #pour changer la direction du mouvement d'un onject, il faur multiplier cette variable par -1
       self.center_x += self.change_x
       self.center_y += self.change_y

       if self.center_x + self.rayon > SCREEN_WIDTH:
           self.change_x *= -1
       if self.center_x - self.rayon < 0:
           self.change_x *= -1
       if self.center_y + self.rayon > SCREEN_HEIGHT:
           self.change_y *= -1
       if self.center_y - self.rayon < 0:
           self.change_y *= -1

class Rectangle():#on definie un rectangle par sa base et sa hauteur,son angle par rapport le cadre son centre dans les axes de x et y, sa couleur, et son mouvement(dans es 2 axes)
    def __init__(self,base,heigth,center_x,center_y,color,change_x,change_y,angle):
        self.base = base
        self.heigth = heigth
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.change_x = change_x
        self.change_y = change_y
        self.angle = angle

    def draw(self): 
       arcade.draw_rectangle_filled(self.center_x,self.center_y,self.base,self.heigth,self.color,self.angle)
       pass

    def mouvement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x + (self.base / 2) > SCREEN_WIDTH:
            self.change_x *= -1
        if self.center_x - (self.base / 2) < 0:
            self.change_x *= -1
        if self.center_y + (self.heigth / 2) > SCREEN_HEIGHT:
            self.change_y *= -1
        if self.center_y - (self.heigth / 2) < 0:
            self.change_y *= -1



class MyGame(arcade.Window): #cette clase sert a definir la fenetre dont tout les action se deroules
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
       self.liste_cercles = [] #on cree une liste pour les cercles
       self.liste_rectangles = [] #et ine autres pour les rectangles


   def setup(self):
       # remplir la liste avec 20 objets de type Cercle, avec leur respectives variables
       for _ in range(20): #on crée tout les variables des cercles et rectnagles pour apres les append à leur liste respectives
           rayon = random.randint(10,30)
           center_x = random.randint(0 + rayon, SCREEN_WIDTH - rayon)
           center_y = random.randint(0 + rayon, SCREEN_HEIGHT - rayon)
           color = random.choice(COLORS)
           change_x = random.randint(-10,10)
           change_y = random.randint(-10,10)
           self.liste_cercles.append(Cercle(rayon,center_x,center_y,color, change_x, change_y)) #on appelle le contrustor et on append l'object crée
       for _ in range(20):
         #  remplir la liste avec 20 objets de type Cercle, avec leur respectives variables
           base = random.randint(10, 30)
           heigth = random.randint(10, 30)
           center_x = random.randint(0 + base, SCREEN_WIDTH - base)
           center_y = random.randint(0 + heigth, SCREEN_HEIGHT - heigth)
           color = random.choice(COLORS)
           change_x = random.randint(-10, 10)
           change_y = random.randint(-10, 10)
           angle = random.randint(0,180)
           self.liste_rectangles.append(Rectangle(base,heigth, center_x, center_y, color, change_x, change_y,angle))

   def on_draw(self): #on draw les objects dans l'ecran
       arcade.start_render()

       for cercle in self.liste_cercles:
           cercle.draw()
       for rectangle in self.liste_rectangles:
           rectangle.draw()


   def on_update(self, delta_time: float): #à chauque frame, on update la posuition des cercles et rectangles
       for cercle in self.liste_cercles:
           cercle.mouvement()
       for rectangle in self.liste_rectangles:
           rectangle.mouvement()

   def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
#
       if button == arcade.MOUSE_BUTTON_LEFT: #lorseque on clique la partie gauche du mouse,on append un cercle(avec ses proprietes) dans la position du click
           rayon = random.randint(10, 30)
           center_x = x
           center_y =y
           color = random.choice(COLORS)
           change_x = random.randint(-10, 10)
           change_y = random.randint(-10, 10)
           self.liste_cercles.append(Cercle(rayon, center_x, center_y, color, change_x, change_y))
       elif button == arcade.MOUSE_BUTTON_RIGHT: #lorseque on clique la partie droit du mouse,on append un rectangle(avec ses proprietes) dans la position du click
           base = random.randint(10, 30)
           heigth = random.randint(10, 30)
           center_x = x
           center_y = y
           color = random.choice(COLORS)
           change_x = random.randint(-10, 10)
           change_y = random.randint(-10, 10)
           angle = random.randint(0, 180)
           self.liste_rectangles.append(Rectangle(base, heigth, center_x, center_y, color, change_x, change_y, angle))








def main(): #on run la fenetre
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()

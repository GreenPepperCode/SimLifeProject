# environment.py
import pygame

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Définir la zone de nourriture et la zone de danger
        self.food_zone = pygame.Rect(100, 100, 200, 200)
        self.danger_zone = pygame.Rect(500, 400, 150, 150)

    def draw(self, screen):
        # Dessiner les zones de l'environnement sur l'écran
        green_color = (0, 255, 0)  # Couleur verte pour la zone de nourriture
        red_color = (255, 0, 0)    # Couleur rouge pour la zone de danger
        pygame.draw.rect(screen, green_color, self.food_zone)
        pygame.draw.rect(screen, red_color, self.danger_zone)

    def is_food_nearby(self, x, y):
        # Vérifier si la position (x, y) est proche de la zone de nourriture
        return self.food_zone.collidepoint(x, y)

    def is_carnivore_nearby(self, creature, carnivores):
        # Vérifier si un carnivore est proche de la créature
        for carnivore in carnivores:
            distance = ((creature.x - carnivore.x) ** 2 + (creature.y - carnivore.y) ** 2) ** 0.5
            if distance < 50:  # Distance seuil pour définir "proche"
                return True
        return False


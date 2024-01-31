# creature.py
import random
import pygame

class Creature:
    def __init__(self, x, y, color, gender, speed, strength, resistance):
        self.x = x
        self.y = y
        self.color = color
        self.gender = gender
        self.speed = speed
        self.strength = strength
        self.resistance = resistance
        self.age = 0
        self.lifespan = random.randint(50, 100)
        self.health = 100

    def draw(self, screen):
        # Méthode pour dessiner la créature sur l'écran
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

    def update(self):
        # Mettre à jour l'âge et la santé de la créature
        self.age += 1
        self.health -= 1
        if self.health <= 0 or self.age >= self.lifespan:
            return 'dead'
        return 'alive'

    def move_towards_food(self, food_zone):
        # Se déplacer vers le centre de la zone de nourriture
        food_center_x, food_center_y = food_zone.center
        self.x += (food_center_x - self.x) * 0.05 * self.speed
        self.y += (food_center_y - self.y) * 0.05 * self.speed

    def flee_from_danger(self, danger_zone, carnivores):
        # S'éloigner des carnivores et de la zone de danger
        for carnivore in carnivores:
            if abs(carnivore.x - self.x) < 50 and abs(carnivore.y - self.y) < 50:
                self.x -= (carnivore.x - self.x) * 0.1 * self.speed
                self.y -= (carnivore.y - self.y) * 0.1 * self.speed
        if danger_zone.collidepoint(self.x, self.y):
            danger_center_x, danger_center_y = danger_zone.center
            self.x -= (danger_center_x - self.x) * 0.1 * self.speed
            self.y -= (danger_center_y - self.y) * 0.1 * self.speed

    def chase_prey(self, herbivores):
        # Suivre l'herbivore le plus proche
        closest_prey = None
        closest_distance = float('inf')
        for herbivore in herbivores:
            distance = ((herbivore.x - self.x) ** 2 + (herbivore.y - self.y) ** 2) ** 0.5
            if distance < closest_distance:
                closest_distance = distance
                closest_prey = herbivore
        if closest_prey:
            self.x += (closest_prey.x - self.x) * 0.05 * self.speed
            self.y += (closest_prey.y - self.y) * 0.05 * self.speed

def reproduce(creature1, creature2):
    if creature1.gender != creature2.gender and creature1.age > 20 and creature2.age > 20:
        x, y = (creature1.x + creature2.x) // 2, (creature1.y + creature2.y) // 2
        color = random.choice([creature1.color, creature2.color])
        gender = random.choice(['male', 'female'])
        speed = (creature1.speed + creature2.speed) / 2
        strength = (creature1.strength + creature2.strength) / 2
        resistance = (creature1.resistance + creature2.resistance) / 2
        offspring = Creature(x, y, color, gender, speed, strength, resistance)
        return offspring
    return None

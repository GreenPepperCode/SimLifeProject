# simulation.py
import pygame
from creature import Creature, reproduce
from environment import Environment

def main():
    pygame.init()

    # Configuration de la fenêtre
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulation de Créatures")

    # Initialisation de l'environnement
    environment = Environment(width, height)

    # Création des créatures
    herbivores = [Creature(300, 300, (0, 255, 0), 'male', 5, 5, 5), 
                  Creature(350, 300, (0, 0, 255), 'female', 5, 5, 5)]
    carnivores = [Creature(400, 400, (255, 0, 0), 'male', 7, 7, 7), 
                  Creature(450, 450, (255, 0, 0), 'female', 7, 7, 7)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Mise à jour des créatures
        new_creatures = []
        for creature in herbivores + carnivores:
            status = creature.update()
            if status == 'dead':
                if creature in herbivores: herbivores.remove(creature)
                elif creature in carnivores: carnivores.remove(creature)
            else:
                for other_creature in herbivores:
                    offspring = reproduce(creature, other_creature)
                    if offspring:
                        new_creatures.append(offspring)

        herbivores.extend(new_creatures)

        # Affichage
        screen.fill((0, 0, 0))
        environment.draw(screen)
        for creature in herbivores + carnivores:
            creature.draw(screen)

        pygame.display.flip()
        pygame.time.delay(250)

    pygame.quit()

if __name__ == "__main__":
    main()

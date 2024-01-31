# utils.py
def calculate_distance(x1, y1, x2, y2):
    """Calcule la distance euclidienne entre deux points."""
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def random_position(width, height):
    """Génère une position aléatoire dans les limites données."""
    import random
    return random.randint(0, width), random.randint(0, height)

def is_within_bounds(x, y, width, height):
    """Vérifie si une position (x, y) se trouve à l'intérieur des limites définies."""
    return 0 <= x <= width and 0 <= y <= height

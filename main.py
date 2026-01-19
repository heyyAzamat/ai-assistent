import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size() #constants
IMAGE_FOLDER = "emotions"
images = [
    os.path.join(IMAGE_FOLDER, file)
    for file in os.listdir(IMAGE_FOLDER)
    if file.lower().endswith((".png", ".jpg", "jpeg"))
]

if not images:
    pygame.quit()
    sys.exit()

current_index = 0

def load_image(index):
    image = pygame.image.load(images[index])
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return image 

current_image = load_image(current_index)

clock = pygame.time.Clock()
clock.tick(60)

while running:
    for event in pygame.event.get():
        if event.key == pygame.K_ESCAPE:
            running = False 
            current_index = (current_index + 1) % len(images)
            screen_blit(current_image, (0, 0))
            pygame.display.flip()
            pygame.quit()
            sys.exit()
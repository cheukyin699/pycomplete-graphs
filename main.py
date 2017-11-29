import pygame
import math
import sys

if len(sys.argv) < 2:
    print("Invalid arguments; exiting")
    print("Note: %s <number_of_vertices>" % sys.argv[0])
    sys.exit(-1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

VERTICES = int(sys.argv[1])
ALPHA = 2 * math.pi / VERTICES
WIDTH, HEIGHT = 700, 700
RADIUS = WIDTH // 2
# Generate the vertices
vs = [(int(RADIUS * math.cos(i * ALPHA) + RADIUS),
       int(-RADIUS * math.sin(i * ALPHA) + RADIUS))
      for i in range(VERTICES)]

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Complete Graphs')

running = True
drawn = False

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

    if not drawn:
        screen.fill(BLACK)
        for i in range(len(vs)):
            for j in range(len(vs)):
                if i == j:
                    continue
                pygame.draw.line(screen, WHITE, vs[i], vs[j])
            pygame.draw.circle(screen, WHITE, vs[i], 5)
        drawn = True
        pygame.display.flip()

pygame.quit()

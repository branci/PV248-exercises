# PV248 Python, Group 2
# Part 8 - Animations with Pygame
# Branislav Smik
# 25.11.2017
#
#
# bubbles animation

import pygame
from pygame import display, draw, time, event, Color
from random import randint

BUBBLE_BLUE = [51, 153, 255]
X_MAX = 800
Y_MAX = 600

def main():
    screen = display.set_mode([X_MAX, Y_MAX])
    bubbles = []
    clock = time.Clock()

    while True:
        screen.fill([0, 0, 0])

        for bubble in bubbles.copy():
            draw.circle(screen, BUBBLE_BLUE, bubble.center, bubble.radius, 1)
            bubble.radius += 1
            if bubble.radius > X_MAX-700:
                bubbles.remove(bubble)
        bubbles.append(Bubble())
        display.flip()
        clock.tick(60)
        if event.poll().type == pygame.KEYDOWN:
            break

class Bubble:
    def __init__(self):
        self.center = [randint(0, X_MAX), randint(0, Y_MAX)]
        self.radius = 1

if __name__ == "__main__":
    main()
#!/usr/bin/env python
"""demonstrate pycairo and pygame"""


import math
import sys

import cairo
import pygame


def draw_white(surface,x, y, width=60, height=60):
   # x, y, width, height = (50, 50, 100, 100)
    ctx = cairo.Context(surface)
    #ctx.set_line_width(5)
    ctx.rectangle(x, y, width, height)
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

def draw_black(surface, x, y, width=60, height=60):
   # x, y, width, height = (150, 50, 100, 100)
    ctx = cairo.Context(surface)
    #ctx.set_line_width(0)
    ctx.rectangle(x, y, width, height)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()
    


def board(surface):

    square_size = 60

    for i in range(8):  # 8 rows
        for j in range(8):  # 8 columns
            x_position = i * square_size  + 100
            y_position = j * square_size  + 250
            
            if (i + j) % 2 == 0:
                draw_black(surface, x_position, y_position)  # Black square
            else:
                draw_white(surface, x_position, y_position)  # White square


       

  

def main():
    width, height = 812, 812
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)

    pygame.init()
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(0, 0, 0.1)  # Dark blue background
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

    #draw_white(surface, 50, 50)
    board(surface)
    # Create PyGame surface from Cairo Surface
    buf = surface.get_data()
    image = pygame.image.frombuffer(buf, (width, height), "ARGB")
    # Tranfer to Screen
    screen.blit(image, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Optionally, add a delay to reduce CPU usage
        pygame.time.delay(10)


if __name__ == "__main__":
    main()
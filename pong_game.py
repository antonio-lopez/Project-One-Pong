import pygame
import sys
import random
from pygame.locals import *

windowHeight = 500
windowWidth = 700
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 200, 0)
white = (255, 255, 255)


class ScoreBoard:
    def updatescore(self, computer_win, computer_score, player_score, player_win):
        font = pygame.font.Font(None, 74)
        text = font.render(str(computer_win), 1, white)
        gameDisplay.blit(text, (250, 10))
        text = font.render(str(computer_score), 1, white)
        gameDisplay.blit(text, (250, 50))
        text = font.render(str(player_win), 1, white)
        gameDisplay.blit(text, (420, 10))
        text = font.render(str(player_score), 1, white)
        gameDisplay.blit(text, (420, 50))


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, w):
        super().__init__()
        self.color = color
        self.width = w

        self.image = pygame.Surface([w, w])
        self.image.fill(white)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, color, [0, 0, w, w])
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]       # x, y

    # set up random ball velocity
    def update(self):
        self.rect.x += self.velocity[0]     # ball x coordinate
        self.rect.y += self.velocity[1]     # ball y coordinate

        collision = pygame.sprite.spritecollideany(ball, spritelist)
        if collision:
            if collision == player_y_pad:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                # game sound will go here
            if collision == player_x_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                # game sound will go here
            if collision == player_x2_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                # game sound will go here
            if collision == comp_y_pad:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                # game sound will go here
            if collision == comp_x_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                # game sound will go here
            if collision == comp_x2_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                # game sound will go here


class XPaddle(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    # move paddles left and right and keep them in player area
    def move_left(self, pix):
        self.rect.x -= pix
        if self.rect.x < 350:
            self.rect.x = 350

    def move_right(self, pix):
        self.rect.x += pix
        # off screen detection
        if self.rect.x > 600:
            self.rect.x = 600


class CompXPaddle(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    # move paddles left and right and keep them in computer area
    def move_left(self, pix):
        self.rect.x -= pix
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self, pix):
        self.rect.x += pix
        if self.rect.x > 250:
            self.rect.x = 250


class YPaddle(pygame.sprite.Sprite):
    def __index__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(white)
        self.image.set_colorkey(white)

        pygame.draw.rect(self.image, color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    def move_up(self, pix):
        self.rect.y -= pix
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pix):
        self.rect.y += pix
        if self.rect.y > 400:
            self.rect.y = 400


pygame.init()

player_score = 0
players_win = 0
comp_score = 0
comp_win = 0

gameDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pong')


import pygame
import random
import sys
from pygame.locals import *

HEIGHT = 500
WIDTH = 700
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Ball(pygame.sprite.Sprite):

    def __init__(self, ball_color, w):
        super().__init__()
        self.color = ball_color
        self.width = w

        self.image = pygame.Surface([w, w])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.ellipse(self.image, ball_color, [0, 0, w, w])
        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]   # x, y

    # set up random ball velocity
    def update(self):
        self.rect.x += self.velocity[0]     # ball x coordinate
        self.rect.y += self.velocity[1]     # ball y coordinate

        collision = pygame.sprite.spritecollideany(ball, sprites)
        if collision:
            if collision == player_x_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)
            if collision == player_x2_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)
            if collision == player_y_pad:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)
            if collision == comp_x_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)
            if collision == comp_x2_pad:
                self.velocity[0] = random.randint(-8, 8)
                self.velocity[1] = -self.velocity[1]
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)
            if collision == comp_y_pad:
                self.velocity[0] = -self.velocity[0]
                self.velocity[1] = random.randint(-8, 8)
                pygame.mixer.music.load('pong_blip.wav')
                pygame.mixer.music.play(0)


class XPaddle(pygame.sprite.Sprite):

    def __init__(self, x_pad_color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, x_pad_color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    # move paddles left and right and keep them in player area
    def move_left(self, pix):
        self.rect.x -= pix
        if self.rect.x < 350:
            self.rect.x = 350

    def move_right(self, pix):
        self.rect.x += pix
        if self.rect.x > 600:
            self.rect.x = 600


class CompXPaddle(pygame.sprite.Sprite):

    def __init__(self, comp_x_pad_color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, comp_x_pad_color, [0, 0, w, h])
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

    def __init__(self, y_pad_color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, y_pad_color, [0, 0, w, h])
        self.rect = self.image.get_rect()

    # move paddles up and down and keep them in the border
    def move_up(self, pix):
        self.rect.y -= pix
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pix):
        self.rect.y += pix
        if self.rect.y > 400:
            self.rect.y = 400


def score_update(comp_point, player_point, comp_update, player_update):
    text_font = pygame.font.Font(None, 50)
    score_text = text_font.render(str(comp_point), 1, WHITE)
    gameDisplay.blit(score_text, (220, 10))
    score_text = text_font.render(str("/11"), 1, WHITE)
    gameDisplay.blit(score_text, (280, 10))

    score_text = text_font.render(str(player_point), 1, WHITE)
    gameDisplay.blit(score_text, (380, 10))
    score_text = text_font.render(str("/11"), 1, WHITE)
    gameDisplay.blit(score_text, (450, 10))

    score_text = text_font.render(str(comp_update), 1, WHITE)
    gameDisplay.blit(score_text, (250, 50))
    score_text = text_font.render(str("/3"), 1, WHITE)
    gameDisplay.blit(score_text, (280, 50))
    score_text = text_font.render(str(player_update), 1, WHITE)
    gameDisplay.blit(score_text, (420, 50))
    score_text = text_font.render(str("/3"), 1, WHITE)
    gameDisplay.blit(score_text, (450, 50))


class Scoreboard:
    pass


pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG Game')
score = Scoreboard()
clock = pygame.time.Clock()
player_score = 0
comp_score = 0
player_win = 0
comp_win = 0
total_wins = 0
game_limit = 5
end_game = 0

# set up paddles with image backgrounds
y_paddle_img = pygame.image.load("y_paddle_image.png")
x_paddle_img = pygame.image.load("x_paddle_image.png")
ball_image = pygame.image.load("pong_ball.png")
sprites = pygame.sprite.Group()

# set up player paddles
player_x_pad = XPaddle(BLACK, 100, 10)
player_x_pad.rect.x = 600
player_x_pad.rect.y = 10
player_x_pad.image = x_paddle_img
sprites.add(player_x_pad)

player_x2_pad = XPaddle(BLACK, 100, 10)
player_x2_pad.rect.x = 600
player_x2_pad.rect.y = 480
player_x2_pad.image = x_paddle_img
sprites.add(player_x2_pad)

player_y_pad = YPaddle(BLACK, 10, 100)
player_y_pad.rect.x = 680
player_y_pad.rect.y = 200
player_y_pad.image = y_paddle_img
sprites.add(player_y_pad)

# set up computer paddles
comp_x_pad = CompXPaddle(BLACK, 100, 10)
comp_x_pad.rect.x = 20
comp_x_pad.rect.y = 10
comp_x_pad.image = x_paddle_img
sprites.add(comp_x_pad)

comp_x2_pad = CompXPaddle(BLACK, 100, 10)
comp_x2_pad.rect.x = 20
comp_x2_pad.rect.y = 480
comp_x2_pad.image = x_paddle_img
sprites.add(comp_x2_pad)

comp_y_pad = YPaddle(BLACK, 10, 100)
comp_y_pad.rect.x = 10
comp_y_pad.rect.y = 200
comp_y_pad.image = y_paddle_img
sprites.add(comp_y_pad)

# set up ball
ball = Ball(BLACK, 20)
ball.rect.x = 345
ball.rect.y = 195
ball.image = ball_image
sprites.add(ball)


while True:
    keys = pygame.key.get_pressed()
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # player movements
    if keys[pygame.K_UP]:
        player_y_pad.move_up(5)
    if keys[pygame.K_DOWN]:
        player_y_pad.move_down(5)
    if keys[pygame.K_RIGHT]:
        player_x_pad.move_right(5)
        player_x2_pad.move_right(5)
    if keys[pygame.K_LEFT]:
        player_x_pad.move_left(5)
        player_x2_pad.move_left(5)

    # computer paddles move along with the ball
    if ball.velocity[0] < 0 and ball.velocity[1] > 0:
        comp_y_pad.move_down(5)
    if ball.velocity[0] < 0 and ball.velocity[1] < 0:
        comp_y_pad.move_up(5)
    if ball.velocity[0] < 0 and ball.velocity[1] > 0:
        comp_x_pad.move_right(5)
        comp_x2_pad.move_right(5)
    if ball.velocity[0] < 0 and ball.velocity[1] < 0:
        comp_x_pad.move_left(5)
        comp_x2_pad.move_left(5)

    sprites.update()
    gameDisplay.fill(BLACK)

    # draw middle line
    pygame.draw.line(gameDisplay, WHITE, [349, 0], [349, 500], 5)
    x = 0
    while x < 1000:
        pygame.draw.line(gameDisplay, BLACK, [0, x], [500, x], 20)
        x = x + 50

    # play sound for each opponent point and throw ball from
    # middle of screen at random velocities
    if ball.rect.x >= 690:
        comp_score += 1
        pygame.mixer.music.load('computer_point.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(4, 8)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x > 350 and (ball.rect.y < 10 or ball.rect.y > 490):
        comp_score += 1
        pygame.mixer.music.load('computer_point.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(4, 8)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x <= 0:
        player_score += 1
        pygame.mixer.music.load('player_point.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(-8, -4)
        ball.velocity[1] = random.randint(-8, 8)
    if ball.rect.x < 350 and (ball.rect.y < 10 or ball.rect.y > 490):
        player_score += 1
        pygame.mixer.music.load('player_point.ogg')
        pygame.mixer.music.play(0)
        ball.rect.x = 345
        ball.rect.y = 195
        ball.velocity[0] = random.randint(-8, -4)
        ball.velocity[1] = random.randint(-8, 8)

    # score tracking
    if comp_score >= 11 and comp_score > player_score + 2:
        comp_score = 0
        player_score = 0
        comp_win += 1
    if player_score >= 11 and player_score > comp_score + 2:
        comp_score = 0
        player_score = 0
        player_win += 1

    font = pygame.font.Font(None, 30)
    text = font.render(str(comp_score), 1, WHITE)

    # game win sounds and end game rematch prompt
    game_limit = comp_win + player_win
    if player_win == 3 and total_wins <= game_limit:
        if end_game == 0:
            pygame.mixer.music.load('winner_song.ogg')
            pygame.mixer.music.play(0)
            end_game = 1
        ball.velocity[0] = 0
        ball.velocity[1] = 0
        text = font.render(str('PLAYER WINS! REMATCH? Y/N'), 1, WHITE)
        gameDisplay.blit(text, (170, 250))
        if keys[pygame.K_n]:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if keys[pygame.K_y]:
            ball.velocity[0] = random.randint(4, 8)
            ball.velocity[1] = random.randint(-8, 8)
            pygame.mixer.music.stop()
            comp_win = 0
            comp_score = 0
            player_score = 0
            player_win = 0
            end_game = 0

    if comp_win == 3 and total_wins <= game_limit:
        if end_game == 0:
            pygame.mixer.music.load('loser_song.ogg')
            pygame.mixer.music.play(0)
            end_game = 1
        ball.velocity[0] = 0
        ball.velocity[1] = 0
        text = font.render(str('COMPUTER WINS! REMATCH? Y/N'), 1, WHITE)
        gameDisplay.blit(text, (170, 250))
        if keys[pygame.K_n]:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if keys[pygame.K_y]:
            pygame.mixer.music.stop()
            ball.velocity[0] = random.randint(4, 8)
            ball.velocity[1] = random.randint(-8, 8)
            comp_win = 0
            comp_score = 0
            player_score = 0
            player_win = 0
            end_game = 0

    score_update(comp_score, player_score, comp_win, player_win)
    sprites.draw(gameDisplay)
    pygame.display.flip()
    clock.tick(60)

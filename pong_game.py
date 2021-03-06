import pygame
import random
import math

pygame.init()
from pygame import mixer

screen = pygame.display.set_mode((1350, 629))
pygame.display.set_caption("PONG")
icon = pygame.image.load("nissan_foria_sketch-wallpaper.png")
pygame.display.set_icon(icon)
background = pygame.image.load("map8.jpg")
background1 = pygame.image.load("map8.jpg")


img1 = pygame.image.load("paddleblue.png")
img1X = 40
img1Y = 315
img1X_change = 0
img1Y_change = 0

img2 = pygame.image.load("paddlered.png")
img2X = 1290
img2Y = 315
img2X_change = 0
img2Y_change = 0

ball = pygame.image.load("ball1.png")
ballX = 658
ballY = 303
ballX_change = 0
ballY_change = 0

count = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 40
textY = 40

count1 = 0
score2 = 0
score1 = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)
text1X = 1160
text1Y = 40

font2 = pygame.font.Font('freesansbold.ttf', 32)
text2X = 500
text2Y = 35

i = 1
j = 1
k1 = 0
k2 = 0
k = 0


mixer.music.load("over.wav")
mixer.music.play()

def start(x, y):
    c = font2.render("And Space Bar to Start!", True, (255, 255, 0))
    c1 = font2.render("And Space Bar to Start!", True, (255, 255, 0))
    c2 = font2.render("And Space Bar to Start!", True, (255, 255, 0))
    screen.blit(c, (x, y))
    screen.blit(c1, (x, y+60))
    screen.blit(c2, (x, y+120))

def select(x, y):
    c = font2.render(" * Press 3 for 3 points match", True, (150, 150, 150))
    c1 = font2.render(" * Press 5 for 5 points match", True, (150, 150, 150))
    c2 = font2.render(" * Press 7 for 7 points match", True, (150, 150, 150))
    screen.blit(c, (x, y))
    screen.blit(c1, (x, y+60))
    screen.blit(c2, (x, y+120))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background1, (0, 0))
    select(text2X-320, text2Y+100)
    start(text2X+130, text2Y+100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
            if event.key == pygame.K_3:
                mixer.music.load("select.wav")
                mixer.music.play()
                k = 3
            if event.key == pygame.K_5:
                mixer.music.load("select.wav")
                mixer.music.play()
                k = 5
            if event.key == pygame.K_7:
                mixer.music.load("select.wav")
                mixer.music.play()
                k = 7
    pygame.display.update()


def image1(x, y):
    screen.blit(img1, (x, y))


def image2(x, y):
    screen.blit(img2, (x, y))


def ball1(x, y):
    screen.blit(ball, (x, y))


def collision(ballX, ballY, img2X, img2Y):
    distance1 = math.sqrt((math.pow(ballX - (img2X), 2)) + (math.pow(ballY - (img2Y + 20), 2)))
    if distance1 < 40:
        return True
    else:
        return False


def collision1(ballX, ballY, img1X, img1Y):
    distance = math.sqrt((math.pow(ballX - (img1X - 21), 2)) + (math.pow(ballY - (img1Y + 30), 2)))
    if distance < 40:
        return True
    else:
        return False


def show_score1(count, x, y):
    score = font.render("Score : " + str(count), True, (0, 0, 255))
    screen.blit(score, (x, y))


def show_score2(count1, x, y):
    score = font1.render("Score : " + str(count1), True, (255, 0, 0))
    screen.blit(score, (x, y))


def increase(count, i):
    mixer.music.load("score.wav")
    mixer.music.play()
    count = count + i
    print("blue==>", count)
    return count


def increase1(count1, j):
    mixer.music.load("score.wav")
    mixer.music.play()
    count1 = count1 + j
    print("red==>", count1)
    return count1


running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    if img2Y >= 510:
        img2Y_change = 0

    if img2Y <= 40:
        img2Y_change = 0

    if img1Y >= 510:
        img1Y_change = 0

    if img1Y <= 40:
        img1Y_change = 0

    if ballY <= 30:
        ballY_change = 5

    if ballY >= 570:
        ballY_change = -5

    if ballX <= 10:
        ballX_change = 0
        ballY_change = 0

    if ballX >= 1330:
        ballX_change = 0
        ballY_change = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                img2Y_change = -4
            if event.key == pygame.K_DOWN:
                img2Y_change = 4
            if event.key == pygame.K_w:
                img1Y_change = -4
            if event.key == pygame.K_s:
                img1Y_change = 4
            if event.key == pygame.K_SPACE:
                ballY_change = random.randint(-5, 5)
                ballX_change = random.randint(-5, 5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                img2Y_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                img1Y_change = 0

    img1Y += img1Y_change
    img2Y += img2Y_change
    ballX += ballX_change
    ballY += ballY_change

    image1(img1X, img1Y)
    image2(img2X, img2Y)
    ball1(ballX, ballY)

    col = collision(ballX, ballY, img2X, img2Y)
    if col:
        ballX_change = -(random.randint(1, 3))
        ballY_change = -(random.randint(1, 3))
    elif col is False and ballX >= 1280:
        score1 = increase(count, i)
        i = i + 1
        ballX = 658
        ballY = 303
        ballY_change = 0
        ballX_change = 0
        k1 += 1

    col1 = collision1(ballX, ballY, img1X, img1Y)
    if col1:
        ballX_change = random.randint(1, 3)
        ballY_change = random.randint(1, 3)
    elif col is False and ballX <= 35:
        score2 = increase1(count1, j)
        j = j + 1
        ballX = 658
        ballY = 303
        ballY_change = 0
        ballX_change = 0
        k2 += 1
    if(k1==k):
        break
    if(k2==k):
        break
    show_score1(score1, textX, textY)
    show_score2(score2, text1X, text1Y)
    pygame.display.update()

mixer.music.load("over.wav")
mixer.music.play(-1)

def over(x, y):
    if(k1>k2):
        c = font2.render("BLUE ", True, (255, 215, 0))
        c1 = font2.render("PLAYER WINS!", True, (5, 175, 100))
    else:
        c = font2.render("RED ", True, (255,215,0))
        c1 = font2.render("PLAYER WINS!", True, (5,175,100))
    screen.blit(c, (x, y))
    screen.blit(c1, (x+90, y))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background1, (0, 0))
    over(text2X, text2Y+100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

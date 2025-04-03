import pygame
import pygame_gui
import sys
import os
from playerController import Player
from databaseManagement import Users
pygame.init()
screen = pygame.display.set_mode((1280, 720))
coords = (50,50)
player = Player((0,0), 100, 100, 1, 0, 'KBM')
rect = pygame.Rect(coords[0], coords[1],250,250)

UIManager = pygame_gui.UIManager((1280, 720))
userManagement = Users()

loginBackground = pygame.image.load(os.path.join('images', 'loginPage.png'))
loginErrorBackground = pygame.image.load(os.path.join('images', 'loginErrorPage.png'))
accountCreationBackground = pygame.image.load(os.path.join('images', 'signUpPage.png'))
accountCreationErrorBackground = pygame.image.load(os.path.join('images', 'signUpErrorPage.png'))
joinGameBackground = pygame.image.load(os.path.join('images', 'joinGame.png'))

clock = pygame.time.Clock()

loginFont = pygame.font.SysFont('Consolas', 24)
errorFont = pygame.font.SysFont('Consolas', 15)
usernameInput = loginFont.render('Enter username', True, (0,0,0))
passwordInput = loginFont.render('Enter password', True, (0,0,0))
submitButton = loginFont.render('SUBMIT', True, (0,0,0))
createAccountText = loginFont.render('Create Account', True, (0,0,0))
loginError = errorFont.render('Account not found.', True, (255,0,0))
passwordError = errorFont.render('Ensure password contains at least:\n1 Special character\n1 letter\n1 number\n8 characters', True, (255,0,0))
textItems = [[usernameInput, (566, 190)], [passwordInput, (566, 270)], [submitButton, (620, 390)]]
buttons = [[pygame.Rect(560,220,200,40), 0], [pygame.Rect(560,300,200,40), 0], [pygame.Rect(540, 380, 240, 40), 0], [pygame.Rect(140,219, )]]
usernameTextInput = pygame_gui.elements.UITextEntryLine(relative_rect = buttons[0][0], manager=UIManager, object_id='#main_text_entry')
passwordTextInput = pygame_gui.elements.UITextEntryLine(relative_rect = buttons[1][0], manager=UIManager, object_id='#main_text_entry')



def loginSubmit():
    username = usernameTextInput.text; password = passwordTextInput.text
    data = userManagement.login(username, password)
    if data[0] == True:
        login(True)
    else:
        joinGame()

def createAccountSubmit():
    username = usernameTextInput.text; password = passwordTextInput.text
    data = userManagement.createAccount(username, password)
    if data[0] == True:
        createAccount(True)
    else:
        joinGame()
        


def createAccount(error):
    while True:
        clock.tick(60)
        UIRefreshRate = clock.tick(60)/500

        if not error:
            screen.blit(accountCreationBackground, (0,0))
        else:
            screen.blit(accountCreationErrorBackground, (0,0))
            screen.blit(passwordError, (520, 450))

        for textItem in textItems:
            screen.blit(textItem[0], textItem[1])

        UIManager.draw_ui(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.mouse.get_pressed()[0] == 1:
                for button in buttons:
                    if pygame.Rect.collidepoint(button[0], pygame.mouse.get_pos()):
                        for i in range(len(buttons)):
                            if buttons[i] == button:
                                buttons[i][1] = 1
                                if i == 2:
                                    createAccountSubmit()

            UIManager.process_events(event)
        

        UIManager.update(UIRefreshRate)
        pygame.display.flip()

def login(error):
    while True:
        clock.tick(60)
        UIRefreshRate = clock.tick(60)/500
        if not error:
            screen.blit(loginBackground, (0,0))
        else:
            screen.blit(loginErrorBackground, (0,0))
            screen.blit(loginError, (520, 450))
        for textItem in textItems:
            screen.blit(textItem[0], textItem[1])

        UIManager.draw_ui(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if pygame.mouse.get_pressed()[0] == 1:
                for button in buttons:
                    if pygame.Rect.collidepoint(button[0], pygame.mouse.get_pos()):
                        for i in range(len(buttons)):
                            if buttons[i] == button:
                                buttons[i][1] = 1
                                if i == 2:
                                    loginSubmit()
                    
            UIManager.process_events(event)


        UIManager.update(UIRefreshRate)
        pygame.display.flip()

def joinGame():
    while True:
        screen.blit(joinGameBackground, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if pygame.mouse.get_pressed()[0] == 1:
                print(pygame.mouse.get_pos())
        pygame.display.flip()
    
def mainGame():
    while True:
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,0,0), rect)
        rect.topleft = player.movexy()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

#login(False)
#createAccount(False)
#mainGame()
joinGame()
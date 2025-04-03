import hashlib
import pygame
import string
import sqlite3
pygame.init()
screen = pygame.display.set_mode((1280, 720))

class Users:
    def __init__(self):
        self.hash = hashlib.sha256()
        self.alphabet = string.ascii_letters
        self.specialCharacters = string.punctuation
        self.numbers = ['1','2','3','4','5','6','7','8','9','0']
        self.conn = sqlite3.connect('clientData.db')
        self.curs = self.conn.cursor()

    def login(self, username, password):
        hashedUsername = hashlib.sha256(username.encode()).hexdigest()
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()
        data = self.curs.execute("SELECT password FROM tblUsers WHERE username==(?)", (hashedUsername, ))
        for i in data:
            print(i)
            if i[0] != None and i[0] == hashedPassword:
                return False, hashedUsername, hashedPassword
            else:
                print("Account not found.")
                return True, '', ''
    
    def createAccount(self, username, password):
        if len(password) >= 8:
            containsSpecialCharacters=False
            containsLetters=False
            containsNumbers=False
            for i in password:
                if i in self.specialCharacters:
                    containsSpecialCharacters=True
                elif i in self.alphabet:
                    containsLetters=True
                elif i in self.numbers:
                    containsNumbers=True

            if containsNumbers and containsSpecialCharacters and containsLetters:
                hashedUsername = hashlib.sha256(username.encode()).hexdigest()
                hashedPassword = hashlib.sha256(password.encode()).hexdigest()
                self.curs.execute("INSERT INTO tblUsers(username, password) VALUES(?, ?)", (hashedUsername, hashedPassword))
                self.conn.commit()
                return False, hashedUsername, hashedPassword
            
            else:
                print('not met requirements.', containsNumbers, containsLetters, containsSpecialCharacters)
                return True, '', ''
            
        else:
           print('not met requirements.')
           return True, '', ''
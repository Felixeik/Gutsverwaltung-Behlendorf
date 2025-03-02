import pygame
from raum import Raum

class Raum6(Raum):
    def init(self):
        self.platforms = [pygame.Rect(0,437, 140, 10),pygame.Rect(260,441, 75, 10),pygame.Rect(420,445, 85, 10),pygame.Rect(592,437, 48, 10),pygame.Rect(740,441, 60, 10)]
        

    def handleEvent(self, event, spielstand):
        # Maus klicken
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            
           
    def handleLogic(self, spielstand):
        spielstand.playerJumping = True


        self.player_rect = pygame.Rect(spielstand.playerX, spielstand.playerY, 80, 140)

        for platform in self.platforms:
            if self.player_rect.colliderect(platform):
                spielstand.playerY = platform.y - spielstand.playerHeight
                spielstand.playerJumping = False

    def drawBehindPlayer(self, window, spielstand):
       


        # Bilder einfügen
        window.blit(self.hintergrund, (0, 0))
        #window.blit(self.rahmen, (0, 0))
        #window.blit(self.inventar, (window.get_width() / 2 - 238, 40))


    
    def drawInFrontOfPlayer(self, window, spielstand):
        
        # hitbox spieler anzeigen
        pygame.draw.rect(window, (255, 0, 0), self.player_rect, 2)

        #window.blit(self.inventar, (window.get_width() / 2 - 238, 40))

        for platform in self.platforms:
            pygame.draw.rect(window, (255,0,0), platform)
        pass

import pygame
from player import Player
from network import Network
from subsurface import Subsurface


def redrawWindow(window, player1, player2):
    
    window.fill((255,255,255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.flip()
    

def main():
    
    width, height = 500, 500
    window = pygame.display.set_mode((width, height))
    
    n = Network()
    player1 = n.getPlayer()
    
    pygame.display.set_caption("Client")
    
    run = True    
    clock = pygame.time.Clock()
    
    while run:
        
        clock.tick(7)
        player2 = n.send(player1)
        
        for event in pygame.event.get():
            print(event)    
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            
        player1.move(window, event)
        redrawWindow(window, player1, player2)
        
if __name__ == "__main__":
    main()
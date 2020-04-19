import pygame

class Subsurface:
    
    def __init__(self, path, clip):
        self.sheet = pygame.image.load(path)
        self.sheet.set_clip(clip)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rectangle = self.image.get_rect()        
        
        
        
    def getSubsurface(self):
        return self.image#, self.rectangle
        
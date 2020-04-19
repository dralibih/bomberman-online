import pygame
from subsurface import Subsurface

class Player:
    
    def __init__(self, rectangle):
        
        self.image = '../sprite/player.png'
        self.speed = 10
        self.rectangle = pygame.Rect(rectangle)
        self.clip = (60,90,60,90)
        self.frame = 1
        self.down_states = { 0: (0, 0, 60, 90), 1: (60, 0, 60, 90), 2: (120, 0, 60, 90) }
        self.up_states = { 0: (0, 90, 60, 90), 1: (60, 90, 60, 90), 2: (120, 90, 60, 90) }
        self.left_states = { 0: (0, 180, 60, 90), 1: (60, 180, 60, 90), 2: (120, 180, 60, 90) }
        self.right_states = { 0: (0, 270, 60, 90), 1: (60, 270, 60, 90), 2: (120, 270, 60, 90) }
        
    def draw(self, window):
        print(self.rectangle)
        subsurface = Subsurface(self.image, pygame.Rect(self.clip))
        image = subsurface.getSubsurface()
        window.blit(image, self.rectangle)
        
    def getFrame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
    def getClip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.clip = pygame.Rect(self.getFrame(clipped_rect))
        else:
            self.clip = pygame.Rect(clipped_rect)
        return clipped_rect
    
    def update(self, window, direction):
        if direction == 'left':
            self.getClip(self.left_states)
            self.rectangle.x -= self.speed
        if direction == 'right':
            self.getClip(self.right_states)
            self.rectangle.x += self.speed
        if direction == 'up':
            self.getClip(self.up_states)
            self.rectangle.y -= self.speed
        if direction == 'down':
            print(self.down_states)
            self.getClip(self.down_states)
            self.rectangle.y += self.speed

        if direction == 'stand_left':
            self.getClip(self.left_states[1])
        if direction == 'stand_right':
            self.getClip(self.right_states[1])
        if direction == 'stand_up':
            self.getClip(self.up_states[1])
        if direction == 'stand_down':
            self.getClip(self.down_states[1])

        self.draw(window)


    def move(self, window, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update(window, 'left')
            if event.key == pygame.K_RIGHT:
                self.update(window, 'right')
            if event.key == pygame.K_UP:
                self.update(window, 'up')
            if event.key == pygame.K_DOWN:
                self.update(window, 'down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update(window, 'stand_left')
            if event.key == pygame.K_RIGHT:
                self.update(window, 'stand_right')
            if event.key == pygame.K_UP:
                self.update(window, 'stand_up')
            if event.key == pygame.K_DOWN:
                self.update(window, 'stand_down')

    
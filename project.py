# יבאנו את ספריית Pygame
import pygame 
from pygame import time, mouse, draw, font

# פתיחת החלון וקביעת הגודל שלו
pygame.init()
pygame.display.set_caption('')
window = 800
window_ = 600
window1 = pygame.display.set_mode((window,window_))
# הרקע לחלון
image = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\backround.jpeg').convert()
image = pygame.transform.scale(image,(window-50,window_-50))
window1.blit(image, (0, 0))
pygame.display.flip()





image2 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download-removebg-preview-PhotoRoom.png-PhotoRoom.png').convert()
image2 = pygame.transform.scale(image2,(100,100))
window1.blit(image2, (70, 50))
pygame.display.flip()


image3 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\images.png').convert()
image3 = pygame.transform.scale(image3,(100,100))
window1.blit(image3, (250, 50))
pygame.display.flip()



# create the font object
font = pygame.font.Font(None, 36)

# render the text as a surface
text = font.render("Hello, World!", True, (255,255,255))
window1.blit(text, (window1.get_width() // 2 - text.get_width() // 2, window1.get_height() // 2 - text.get_height() // 2))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False













































pygame.quit()
# יבאנו את ספריית Pygame
import pygame 
from pygame import time, mouse, draw, font
from pygame.locals import *




# פתיחת החלון וקביעת הגודל שלו
pygame.init()

pygame.display.set_caption('')
window = 800
window_ = 600
window1 = pygame.display.set_mode((window,window_))
# הרקע לחלון
image = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\backround.jpeg').convert()
image = pygame.transform.scale(image,(window,window_))
window1.blit(image, (0, 0))
pygame.display.flip()
    




image2 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download-removebg-preview-PhotoRoom.png-PhotoRoom.png').convert()
image2 = pygame.transform.scale(image2,(100,100))
window1.blit(image2, (70, 50))
pygame.display.flip()


image3 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\images.png').convert()
image3 = pygame.transform.scale(image3,(100,100))
window1.blit(image3, (350, 50))
pygame.display.flip()


image4 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\images (1234651).png').convert()
image4 = pygame.transform.scale(image4,(100,100))
window1.blit(image4, (600, 50))
pygame.display.flip()





# create the font object
font = pygame.font.Font(None, 24)

# render the text as a surface
text = font.render("Mini Game Questions", True, (255,255,255))
window1.blit(text, (window1.get_width() // 2 - text.get_width() // 2, window1.get_height() // 2 - text.get_height() // 0.125))
pygame.display.flip()



text1 = font.render("DRAWING game", True, (255,255,255))
window1.blit(text1, (window1.get_width() // 2 - text1.get_width() // 0.375, window1.get_height() // 2 - text1.get_height() // 0.125))
pygame.display.flip()


text2 = font.render("Settings", True, (255,255,255))
window1.blit(text2, (window1.get_width() // 1.275- text2.get_width() // 6.5, window1.get_height() // 2 - text2.get_height() // 0.125))
pygame.display.flip()








button1 = image2.get_rect(topleft=(70, 50))
button2 = image3.get_rect(topleft=(350, 50))
button3 = image4.get_rect(topleft=(600, 50))


def open_new_window1():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window2 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window2.blit(image5, (0, 0))
    pygame.display.flip()
    pygame.draw.rect(window2, (0, 0, 255),
                 [100, 100, 400, 100], 2)
    pygame.display.update()
    
def open_new_window2 ():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window3 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window3.blit(image5, (0, 0))
    pygame.display.flip()







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if button1.collidepoint(pos):
                    open_new_window1()
                elif button2.collidepoint(pos):
                    open_new_window2()
                elif button3.collidepoint(pos):
                    print("Clicked button 3")
                    new_window = pygame.display.set_mode((window, window_))






pygame.quit()
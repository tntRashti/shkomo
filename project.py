# יבאנו את ספריית Pygame
import pygame 
from pygame import time, mouse, draw, font
from pygame.locals import *
import random

# פתיחת החלון וקביעת הגודל שלו
pygame.init()

pygame.display.set_caption('window 15')
window = 800
window_ = 600
window1 = pygame.display.set_mode((window,window_))
# הרקע לחלון
image = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\imagdsdsfsdfsddfsfsdawdfsasdfsfses.png').convert()
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


image4 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\downloadsdasda.png').convert()
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


text2 = font.render("Games Of Words", True, (255,255,255))
window1.blit(text2, (window1.get_width() // 1.275- text2.get_width() // 6.5, window1.get_height() // 2 - text2.get_height() // 0.125))
pygame.display.flip()







button1 = image2.get_rect(topleft=(70, 50))
button2 = image3.get_rect(topleft=(350, 50))
button3 = image4.get_rect(topleft=(600, 50))



def try_try ():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window4 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window4.blit(image5, (0, 0))
    pygame.display.flip()
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface

    list_words = ('television','grade','ghost','elephent','python')
    _list_words_ = random.choice(list_words)
    
    
    
    
    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == _list_words_:
                        print ('excellent')
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        window4.fill((255, 255, 255))
        text = font.render("write   "+_list_words_, True, (0,0,0))
        window4.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window4, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window4.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()




def for_window_3():
    pygame.quit()
    pygame.init()
    window_size = (window, window_)
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    pygame.display.update()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:


                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0,0,255), pos, 20)


            pygame.display.update()


def for_window_2():
    pygame.quit()
    pygame.init()
    window_size = (window, window_)
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    pygame.display.update()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:


                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0,255,0), pos, 20)


            pygame.display.update()


def for_window_1():
    pygame.quit()
    pygame.init()
    window_size = (window, window_)
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    pygame.display.update()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:


                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (255,0,0), pos, 20)


            pygame.display.update()
    
    
    



def open_new_window1():
    pygame.init()
    

# Set up the window
    window_size = (window, window_)
    screen = pygame.display.set_mode(window_size)
    img = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\download (1).png').convert()
    img = pygame.transform.scale(img,(100,100))
    screen.blit(img, (350, 50))
    pygame.display.flip()
    button_1 = img.get_rect(topleft=(70, 50))


    
    img2 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\dosdfgfdgdgd (2).png').convert()
    img2 = pygame.transform.scale(img2,(100,100))
    screen.blit(img2, (70, 50))
    pygame.display.flip()
    button_2 = img.get_rect(topleft=(350, 50))

    img3 = pygame.image.load('C:\\Users\\user\\OneDrive\\שולחן העבודה\\project with tal\\sdsdsfsfdsmkvdnbrgjhngse(2).png').convert()
    img3 = pygame.transform.scale(img3,(100,100))
    screen.blit(img3, (600, 50))
    pygame.display.flip()
    button_3 = img.get_rect(topleft=(600, 50))


    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if button_1.collidepoint(pos):
                        for_window_1()
                    elif button_2.collidepoint(pos):
                        for_window_2()
                    elif button_3.collidepoint(pos):
                        for_window_3()
                    
    
           
   
                    








def for_window4 ():
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
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '123456':
                        running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        window3.fill((255, 255, 255))
        text = font.render("Enter Password:", True, (0,0,0))
        window3.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window3, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window3.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()



def for_window3 ():
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
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '123456':
                        for_window4()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        window3.fill((255, 255, 255))
        text = font.render("Enter Password:", True, (0,0,0))
        window3.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window3, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window3.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()




def open_new_window2():
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
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '77':
                        for_window3()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        window3.fill((255, 255, 255))
        text = font.render("5+4(3*6)", True, (0,0,0))
        window3.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window3, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window3.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()






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
                    try_try()
                    new_window = pygame.display.set_mode((window, window_))






pygame.quit()
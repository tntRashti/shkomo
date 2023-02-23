# יבאנו את ספריית Pygame
import pygame 
from pygame import time, mouse, draw, font
import random

# פתיחת החלון וקביעת הגודל שלו
pygame.init()

pygame.display.set_caption('window 15')
window = 800
window_ = 600
window1 = pygame.display.set_mode((window,window_))
# הרקע לחלון
image = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\imagdsdsfsdfsddfsfsdawdfsasdfsfses.png').convert()
image = pygame.transform.scale(image,(window,window_))
window1.blit(image, (0, 0))
pygame.display.flip()
    


# תמונות של המשחקים

image2 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download-removebg-preview-PhotoRoom.png-PhotoRoom.png').convert()
image2 = pygame.transform.scale(image2,(100,100))
window1.blit(image2, (70, 50))
pygame.display.flip()


image3 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\images.png').convert()
image3 = pygame.transform.scale(image3,(100,100))
window1.blit(image3, (350, 50))
pygame.display.flip()


image4 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\downloadsdasda.png').convert()
image4 = pygame.transform.scale(image4,(100,100))
window1.blit(image4, (600, 50))
pygame.display.flip()





# create the font object
font = pygame.font.Font(None, 24)
font1 = pygame.font.Font(None, 46)

# render the text as a surface
text = font.render("Mini Game Math Questions", True, (255,255,255))
window1.blit(text, (window1.get_width() // 2 - text.get_width() // 2, window1.get_height() // 2 - text.get_height() // 0.125))
pygame.display.flip()



text1 = font.render("DRAWING game", True, (255,255,255))
window1.blit(text1, (window1.get_width() // 2 - text1.get_width() // 0.375, window1.get_height() // 2 - text1.get_height() // 0.125))
pygame.display.flip()


text2 = font.render("Games Of Words", True, (255,255,255))
window1.blit(text2, (window1.get_width() // 1.275- text2.get_width() // 6.5, window1.get_height() // 2 - text2.get_height() // 0.125))
pygame.display.flip()






# יצירת הכפתורים
button1 = image2.get_rect(topleft=(70, 50))
button2 = image3.get_rect(topleft=(350, 50))
button3 = image4.get_rect(topleft=(600, 50))





    
    
    

    

# יצירת המשחק של המילים 

def try_try ():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window4 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window4.blit(image5, (0, 0))
    pygame.display.flip()
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface
# יוצרים את רשימת המילים ומקום הכתיבה שלהם
    list_words = ('television','grade','ghost','elephent','python')
    _list_words_ = random.choice(list_words)
    
    
        
    
    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''

    coren_time = 0

#  מתחיל בכך שברגע שלוחצים לסגור את התוכנית היא נסגרת וכותבים את המילה הנכונה התוכניתצ לא נסגרת והיא רושמת מתויין ואת הזמן שלקח לך לכתוב את המילה
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == _list_words_:
                        coren_time = pygame.time.get_ticks()
                        coren_time = coren_time/1000
                        print (coren_time,'sec')
                        print ('excellent')
                        try_try ()
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



# מה שקורה כאשר לוחצים על התמונה הכחולה בתוך הצייר
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
# מה שקורה כאשר לוחצים על התמונה הירוקה בצייר
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

# מה שקורה כאשר לוחצים על התמונה האדומה בצייר
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
    
    
    

# מה שקורה כאשר לוחצים על התמונה של הצייר

def open_new_window1():
    pygame.init()
    

# Set up the window
    window_size = (window, window_)
    screen = pygame.display.set_mode(window_size)
    img = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download (1).png').convert()
    img = pygame.transform.scale(img,(100,100))
    screen.blit(img, (350, 50))
    pygame.display.flip()
    button_1 = img.get_rect(topleft=(70, 50))


    #  יציראת מיקום התמונות והגגדרת הכפתורים 
    img2 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\project with tal\\dosdfgfdgdgd (2).png').convert()
    img2 = pygame.transform.scale(img2,(100,100))
    screen.blit(img2, (70, 50))
    pygame.display.flip()
    button_2 = img.get_rect(topleft=(350, 50))

    img3 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\sdsdsfsfdsmkvdnbrgjhngse(2).png').convert()
    img3 = pygame.transform.scale(img3,(100,100))
    screen.blit(img3, (600, 50))
    pygame.display.flip()
    button_3 = img.get_rect(topleft=(600, 50))


    

    text_01= font1.render("click on the color that u want to draw with", True, (255,255,255))
    screen.blit(text_01, (screen.get_width() // 2 - text_01.get_width() // 2, screen.get_height() // 2 - text_01.get_height() // 0.5))
    pygame.display.flip()





    # מה קורה כאשר לוחצים על התמונות 
    
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
                    
    
           
   
                    






# יצירת החלון האחרון של משחק השאלות

def for_window4 ():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window3 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window3.blit(image5, (0, 0))
    pygame.display.flip()
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''
# כאן רואים מה קורה כאשר מקלידים את הספרה הנכונה (זה כותב מצויין וסוגר אץ התתכנית)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '2160':
                        print ('exellent')
                        running = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
# מגדיר את מיקום השאלה ואת חלונית הטקסט
        window3.fill((255, 255, 255))
        text = font.render("6*24*15", True, (0,0,0))
        window3.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window3, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window3.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()

# יצירת החלון השני של השאלות

def for_window3 ():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window3 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window3.blit(image5, (0, 0))
    pygame.display.flip()
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''
# עושה כאשר מקלידים את הספרה הנכונה אז זה רושם מצויין ומעברי לשאלה הבאה 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == '468':
                        for_window4()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        window3.fill((255, 255, 255))
        text = font.render("(13*18)2", True, (0,0,0))
        window3.blit(text, (window // 2 - text.get_width() // 2, window_ // 2 - text.get_height() // 0.125))
        pygame.display.flip()
        pygame.draw.rect(window3, (0, 0, 0), input_box, 2)
        font = pygame.font.Font(None, 24)
        input_surf = font.render(input_text, True, (0, 0, 0))
        window3.blit(input_surf, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        pygame.display.update()


# יצירת משחק השאלות והחלון הראשון 

def open_new_window2():
    pygame.quit()
    pygame.init()
    pygame.display.set_caption('')
    window = 800
    window_ = 600
    window3 = pygame.display.set_mode((window,window_))
    image5 = pygame.image.load('C:\\Users\\יהונתן\\Desktop\\project with tal\\download.png').convert()
    image5 = pygame.transform.scale(image5,(window,window_))
    window3.blit(image5, (0, 0))
    pygame.display.flip()
    
    # create the font object
    font = pygame.font.Font(None, 32)

    # render the text as a surface


    input_box = pygame.Rect(window // 2 - 100, window_ // 2 + 20, 200, 32)
    input_text = ''
# השאלה הראשונה כלומר ברגע שמקלידים את הספרה הנכונה זה מעביר לשאלה הבאה
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



# מה שקורה כאשר לוחצים על אחד מהמשחקים במסך הבית

def main():
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



if __name__ == '__main__':
    main() 


pygame.quit()
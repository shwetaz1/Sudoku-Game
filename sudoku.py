#Created by Shweta Zade
#Initializing sudoku game window and variables
import pygame
import pyttsx3
pygame.font.init()
Window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SUDOKU GAME")
x = 0
z = 0
y = 0
diff = 500 / 9
value= 0
defaultgrid =[
       [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

font = pygame.font.SysFont("comicsans", 30)
font1 = pygame.font.SysFont("comicsans", 10)
engine=pyttsx3.init() 
voices = engine.getProperty('voices') 
engine.setProperty(voices , voices[-2].id) 
engine.say ('Welcome to Sudoku game ')
engine.runAndWait() 

def cord(pos):
    global x
    x = pos[0]//diff
    global z
    z = pos[1]//diff
 
#Function for highlighting selected cell 
def highlightbox():
    for k in range(2):
        pygame.draw.line(Window, (0, 0, 0), (x * diff-3, (z + k)*diff), (x * diff + diff + 3, (z + k)*diff), 7)
        pygame.draw.line(Window, (0, 0, 0), ( (x + k)* diff, z * diff ), ((x + k) * diff, z * diff + diff), 7) 

#Function to draw lines for making sudoku grid
def drawlines():
    for i in range (9):
        for j in range (9):
            if defaultgrid[i][j]!= 0:
                pygame.draw.rect(Window, (255,255,0), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(defaultgrid[i][j]), 1, (0, 0, 0))
                Window.blit(text1, (i * diff + 15, j * diff + 15))         
    for l in range(10):
        if l % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Window, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(Window, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)

#Function to fill value in the cell
def fillvalue(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Window.blit(text1, (x * diff + 15, z * diff + 15)) 

#Function for raising error when wrong value is entered 
def raiseerror():
    text1 = font.render("wrong!", 1, (0, 0, 0))
    Window.blit(text1, (20, 570)) 
    engine=pyttsx3.init() 
    voices = engine.getProperty('voices') 
    engine.setProperty( voices, voices[1].id) 
    engine.say ('Wrong number')
    engine.runAndWait() 
    print("WRONG NUMBER!")

def raiseerror1():
    text1 = font.render("wrong ! enter a valid key for the game", 1, (0, 0, 0))
    Window.blit(text1, (20, 570)) 

#Function to check if the entered value is valid
def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it]== value:
            return False
        if m[it][l]== value:
            return False

    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if m[k][l]== value:
                return False
    return True
      
#Function to solve sudoku game
def solvegame(defaultgrid, i, j):
    while defaultgrid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if validvalue(defaultgrid, i, j, it)== True:
            defaultgrid[i][j]= it
            global x, z
            x = i
            z = j
            Window.fill((255,128,0))
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(20)
            if solvegame(defaultgrid, i, j)== 1:
                return True
            else:
                defaultgrid[i][j]= 0
            Window.fill((0,0,0))
         
            drawlines()
            highlightbox()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 

#Function to show result
def gameresult():
    engine=pyttsx3.init() 
    voices = engine.getProperty('voices') 
    engine.setProperty( voices , voices[1].id) 
    engine.say ('Game Over')
    engine.runAndWait() 
    text1 = font.render("Game Over", 1, (0, 0, 0))
    Window.blit(text1, (20, 570)) 
    
flag=True  
flag1 = 0
flag2 = 0
rs = 0
error = 0

#Rest Code
while flag:
    Window.fill((0,0,128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2   
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                defaultgrid=[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                defaultgrid  =[
                    [0, 0, 4, 9, 1, 0, 0, 0, 2],
                    [1, 9, 0, 4, 0, 0, 0, 7, 0],
                    [0, 0, 7, 6, 0, 3, 0, 4, 8],
                    [5, 3, 0, 0, 8, 2, 0, 0, 4],
                    [0, 0, 2, 4, 6, 0, 0, 8, 3],
                    [0, 0, 1, 3, 9, 0, 6, 2, 0],
                    [0, 1, 0, 2, 0, 0, 0, 6, 0],
                    [0, 4, 0, 5, 0, 8, 0, 0, 1],
                    [0, 5, 0, 0, 0, 6, 7, 0, 0],
                ]
    if flag2 == 1:
        if solvegame(defaultgrid , 0, 0)== False:
            error = 1
        else:
            rs = 1
        flag2 = 0   
    if value != 0:           
        fillvalue(value)
        if validvalue(defaultgrid , int(x), int(z), value)== True:
            defaultgrid[int(x)][int(z)]= value
            flag1 = 0
        else:
            defaultgrid[int(x)][int(z)]= 0
            raiseerror()  
        value = 0   
       
    if error == 1:
        raiseerror() 
    if rs == 1:
        gameresult()
        print("YOU WIN!") 
    drawlines() 
    if flag1 == 1:
        highlightbox()      
    pygame.display.update() 
   
pygame.quit()    
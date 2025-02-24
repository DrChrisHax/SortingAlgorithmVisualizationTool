import matplotlib.pyplot as plt
import numpy as np

import pygame
import pygame_gui
import sys
import random

#initialize modules
pygame.init()

mainWidth = 380     #bgNBSS = 380   bgNB = 534 
mainHeight = 1079   #bgNBSS = 1079  bgNB = 1438

#frames per second
clock = pygame.time.Clock()
refreshRate = clock.tick(60)/1000

bg = pygame.image.load("bgNBSS.png")

#defines text colors
black = (0, 0, 0)
white = (255, 255, 255)
lightgrey = (217,217,217)
darkGrey = (84, 84, 84)
darkishGray = (166, 166, 166) 
green = (193,255,114)


#theme for text boxes
theme = {"minText":{"colours":
         {
             "dark_bg":"#FFFFFF",
             "normal_text":"#000000"
         }
        },
        "maxText":{"colours":
         {
             "dark_bg":"#FFFFFF",
             "normal_text":"#000000"
         }
        },        
        "numElementsText":{"colours":
         {
             "dark_bg":"#FFFFFF",
             "normal_text":"#000000"
         }
        }}


#manges UI elements (only deals with the text boxes since I didn't know pygame_gui existed)
uiManager = pygame_gui.UIManager((mainWidth, mainHeight), theme)

#
def MainMenu():
    screen = pygame.display.set_mode((mainWidth, mainHeight))
    pygame.display.set_caption("Algorithm Efficiency Analyzer")

    #buttons
    #sorting algorithm buttons
    buttonSize = (20, 20)
    buttonColor = white
    bX = 40        #button x coordinate
    bY = 325        #button y coordinate
    spaceFac = 37   #number of pixels each button is to be serpated

    #Algorithm buttons
    bubbleSortButton = Button("", buttonSize, buttonColor, (bX, bY), 20, black)
    mergeSortButton = Button("", buttonSize, buttonColor, (bX, bY + spaceFac), 20, black)
    quickSortButton = Button("", buttonSize, buttonColor, (bX, bY + spaceFac * 2), 20, black)
    radixSortButton = Button("", buttonSize, buttonColor, (bX, bY + spaceFac * 3), 20, black)
    linearSearchButton = Button("", buttonSize, buttonColor, (bX, bY + spaceFac * 4), 20, black)

    #Buttons for runtime and space
    runtimeButton = Button("", buttonSize, buttonColor, (230, 365), 20, black)
    spaceButton = Button("", buttonSize, buttonColor, (230, 410), 20, black)

    #buttons for controls
    controlButtonSize = (200, 65)
    resetButton = Button("Reset", controlButtonSize, buttonColor, (90, 700), 40, black, False)
    startButton = Button("Start/Stop", controlButtonSize, buttonColor, (90, 800), 40, black)

    #buttons for the graph comparisons
    graphButtonSize = (140, 40)
    lineGraphButton = Button("Line Graph", graphButtonSize, buttonColor, (40, 999), 25, black, False)
    barGraphButton = Button("Bar Graph", graphButtonSize, buttonColor, (200, 999), 25, black, False)



    #array of all active buttons
    buttonArray = [bubbleSortButton, mergeSortButton, quickSortButton,               #Array to keep track of the buttons on screen
                   radixSortButton, linearSearchButton, runtimeButton, 
                   spaceButton, resetButton, startButton, lineGraphButton,
                   barGraphButton]     


    #user boxtext inputs
    textBoxRectWidth = 70
    textBoxRectHeight = 40

    minTextBox = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(100, 85, textBoxRectWidth, textBoxRectHeight), manager=uiManager, object_id = "minText")
    maxTextBox = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(280, 85, textBoxRectWidth, textBoxRectHeight), manager=uiManager, object_id = "maxText")
    numElementsTextBox = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect(210, 152, textBoxRectWidth, textBoxRectHeight), manager=uiManager, object_id = "numElementsText")


    #vars for the array size
    min = "0"
    max = "100"
    numElements = "50"


    #set default textbox
    minTextBox.set_text(min)
    maxTextBox.set_text(max)
    numElementsTextBox.set_text(numElements)

    #ui update loop
    while True:
        clock.tick(24)              #set framerate

        screen.blit(bg, (0,0))

        #renders the buttons every frame
        for button in buttonArray:
            button.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #if a certain button is pressed, run that command
            if event.type == pygame.MOUSEBUTTONDOWN:

                #if you click off the text box, update the text box with new default values
                minTextBox.set_text(min)
                maxTextBox.set_text(max)
                numElementsTextBox.set_text(numElements)

                #buttons 0-4 are for the sorts and linear search

                if buttonArray[0].handleEvent(event):      #button 0 (bubble)
                    #
                    print("bubble")
                    #
                elif buttonArray[1].handleEvent(event):      #button 1 (merge)
                    #
                    print("merge")
                    #
                elif buttonArray[2].handleEvent(event):      #button 2 (quick)
                    #
                    print("quick")
                    #
                elif buttonArray[3].handleEvent(event):      #button 3 (radix)
                    #
                    print("radix")
                    #
                elif buttonArray[4].handleEvent(event):      #button 4 (linear search)
                    #
                    print("linear search")
                    #
                elif buttonArray[5].handleEvent(event):       #button 5 (runtime)
                    #
                    print("runtime")
                    #
                elif buttonArray[6].handleEvent(event):       #button 6 (space)
                    #
                    print("space")
                    #
                elif buttonArray[7].handleEvent(event):       #button # (reset)
                    #
                    print("R")
                    #
                elif buttonArray[8].handleEvent(event):       #button # (start)
                    #
                    print("S")
                    #
                elif buttonArray[9].handleEvent(event):       #button # (graph1 (line))
                    #
                    print("L")
                    #
                elif buttonArray[10].handleEvent(event):       #button # (graph2 (bar))
                    #
                    print("b")
                    #

            #save the text typed in the respective textbox in min, max, and numElements
            if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                if event.ui_object_id == "minText":
                    min = event.text

                    if(not min):    #default case if empty
                        min = "0"

                if event.ui_object_id == "maxText":
                    max = event.text

                    if(not max):    #default case if empty
                        max = "100"

                if event.ui_object_id == "numElementsText":
                    numElements = event.text
                    if(not numElements):    #default case if empty
                        numElements = "50"


        #update the text boxes every frame
        uiManager.process_events(event)
        uiManager.update(refreshRate)  
        uiManager.draw_ui(screen)      

        pygame.display.update()



class Button:
    #constructor          size = (width, height)    buttonPos_ = (x, y)
    def __init__(self, buttonText_, size_, buttonColor_, buttonPos_, fontSize_, textColor_, isToggle_ = True):
        
        self.buttonText = buttonText_
        self.size = size_
        self.buttonColor = buttonColor_
        self.textColor = textColor_
        self.currentColor = self.buttonColor
        self.buttonPos = buttonPos_
        self.font = pygame.font.Font(None, fontSize_)
        self.middle = (self.buttonPos[0] + (self.size[0] // 2), self.buttonPos[1] + (self.size[1] // 2))

        #if the button color is dark, make the color lighter when pressed
        if self.buttonColor[0] > 75 and self.buttonColor[1] > 75 and self.buttonColor[2] > 75:
            self.buttonColorDark = (self.buttonColor[0]-60, self.buttonColor[1]-60, self.buttonColor[2]-60) 
        else:
            self.buttonColorDark = (self.buttonColor[0]+50, self.buttonColor[1]+50, self.buttonColor[2]+50)

        self.text = self.font.render(self.buttonText, True, self.textColor)
        self.rect = pygame.Rect(self.buttonPos[0], self.buttonPos[1], self.size[0], self.size[1])
        
        self.isPushed = False       #bool that stores if the button has been pushed or not
        self.isToggle = isToggle_   #if true, the button can be clicked once, and it stays active
                                    #if false, can be clicked once, and turns off after click


    def update(self, screen):
        pygame.draw.rect(screen, self.currentColor, self.rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=10)


        self.text = self.font.render(self.buttonText, True, self.textColor)
        #self.rect = pygame.Rect(self.buttonPos[0], self.buttonPos[1], self.size[0], self.size[1], center = self.middle)
        textRect = self.text.get_rect(center = self.middle)

        screen.blit(self.text, textRect)


    #checks if the button has been pressed
    def handleEvent(self, event):
            
            #isTrue becomes true if the button was clicked
            #darkens the button on click
            #the opposite happens when clicked again
            if self.isToggle:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos) and not self.isPushed: #if not pushed
                        self.currentColor = self.buttonColorDark
                        self.isPushed = True
                        return True
                    if self.rect.collidepoint(event.pos) and self.isPushed:   #if pushed again
                        self.currentColor = self.buttonColor
                        self.isPushed = False
                        return False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(event.pos):
                        return True
                    

#call main menu function
MainMenu()







###############################################################3
#old text box class
#can be removed


# class textBox():
#     def __init__(self, uiManager, defaultText, pos_, size_, textboxName, fontSize_ = 40, textColor_ =( 0, 0, 0), borderCol_ = (0, 0, 0)):
#         self.size = size_
#         self.textColor = textColor_
#         self.font = pygame.font.Font(None, fontSize_)
#         self.pos = pos_
#         self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
#         self.borderCol = borderCol_
#         self.isTyping = False
#         #uiManager = uiManager_
#         #self.text = ""
#         self.text = pygame_gui.elements.UITextEntryLine(relative_rect = self.rect, manager=uiManager, object_id = textboxName)
#         #self.textRender = self.font.render(self.text, True, self.textColor)                #the actual text
        

#     #renders the new typed in text on screen
#     def update(self, screen):
#         pygame.draw.rect(screen, (255, 255, 255), self.rect)
#         pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
#         textSurface = self.font.render(self.text, True, self.textColor)
#         screen.blit(textSurface, (self.rect.x + 5, self.rect.y + 2))
#         #self.rect.w = max(100, textSurface.get_width() + 10)

#     #changes what is typed in the box when clicked
#     def handleEvent(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if self.rect.collidepoint(event.pos):
#                 self.isTyping = True
#             else:
#                 self.isTyping = False
        
#         #adds to the text when the textbox is clicked and when you type
#         if event.type == pygame.KEYDOWN and self.isTyping:
#             if event.key == pygame.K_BACKSPACE:
#                 self.text = self.text[:-1]
#             else:
#                 self.text += event.unicode
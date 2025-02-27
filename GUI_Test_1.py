# import multiprocessing
# try:
#     multiprocessing.set_start_method('spawn')
# except RuntimeError:
#     pass

# import matplotlib.pyplot as plt
# import numpy as np
# import pygame
# import pygame_gui
# import sys
# import random
# from multiprocessing import Process

# from Algorithms import BubbleSort, MergeSort, QuickSort, RadixSort, LinearSearch

# # -----------------------------
# # Function: run_visualizer
# # -----------------------------
# def run_visualizer(algo_name, min_val, max_val, num, speed, pause_event):
#     pygame.init()
#     window_size = (1200, 600)
#     window = pygame.display.set_mode(window_size)
#     pygame.display.set_caption(f"{algo_name} Visualizer")
    
#     white   = (255, 255, 255)
#     darkGrey= (84, 84, 84)
#     green   = (193, 255, 114)
#     black   = (0, 0, 0)
    
#     # Create random array.
#     arr = [random.randint(min_val, max_val) for _ in range(num)]
#     if algo_name == "LinearSearch":
#         target = random.choice(arr)
#         print("Linear Search - Array:", arr)
#         print("Linear Search - Target:", target)
    
#     if algo_name == "BubbleSort":
#         generator = BubbleSort(arr)
#     elif algo_name == "MergeSort":
#         generator = MergeSort(arr)
#     elif algo_name == "QuickSort":
#         generator = QuickSort(arr)
#     elif algo_name == "RadixSort":
#         generator = RadixSort(arr)
#     elif algo_name == "LinearSearch":
#         generator = LinearSearch(arr, target)
#     else:
#         print("Unknown algorithm.")
#         return

#     clock = pygame.time.Clock()
#     running = True
#     while running:
#         clock.tick(60)
#         # Check pause_event. While paused, keep processing events.
#         while pause_event.is_set():
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#             pygame.time.delay(100)
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         try:
#             current_arr, swap_indices = next(generator)
#         except StopIteration:
#             running = False
#             break

#         window.fill(white)
#         width, height = window.get_size()
#         bar_width = max(width // len(current_arr), 1)
#         max_val_in_array = max(current_arr) if current_arr else 1
#         font = pygame.font.SysFont(None, 20)
#         for i, val in enumerate(current_arr):
#             bar_height = int((val / max_val_in_array) * (height - 50))
#             x = i * bar_width
#             y = height - bar_height - 30
#             color = green if swap_indices and i in swap_indices else darkGrey
#             pygame.draw.rect(window, color, (x, y, bar_width, bar_height))
#             text_surface = font.render(str(val), True, black)
#             text_rect = text_surface.get_rect(center=(x + bar_width / 2, height - 15))
#             window.blit(text_surface, text_rect)
#         pygame.display.update()
#         pygame.time.delay(speed)
#     pygame.quit()
#     sys.exit()

# # -----------------------------
# # Main GUI Code (Left Panel Only)
# # -----------------------------
# pygame.init()

# # Load the left panel GUI image.
# bg = pygame.image.load("bgNBSVS.png")
# imgScale = 0.91
# gui_width = bg.get_width()
# gui_height = int(bg.get_height() * imgScale)  # Use scaled height

# screen = pygame.display.set_mode((gui_width, gui_height), pygame.RESIZABLE)
# pygame.display.set_caption("Algorithm Visualizer - Main Control")

# clock = pygame.time.Clock()

# black     = (0, 0, 0)
# white     = (255, 255, 255)
# lightgrey = (217, 217, 217)
# darkGrey  = (84, 84, 84)
# green     = (193, 255, 114)

# screen.fill(white)

# theme = {
#     "minText": {"colours": {"dark_bg": "#FFFFFF", "normal_text": "#000000"}},
#     "maxText": {"colours": {"dark_bg": "#FFFFFF", "normal_text": "#000000"}},
#     "numElementsText": {"colours": {"dark_bg": "#FFFFFF", "normal_text": "#000000"}}
# }

# uiManager = pygame_gui.UIManager((gui_width, gui_height), theme)

# ###############################################################################
# # Class: Button (with optional text rendering)
# ###############################################################################
# class Button:
#     def __init__(self, buttonText_, size_, buttonColor_, buttonPos_, fontSize_, textColor_, isToggle_=True, showText=True):
#         self.buttonText = buttonText_
#         self.size = size_
#         self.buttonColor = buttonColor_
#         self.textColor = textColor_
#         self.currentColor = self.buttonColor
#         self.buttonPos = buttonPos_
#         self.font = pygame.font.Font(None, fontSize_)
#         self.middle = (self.buttonPos[0] + self.size[0] // 2, self.buttonPos[1] + self.size[1] // 2)
#         if self.buttonColor[0] > 75 and self.buttonColor[1] > 75 and self.buttonColor[2] > 75:
#             self.buttonColorDark = (self.buttonColor[0] - 60, self.buttonColor[1] - 60, self.buttonColor[2] - 60)
#         else:
#             self.buttonColorDark = (self.buttonColor[0] + 50, self.buttonColor[1] + 50, self.buttonColor[2] + 50)
#         self.text = self.font.render(self.buttonText, True, self.textColor)
#         self.rect = pygame.Rect(self.buttonPos[0], self.buttonPos[1], self.size[0], self.size[1])
#         self.isPushed = False
#         self.isToggle = isToggle_
#         self.showText = showText
    
#     def update(self, surface):
#         pygame.draw.rect(surface, self.currentColor, self.rect, border_radius=10)
#         pygame.draw.rect(surface, (0, 0, 0), self.rect, 2, border_radius=10)
#         if self.showText:
#             self.text = self.font.render(self.buttonText, True, self.textColor)
#             textRect = self.text.get_rect(center=self.middle)
#             surface.blit(self.text, textRect)
    
#     def handleEvent(self, event):
#         if self.isToggle:
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if self.rect.collidepoint(event.pos) and not self.isPushed:
#                     self.currentColor = self.buttonColorDark
#                     self.isPushed = True
#                     return True
#                 if self.rect.collidepoint(event.pos) and self.isPushed:
#                     self.currentColor = self.buttonColor
#                     self.isPushed = False
#                     return False
#         else:
#             if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
#                 return True

# ###############################################################################
# # Function: MainMenu (Main control GUI for left panel only)
# ###############################################################################
# def MainMenu():
#     global min_value, max_value, num_elements, speed

#     # Default parameters.
#     min_value = "0"
#     max_value = "100"
#     num_elements = "50"
#     speed = 75

#     # Global lists to store pending selections and spawned processes.
#     pending_algorithms = []  # List of algorithm names selected.
#     processes = []           # List of Process objects.
#     pause_event = multiprocessing.Event()
#     pause_event.set()   # Initially paused.

#     # GUI layout.
#     buttonSize = (20, 20)
#     buttonColor = white
#     bX = 40 * imgScale
#     bY = 325 * imgScale
#     spaceFac = 37 * imgScale

#     # Create algorithm selection buttons (no text).
#     bubbleSortButton   = Button("Bubble",   buttonSize, buttonColor, (bX, bY),                   20, black, showText=False)
#     mergeSortButton    = Button("Merge",    buttonSize, buttonColor, (bX, bY + spaceFac),          20, black, showText=False)
#     quickSortButton    = Button("Quick",    buttonSize, buttonColor, (bX, bY + spaceFac * 2),      20, black, showText=False)
#     radixSortButton    = Button("Radix",    buttonSize, buttonColor, (bX, bY + spaceFac * 3),      20, black, showText=False)
#     linearSearchButton = Button("Search",   buttonSize, buttonColor, (bX, bY + spaceFac * 4),      20, black, showText=False)

#     # Create analysis/running buttons (no text for runtime/space).
#     runtimeButton = Button("RunTime", buttonSize, buttonColor, (230 * imgScale, 365 * imgScale), 20, black, showText=False)
#     spaceButton   = Button("Space",   buttonSize, buttonColor, (230 * imgScale, 410 * imgScale), 20, black, showText=False)
#     # Control buttons (with text).
#     controlButtonSize = (200 * imgScale, 65 * imgScale)
#     resetButton   = Button("Reset",     controlButtonSize, buttonColor, (90 * imgScale, 700 * imgScale), 40, black, False, showText=True)
#     # For the Start/Stop button, set isToggle to False so that each press registers once.
#     startButton   = Button("Start/Stop", controlButtonSize, buttonColor, (90 * imgScale, 800 * imgScale), 40, black, isToggle_=False, showText=True)
#     graphButtonSize = (140 * imgScale, 40 * imgScale)
#     lineGraphButton = Button("Line",     graphButtonSize, buttonColor, (40 * imgScale, 999 * imgScale), 25, black, False, showText=True)
#     barGraphButton  = Button("Bar",      graphButtonSize, buttonColor, (200 * imgScale, 999 * imgScale), 25, black, False, showText=True)

#     buttonArray = [bubbleSortButton, mergeSortButton, quickSortButton,
#                    radixSortButton, linearSearchButton, runtimeButton,
#                    spaceButton, resetButton, startButton, lineGraphButton,
#                    barGraphButton]

#     textBoxRectWidth = 70 * imgScale
#     textBoxRectHeight = 40 * imgScale
#     minTextBox = pygame_gui.elements.UITextEntryLine(
#         relative_rect=pygame.Rect(100 * imgScale, 85 * imgScale, textBoxRectWidth, textBoxRectHeight),
#         manager=uiManager, object_id="minText")
#     maxTextBox = pygame_gui.elements.UITextEntryLine(
#         relative_rect=pygame.Rect(280 * imgScale, 85 * imgScale, textBoxRectWidth, textBoxRectHeight),
#         manager=uiManager, object_id="maxText")
#     numElementsTextBox = pygame_gui.elements.UITextEntryLine(
#         relative_rect=pygame.Rect(210 * imgScale, 152 * imgScale, textBoxRectWidth, textBoxRectHeight),
#         manager=uiManager, object_id="numElementsText")

#     minTextBox.set_text(min_value)
#     maxTextBox.set_text(max_value)
#     numElementsTextBox.set_text(num_elements)

#     sX = 10 * imgScale
#     sY = 648 * imgScale
#     slider = pygame_gui.elements.UIHorizontalSlider(
#         relative_rect=pygame.Rect(sX, sY, 360 * imgScale, 20 * imgScale),
#         start_value=75, value_range=[100, 0], manager=uiManager)

#     while True:
#         dt = clock.tick(24) / 1000.0
#         events = pygame.event.get()

#         for event in events:
#             if event.type == pygame.QUIT:
#                 # Terminate all spawned processes.
#                 for proc in processes:
#                     proc.terminate()
#                 pygame.quit()
#                 sys.exit()
            
#             uiManager.process_events(event)
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 minTextBox.set_text(min_value)
#                 maxTextBox.set_text(max_value)
#                 numElementsTextBox.set_text(num_elements)
                
#                 # Toggle algorithm selection instead of immediate spawning.
#                 if bubbleSortButton.handleEvent(event):
#                     if "BubbleSort" not in pending_algorithms:
#                         pending_algorithms.append("BubbleSort")
#                         print("BubbleSort selected.")
#                     else:
#                         pending_algorithms.remove("BubbleSort")
#                         print("BubbleSort deselected.")
                
#                 elif mergeSortButton.handleEvent(event):
#                     if "MergeSort" not in pending_algorithms:
#                         pending_algorithms.append("MergeSort")
#                         print("MergeSort selected.")
#                     else:
#                         pending_algorithms.remove("MergeSort")
#                         print("MergeSort deselected.")
                
#                 elif quickSortButton.handleEvent(event):
#                     if "QuickSort" not in pending_algorithms:
#                         pending_algorithms.append("QuickSort")
#                         print("QuickSort selected.")
#                     else:
#                         pending_algorithms.remove("QuickSort")
#                         print("QuickSort deselected.")
                
#                 elif radixSortButton.handleEvent(event):
#                     if "RadixSort" not in pending_algorithms:
#                         pending_algorithms.append("RadixSort")
#                         print("RadixSort selected.")
#                     else:
#                         pending_algorithms.remove("RadixSort")
#                         print("RadixSort deselected.")
                
#                 elif linearSearchButton.handleEvent(event):
#                     if "LinearSearch" not in pending_algorithms:
#                         pending_algorithms.append("LinearSearch")
#                         print("LinearSearch selected.")
#                     else:
#                         pending_algorithms.remove("LinearSearch")
#                         print("LinearSearch deselected.")
                
#                 # Other buttons.
#                 elif runtimeButton.handleEvent(event):
#                     print("runtime")
#                 elif spaceButton.handleEvent(event):
#                     print("space")
#                 elif resetButton.handleEvent(event):
#                     print("Reset pressed")
#                 # Start/Stop button: if there are pending algorithms and no processes, spawn them.
#                 elif startButton.handleEvent(event):
#                     if not processes and pending_algorithms:
#                         # Spawn a visualizer for each pending algorithm.
#                         for algo in pending_algorithms:
#                             m_val = int(min_value)
#                             M_val = int(max_value)
#                             n = int(num_elements)
#                             p = Process(target=run_visualizer, args=(algo, m_val, M_val, n, speed, pause_event))
#                             p.start()
#                             processes.append(p)
#                         pending_algorithms.clear()
#                         # Now resume running by clearing the pause event.
#                         pause_event.clear()
#                         print("Visualizers started and running.")
#                     else:
#                         # Toggle pause/resume for all visualizers.
#                         if pause_event.is_set():
#                             pause_event.clear()
#                             print("Resumed all visualizers.")
#                         else:
#                             pause_event.set()
#                             print("Paused all visualizers.")
                
#                 elif lineGraphButton.handleEvent(event):
#                     print("Line graph button pressed")
#                 elif barGraphButton.handleEvent(event):
#                     print("Bar graph button pressed")
            
#             if event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
#                 if event.ui_object_id == "minText":
#                     min_value = event.text or "0"
#                 if event.ui_object_id == "maxText":
#                     max_value = event.text or "100"
#                 if event.ui_object_id == "numElementsText":
#                     num_elements = event.text or "50"
            
#             if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
#                 speed = event.value

#         uiManager.update(dt)
#         screen.fill(lightgrey)
#         screen.blit(bg, (0, 0))
#         uiManager.draw_ui(screen)
#         for btn in buttonArray:
#             btn.update(screen)
        
#         pygame.display.update()

# if __name__ == '__main__':
#     MainMenu()










# ###############################################################
# #old text box class
# #can be removed


# # class textBox():
# #     def __init__(self, uiManager, defaultText, pos_, size_, textboxName, fontSize_ = 40, textColor_ =( 0, 0, 0), borderCol_ = (0, 0, 0)):
# #         self.size = size_
# #         self.textColor = textColor_
# #         self.font = pygame.font.Font(None, fontSize_)
# #         self.pos = pos_
# #         self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
# #         self.borderCol = borderCol_
# #         self.isTyping = False
# #         #uiManager = uiManager_
# #         #self.text = ""
# #         self.text = pygame_gui.elements.UITextEntryLine(relative_rect = self.rect, manager=uiManager, object_id = textboxName)
# #         #self.textRender = self.font.render(self.text, True, self.textColor)                #the actual text
        

# #     #renders the new typed in text on screen
# #     def update(self, screen):
# #         pygame.draw.rect(screen, (255, 255, 255), self.rect)
# #         pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
# #         textSurface = self.font.render(self.text, True, self.textColor)
# #         screen.blit(textSurface, (self.rect.x + 5, self.rect.y + 2))
# #         #self.rect.w = max(100, textSurface.get_width() + 10)

# #     #changes what is typed in the box when clicked
# #     def handleEvent(self, event):
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             if self.rect.collidepoint(event.pos):
# #                 self.isTyping = True
# #             else:
# #                 self.isTyping = False
        
# #         #adds to the text when the textbox is clicked and when you type
# #         if event.type == pygame.KEYDOWN and self.isTyping:
# #             if event.key == pygame.K_BACKSPACE:
# #                 self.text = self.text[:-1]
# #             else:
# #                 self.text += event.unicode
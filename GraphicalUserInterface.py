import sys
import time
import random
import pygame
import pygame_gui
from Algorithms import BubbleSort, MergeSort, QuickSort, RadixSort, LinearSearch

# Colors
WHITE     = (255, 255, 255)
LIGHTGREY = (217, 217, 217)
DARKGREY  = (84, 84, 84)
GREEN     = (193, 255, 114)
BLACK     = (0, 0, 0)

class VisualizerApp:
    def __init__(self):
        pygame.init()
        self.window_size = (1200, 600)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
        pygame.display.set_caption("Algorithm Visualizer")

        # Split window: left control panel (300px wide) and right visualization area.
        self.control_width = 300
        self.control_rect = pygame.Rect(0, 0, self.control_width, self.window_size[1])
        self.visualizer_rect = pygame.Rect(self.control_width, 0, self.window_size[0] - self.control_width, self.window_size[1])
        self.clock = pygame.time.Clock()

        self.ui_manager = pygame_gui.UIManager(self.window_size)
        self.setup_controls()
        self.reset_visualizer_state()

    def setup_controls(self):
        # Create labels and text entry fields for parameters.
        # Lower Bound
        self.lower_bound_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(20, 20, 120, 30),
            text="Lower Bound",
            manager=self.ui_manager)
        self.min_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(150, 20, 100, 30),
            manager=self.ui_manager)
        self.min_input.set_text("0")

        # Upper Bound
        self.upper_bound_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(20, 60, 120, 30),
            text="Upper Bound",
            manager=self.ui_manager)
        self.max_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(150, 60, 100, 30),
            manager=self.ui_manager)
        self.max_input.set_text("100")

        # Number of Elements
        self.num_elements_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(20, 100, 120, 30),
            text="# Of Elements",
            manager=self.ui_manager)
        self.num_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(150, 100, 100, 30),
            manager=self.ui_manager)
        self.num_input.set_text("25")

        # Speed slider: higher value gives faster updates.
        self.speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(20, 140, 200, 30),
            start_value=75,
            value_range=(1, 100),
            manager=self.ui_manager)

        # Dropdown to select algorithm.
        self.algo_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["BubbleSort", "MergeSort", "QuickSort", "RadixSort", "LinearSearch"],
            starting_option="BubbleSort",
            relative_rect=pygame.Rect(20, 180, 150, 30),
            manager=self.ui_manager)

        # Start/Stop button.
        self.start_stop_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 230, 100, 40),
            text="Start",
            manager=self.ui_manager)

        # Reset button.
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 280, 100, 40),
            text="Reset",
            manager=self.ui_manager)

    def reset_visualizer_state(self):
        # Clear the current algorithm state.
        self.algo_generator = None
        self.current_array = []
        self.swap_indices = None
        self.running_algo = False
        self.last_update_time = time.time()
        self.speed_delay = 1.0 / self.speed_slider.get_current_value()

    def initialize_algorithm(self):
        # Get parameters from the UI.
        try:
            min_val = int(self.min_input.get_text())
            max_val = int(self.max_input.get_text())
            num = int(self.num_input.get_text())
        except ValueError:
            min_val, max_val, num = 0, 100, 25

        arr = [random.randint(min_val, max_val) for _ in range(num)]
        algo_name = self.algo_dropdown.selected_option[0].strip()
        print("Algorithm set to:", repr(algo_name))  # Debug output

        # For LinearSearch, choose a target.
        if algo_name == "LinearSearch":
            target = random.choice(arr)
            print("LinearSearch - Array:", arr)
            print("LinearSearch - Target:", target)

        if algo_name == "BubbleSort":
            self.algo_generator = BubbleSort(arr)
        elif algo_name == "MergeSort":
            self.algo_generator = MergeSort(arr)
        elif algo_name == "QuickSort":
            self.algo_generator = QuickSort(arr)
        elif algo_name == "RadixSort":
            self.algo_generator = RadixSort(arr)
        elif algo_name == "LinearSearch":
            self.algo_generator = LinearSearch(arr, target)
        else:
            print("Unknown algorithm:", repr(algo_name))
            self.algo_generator = None

        self.current_array = arr
        self.running_algo = True
        self.last_update_time = time.time()
        self.speed_delay = 1.0 / self.speed_slider.get_current_value()

    def update_visualization(self):
        if self.algo_generator and self.running_algo:
            current_time = time.time()
            if current_time - self.last_update_time >= self.speed_delay:
                try:
                    self.current_array, self.swap_indices = next(self.algo_generator)
                except StopIteration:
                    # When finished, reset the generator.
                    self.running_algo = False
                    self.algo_generator = None
                    self.start_stop_button.set_text("Start")
                self.last_update_time = current_time

    def draw_visualization(self):
        # Draw the algorithm state in the right panel.
        viz_surface = self.screen.subsurface(self.visualizer_rect)
        viz_surface.fill(LIGHTGREY)

        if not self.current_array:
            return

        width = self.visualizer_rect.width
        height = self.visualizer_rect.height
        n = len(self.current_array)
        bar_width = max(width // n, 1)
        max_val = max(self.current_array) if self.current_array else 1

        font = pygame.font.SysFont(None, 20)
        for i, val in enumerate(self.current_array):
            bar_height = int((val / max_val) * (height - 30))
            x = i * bar_width
            y = height - bar_height
            color = GREEN if (self.swap_indices and i in self.swap_indices) else DARKGREY
            pygame.draw.rect(viz_surface, color, (x, y, bar_width, bar_height))
            text_surface = font.render(str(val), True, BLACK)
            text_rect = text_surface.get_rect(center=(x + bar_width / 2, y - 10))
            viz_surface.blit(text_surface, text_rect)

    def run(self):
        while True:
            time_delta = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.ui_manager.process_events(event)

                # Handle dropdown changes.
                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED and event.ui_element == self.algo_dropdown:
                    print("Dropdown changed to:", event.text.strip())

                # Handle button presses.
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.start_stop_button:
                        # If not running, initialize and start immediately.
                        if not self.running_algo:
                            if self.algo_generator is None:
                                self.initialize_algorithm()
                            self.running_algo = True
                            self.start_stop_button.set_text("Stop")
                        else:
                            # If running, stop.
                            self.running_algo = False
                            self.start_stop_button.set_text("Start")
                    elif event.ui_element == self.reset_button:
                        self.reset_visualizer_state()
                        self.start_stop_button.set_text("Start")

                # Update the speed delay if the slider moves.
                if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED and event.ui_element == self.speed_slider:
                    self.speed_delay = 1.0 / self.speed_slider.get_current_value()

            self.ui_manager.update(time_delta)
            self.update_visualization()

            self.screen.fill(BLACK)
            pygame.draw.rect(self.screen, BLACK, self.control_rect)
            self.ui_manager.draw_ui(self.screen)
            self.draw_visualization()
            pygame.display.update()

if __name__ == '__main__':
    app = VisualizerApp()
    app.run()

import sys
import time
import random
import pygame
import pygame_gui
import matplotlib.pyplot as plt
from multiprocessing import freeze_support
import sys

from Algorithms import BubbleSort, MergeSort, QuickSort, RadixSort, LinearSearch
from noYieldAlgorithms import BubbleSortNoYield, MergeSortNoYield, QuickSortNoYield, RadixSortNoYield, LinearSearchNoYield

# Colors
WHITE     = (255, 255, 255)
LIGHTGREY = (217, 217, 217)
DARKGREY  = (60, 60, 60)
GREEN     = (193, 255, 114)
BLACK     = (0, 0, 0)

# Big-O labels for multi-run plots
BIG_O = {
    "BubbleSort":   {"Time": "O(n^2)",     "Space": "O(1)"},
    "MergeSort":    {"Time": "O(n log n)", "Space": "O(n)"},
    "QuickSort":    {"Time": "O(n log n)*","Space": "O(log n)"},
    "RadixSort":    {"Time": "O(nk)",      "Space": "O(n)"},
    "LinearSearch": {"Time": "O(n)",       "Space": "O(1)"}
}

def BenchmarkAllAlgorithms(min_val, max_val):
    startBenchmarkTime = time.time()
    algorithms = ["BubbleSort", "MergeSort", "QuickSort", "RadixSort", "LinearSearch"]
    n_values = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000]
    results = {}
    
    for algo in algorithms:
        results[algo] = {"times": [], "mems": []}
        for n in n_values:
            iteration_times = []
            iterations = 0
            start_benchmark = time.perf_counter()
            while time.perf_counter() - start_benchmark < 0.01:
                # Generate a new random array for each run.
                arr = [random.randint(min_val, max_val) for _ in range(n)]
                start_time = time.perf_counter()
                if algo == "LinearSearch":
                    # Pick a random target.
                    target = random.choice(arr) if arr else 0
                    LinearSearchNoYield(arr, target)
                elif algo == "BubbleSort":
                    # Pass a copy so that the original array remains unsorted.
                    BubbleSortNoYield(arr.copy())
                elif algo == "MergeSort":
                    MergeSortNoYield(arr.copy())
                elif algo == "QuickSort":
                    QuickSortNoYield(arr.copy())
                elif algo == "RadixSort":
                    RadixSortNoYield(arr.copy())
                elapsed = time.perf_counter() - start_time
                iteration_times.append(elapsed)
                iterations += 1
            # Compute the average time per call for this input size.
            average_time = sum(iteration_times) / len(iteration_times) if iteration_times else 0
            mem_usage = sys.getsizeof(arr)
            results[algo]["times"].append(average_time)
            results[algo]["mems"].append(mem_usage)
            print(f"{algo}, n={n}, avg_time={average_time:.8f}s over {iterations} iterations, original array mem={mem_usage}")
    endBenchmarkTime = time.time()
    totalTime = endBenchmarkTime - startBenchmarkTime 
    print(f"Total Benchmark Time: {totalTime:.8f}s")
    return n_values, results

def PlotAllAlgorithmsComplexity(n_values, results, metric="Time"):
    #Plots the chosen complexity metric (either "Time" or "Space") for all algorithms on one graph.

    plt.figure()
    for algo, data in results.items():
        if metric == "Time":
            plt.plot(n_values, data["times"], marker='o',
                     label=f"{algo} ({BIG_O.get(algo,{}).get('Time','')})")
        else:
            plt.plot(n_values, data["mems"], marker='o',
                     label=f"{algo} ({BIG_O.get(algo,{}).get('Space','')})")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("n (array size)")
    if metric == "Time":
        plt.ylabel("Runtime (s)")
        plt.title("Time Complexity Comparison")
    else:
        plt.ylabel("Memory Usage (bytes)")
        plt.title("Space Complexity Comparison")
    plt.legend(loc="upper left")
    plt.show()

class VisualizerApp:
    def __init__(self):
        pygame.init()
        self.window_size = (1200, 600)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        
        # Split window: left control panel (300px wide) and right visualization area.
        self.control_width = 300
        self.control_rect = pygame.Rect(0, 0, self.control_width, self.window_size[1])
        self.visualizer_rect = pygame.Rect(self.control_width, 0, self.window_size[0]-self.control_width, self.window_size[1])
        
        self.ui_manager = pygame_gui.UIManager(self.window_size)
        self.SetUpUI()
        
        self.ResetSingleRunState()
        self.running_algo = False
        self.paused = False
        self.selected_algo = None

    def ResetSingleRunState(self):
        self.algo_generator = None
        self.current_array = []
        self.swap_indices = None
        self.last_update_time = time.time()
        try:
            self.speed_delay = 1.0 / float(self.speed_slider.get_current_value())
        except:
            self.speed_delay = 0.02
        self.iteration_counts = []
        self.times = []
        self.mem_usage = []
        self.iter_count = 0

    def SetUpUI(self):
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
        
        # Speed slider.
        self.speed_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(20, 140, 200, 30),
            start_value=75,
            value_range=(1, 100),
            manager=self.ui_manager)
        
        # Dropdown for algorithm selection.
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
        
        # Analyze Big-O button (all algorithms)
        self.analyze_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 330, 120, 40),
            text="Analyze Big-O",
            manager=self.ui_manager)

    def InitializeAlgorithm(self):
        try:
            min_val = int(self.min_input.get_text())
            max_val = int(self.max_input.get_text())
            num = int(self.num_input.get_text())
        except ValueError:
            min_val, max_val, num = 0, 100, 25
        arr = [random.randint(min_val, max_val) for _ in range(num)]
        algo_name = self.algo_dropdown.selected_option[0].strip()
        self.selected_algo = algo_name
        print("Algorithm set to:", repr(algo_name))
        if algo_name == "LinearSearch":
            target = random.choice(arr)
            print("LinearSearch - Array:", arr)
            print("LinearSearch - Target:", target)
            self.algo_generator = LinearSearch(arr, target)
        elif algo_name == "BubbleSort":
            self.algo_generator = BubbleSort(arr)
        elif algo_name == "MergeSort":
            self.algo_generator = MergeSort(arr)
        elif algo_name == "QuickSort":
            self.algo_generator = QuickSort(arr)
        elif algo_name == "RadixSort":
            self.algo_generator = RadixSort(arr)
        else:
            print("Unknown algorithm:", repr(algo_name))
            self.algo_generator = None
        self.current_array = arr
        self.running_algo = True
        self.paused = False
        self.last_update_time = time.time()
        self.speed_delay = 1.0 / float(self.speed_slider.get_current_value())
        self.iteration_counts = []
        self.times = []
        self.mem_usage = []
        self.iter_count = 0

    def UpdateVisualization(self):
        if self.algo_generator and self.running_algo and not self.paused:
            current_time = time.time()
            if current_time - self.last_update_time >= self.speed_delay:
                try:
                    self.current_array, self.swap_indices = next(self.algo_generator)
                except StopIteration:
                    self.running_algo = False
                    self.algo_generator = None
                    self.start_stop_button.set_text("Start")
                    # Do not pop up complexities plot for single-run mode.
                    return
                dt = current_time - self.last_update_time
                self.times.append(dt)
                self.iter_count += 1
                self.iteration_counts.append(self.iter_count)
                self.mem_usage.append(sys.getsizeof(self.current_array))
                self.last_update_time = current_time

    def DrawVisualization(self):
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
            text_rect = text_surface.get_rect(center=(x + bar_width/2, y - 10))
            viz_surface.blit(text_surface, text_rect)
    
    def BenchmarkAllAlgorithms(self, min_val, max_val):
        return BenchmarkAllAlgorithms(min_val, max_val)

    def PlotAllAlgorithmsComplexity(self, n_values, results):
        PlotAllAlgorithmsComplexity(n_values, results)

    # def BenchmarkMultiRun(self, algo_name, min_val, max_val):
    #     # Old function for benchmarking only one algorithm
    #     n_values = [1, 10, 100, 1000, 10000]
    #     times = []
    #     mems = []
    #     for n in n_values:
    #         arr = [random.randint(min_val, max_val) for _ in range(n)]
    #         start_time = time.time()
    #         if algo_name == "LinearSearch":
    #             if arr:
    #                 target = random.choice(arr)
    #             else:
    #                 target = 0
    #             from noYieldAlgorithms import LinearSearchNoYield
    #             LinearSearchNoYield(arr, target)
    #         else:
    #             if algo_name == "BubbleSort":
    #                 from noYieldAlgorithms import BubbleSortNoYield as func
    #             elif algo_name == "MergeSort":
    #                 from noYieldAlgorithms import MergeSortNoYield as func
    #             elif algo_name == "QuickSort":
    #                 from noYieldAlgorithms import QuickSortNoYield as func
    #             elif algo_name == "RadixSort":
    #                 from noYieldAlgorithms import RadixSortNoYield as func
    #             else:
    #                 print("Unknown algorithm for multi-run:", algo_name)
    #                 return
    #             func(arr)
    #         total_time = time.time() - start_time
    #         mem_usage = sys.getsizeof(arr)
    #         times.append(total_time)
    #         mems.append(mem_usage)
    #         print(f"{algo_name}, n={n}, time={total_time:.5f}s, mem={mem_usage}")
    #     PlotMultiRunResults(algo_name, n_values, times, mems)
    
    def Run(self):
        self.visualizer_rect = pygame.Rect(self.control_width, 0, self.window_size[0]-self.control_width, self.window_size[1])
        
        while True:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.ui_manager.process_events(event)
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.start_stop_button:
                        if not self.running_algo:
                            self.InitializeAlgorithm()
                            self.start_stop_button.set_text("Stop")
                        else:
                            self.paused = not self.paused
                            if self.paused:
                                self.start_stop_button.set_text("Start")
                                print("Paused.")
                            else:
                                self.start_stop_button.set_text("Stop")
                                print("Resumed.")
                    elif event.ui_element == self.reset_button:
                        self.ResetSingleRunState()
                        self.running_algo = False
                        self.start_stop_button.set_text("Start")
                        # Clear the visualization area.
                        viz_surface = self.screen.subsurface(self.visualizer_rect)
                        viz_surface.fill(LIGHTGREY)
                        pygame.display.update()
                        # Close any open matplotlib windows.
                        plt.close('all')
                    elif event.ui_element == self.analyze_button:
                        try:
                            min_val = int(self.min_input.get_text())
                            max_val = int(self.max_input.get_text())
                        except ValueError:
                            min_val, max_val = 0, 100
                        n_values, results = self.BenchmarkAllAlgorithms(min_val, max_val)
                        self.PlotAllAlgorithmsComplexity(n_values, results)
                
                if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED and event.ui_element == self.speed_slider:
                    self.speed_delay = 1.0 / float(self.speed_slider.get_current_value())
            
            self.ui_manager.update(time_delta)
            pygame.draw.rect(self.screen, DARKGREY, self.control_rect)
            self.ui_manager.draw_ui(self.screen)
            if self.running_algo:
                self.UpdateVisualization()
                self.DrawVisualization()
            pygame.display.update()

def RunGUI():
    freeze_support()
    app = VisualizerApp()
    app.Run()

if __name__ == '__main__':
    RunGUI()

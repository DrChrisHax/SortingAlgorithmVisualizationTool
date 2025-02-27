import sys
import random
import time
import pygame
import pygame_gui
import matplotlib.pyplot as plt

from AlgorithmsNoYield import BubbleSort, MergeSort, QuickSort, RadixSort, LinearSearch

# Colors
DARKGREY = (84, 84, 84)

# For labeling big-O in the legend
BIG_O = {
    "BubbleSort":   {"Time": "O(n^2)",     "Space": "O(1)"},
    "MergeSort":    {"Time": "O(n log n)", "Space": "O(n)"},
    "QuickSort":    {"Time": "O(n log n)*","Space": "O(log n)"},
    "RadixSort":    {"Time": "O(nk)",      "Space": "O(n)"},
    "LinearSearch": {"Time": "O(n)",       "Space": "O(1)"}
}

class MultipleNApp:
    def __init__(self):
        pygame.init()
        self.window_size = (800, 400)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Multiple-n Benchmark")
        self.clock = pygame.time.Clock()
        
        self.ui_manager = pygame_gui.UIManager(self.window_size)
        self.setup_ui()
    
    def setup_ui(self):
        # Dropdown for algorithm selection
        self.algo_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["BubbleSort", "MergeSort", "QuickSort", "RadixSort", "LinearSearch"],
            starting_option="BubbleSort",
            relative_rect=pygame.Rect(20, 20, 150, 30),
            manager=self.ui_manager
        )
        # Start button
        self.start_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 70, 100, 40),
            text="Start",
            manager=self.ui_manager
        )
        # Min/Max labels for random range
        self.min_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(200, 20, 60, 30),
            text="MinVal",
            manager=self.ui_manager
        )
        self.min_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(270, 20, 80, 30),
            manager=self.ui_manager
        )
        self.min_input.set_text("0")
        self.max_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(200, 70, 60, 30),
            text="MaxVal",
            manager=self.ui_manager
        )
        self.max_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(270, 70, 80, 30),
            manager=self.ui_manager
        )
        self.max_input.set_text("999")
    
    def run_algorithm_no_visual(self, algo_name, arr):
        """
        Runs the chosen algorithm in-place on 'arr', measuring total time.
        Returns (runtime, memoryUsage).
        """
        start_time = time.time()
        
        if algo_name == "BubbleSort":
            BubbleSort(arr)
        elif algo_name == "MergeSort":
            MergeSort(arr)
        elif algo_name == "QuickSort":
            QuickSort(arr)
        elif algo_name == "RadixSort":
            RadixSort(arr)
        elif algo_name == "LinearSearch":
            # For searching, pick a random target from arr (if not empty).
            if arr:
                target = random.choice(arr)
            else:
                target = 0
            LinearSearch(arr, target)
        else:
            print("Unknown algorithm:", algo_name)
        
        total_time = time.time() - start_time
        mem_usage = sys.getsizeof(arr)
        return total_time, mem_usage
    
    def benchmark_across_n(self, algo_name, min_val, max_val):
        """
        Runs the selected algorithm across multiple n values, collecting total runtime and memory usage.
        """
        n_values = [10, 20, 40, 80, 160, 320, 640]
        times = []
        mems = []
        
        for n in n_values:
            arr = [random.randint(min_val, max_val) for _ in range(n)]
            t, m = self.run_algorithm_no_visual(algo_name, arr)
            times.append(t)
            mems.append(m)
            print(f"{algo_name}: n={n}, time={t:.5f}s, mem={m} bytes")
        
        # Plot the results
        self.plot_results(algo_name, n_values, times, mems)
    
    def plot_results(self, algo_name, n_values, times, mems):
        plt.figure()
        
        # Plot times with dot markers
        plt.plot(n_values, times, 'b-o', label=f"Time {BIG_O.get(algo_name, {}).get('Time','')}")
        
        # We'll plot memory usage on a secondary y-axis
        ax1 = plt.gca()
        ax2 = ax1.twinx()
        ax2.plot(n_values, mems, 'r-o', label=f"Space {BIG_O.get(algo_name, {}).get('Space','')}")
        
        ax1.set_xlabel("n (array size)")
        ax1.set_ylabel("Runtime (s)", color='b')
        ax2.set_ylabel("Memory Usage (bytes)", color='r')
        plt.title("Complexities")
        
        # Combine legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")
        
        plt.show()
    
    def run(self):
        running = True
        while running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                self.ui_manager.process_events(event)
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.start_button:
                        algo_name = self.algo_dropdown.selected_option[0].strip()
                        try:
                            min_val = int(self.min_input.get_text())
                            max_val = int(self.max_input.get_text())
                        except ValueError:
                            min_val, max_val = 0, 999
                        
                        self.benchmark_across_n(algo_name, min_val, max_val)
            
            self.ui_manager.update(time_delta)
            self.screen.fill(DARKGREY)
            self.ui_manager.draw_ui(self.screen)
            pygame.display.update()
        
        pygame.quit()

if __name__ == "__main__":
    app = MultipleNApp()
    app.run()

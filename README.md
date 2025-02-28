# Algorithm Visualizer and Complexity Analysis Tool

An interactive Python-based tool to visualize sorting algorithms and analyze their runtime and space complexities through both step-by-step visualizations and multi-run benchmarking.

## Overview

This project provides:
- **Step-by-step Visualization:**  
  A graphical interface that displays the inner workings of popular sorting algorithms in real time.
- **Performance Analysis:**  
  A benchmarking mode that runs the algorithm on multiple input sizes and plots runtime and memory usage graphs (with Big-O annotations) using Matplotlib.
- **Interactive Controls:**  
  A user-friendly control panel (using `pygame` and `pygame_gui`) to select algorithms, set parameters (lower/upper bound, number of elements, speed), and start, pause, or reset the visualization.

## Features

- **Supported Algorithms:**  
  - Bubble Sort  
  - Merge Sort  
  - Quick Sort  
  - Radix Sort  
  - Linear Search (for demonstration)

- **Visualization Modes:**  
  - **Single-Run Mode:**  
    Step-by-step visualization using generator-based implementations.
  - **Multi-Run Benchmark Mode:**  
    Measures total runtime and memory usage across a range of input sizes and displays a complexity plot.

- **Graphical User Interface:**  
  The main window is split into two sections:  
  - **Left Panel:** Control panel for user inputs.  
  - **Right Panel:** Real-time visualization of the algorithm's execution.

## Files Structure

- **algorithms.py**  
  Contains generator-based versions of the sorting and searching algorithms for real-time visualization.

- **noYieldAlgorithms.py**  
  Contains non-generator versions of the algorithms used for multi-run benchmarking (to measure total runtime and memory usage).

- **GUI.py**  
  Contains the main GUI application which integrates the control panel, single-run visualization, and multi-run benchmarking features.

## Requirements

- Python 3.10+
- [Pygame](https://www.pygame.org/) (tested with pygame-ce 2.5.3)
- [pygame_gui](https://pygame-gui.readthedocs.io/)
- [Matplotlib](https://matplotlib.org/)
- Other standard libraries: `time`, `random`, `math`, `sys`, `multiprocessing`

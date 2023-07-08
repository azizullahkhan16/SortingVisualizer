import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
from window.ConfigWindow import ConfigWindow
import numpy as np


class AnalysisSpace(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg="#000000")
        # Add your analysis space widgets and layout here

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def quick_sort(self, arr, low, high):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        if low < high:
            pivot_index = partition(arr, low, high)
            self.quick_sort(arr, low, pivot_index - 1)
            self.quick_sort(arr, pivot_index + 1, high)

    def tim_sort(self, arr):

        def insertion_sort(arr, left=0, right=None):
            if right is None:
                right = len(arr) - 1

            for i in range(left + 1, right + 1):
                key_item = arr[i]
                j = i - 1
                while j >= left and arr[j] > key_item:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key_item

        def merge(arr, left, mid, right):
            len1 = mid - left + 1
            len2 = right - mid

            left_arr = arr[left:mid + 1]
            right_arr = arr[mid + 1:right + 1]

            i = j = 0
            k = left

            while i < len1 and j < len2:
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len1:
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len2:
                arr[k] = right_arr[j]
                j += 1
                k += 1

        min_run = 32
        n = len(arr)

        for i in range(0, n, min_run):
            insertion_sort(arr, i, min((i + min_run - 1), n - 1))

        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = min((start + size - 1), (n - 1))
                end = min((start + size * 2 - 1), (n - 1))
                merge(arr, start, mid, end)
            size *= 2

    def heap_sort(self, arr):
        n = len(arr)

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[i] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    def radix_sort(self, arr):
        if len(arr) > 1:
            max_num = max(arr)

            def counting_sort(arr, exp):
                n = len(arr)
                output = [0] * n
                count = [0] * 10

                for i in range(n):
                    index = arr[i] // exp
                    count[index % 10] += 1

                for i in range(1, 10):
                    count[i] += count[i - 1]

                i = n - 1
                while i >= 0:
                    index = arr[i] // exp
                    output[count[index % 10] - 1] = arr[i]
                    count[index % 10] -= 1
                    i -= 1

                for i in range(n):
                    arr[i] = output[i]

            exp = 1
            while max_num // exp > 0:
                counting_sort(arr, exp)
                exp *= 10

    def counting_sort(self, arr):
        if len(arr) > 0:
            max_val = max(arr)
            count = [0] * (max_val + 1)

            for num in arr:
                count[num] += 1

            for i in range(1, len(count)):
                count[i] += count[i - 1]

            sorted_arr = [0] * len(arr)
            for num in arr:
                sorted_arr[count[num] - 1] = num
                count[num] -= 1

            for i in range(len(arr)):
                arr[i] = sorted_arr[i]

    def shell_sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    def tree_sort(self, arr):
        def insert(root, value):
            if root is None:
                return {'value': value, 'left': None, 'right': None}
            if value < root['value']:
                root['left'] = insert(root['left'], value)
            else:
                root['right'] = insert(root['right'], value)
            return root

        def in_order_traversal(root, sorted_arr):
            if root is None:
                return
            in_order_traversal(root['left'], sorted_arr)
            sorted_arr.append(root['value'])
            in_order_traversal(root['right'], sorted_arr)

        root = None
        for num in arr:
            root = insert(root, num)
        sorted_arr = []
        in_order_traversal(root, sorted_arr)
        arr.clear()
        arr.extend(sorted_arr)

    def plot_scatter_graph(self):
        # Initialize lists to store values
        n_values = []
        time_taken = []

        # Perform sorting algorithm for different n values
        for n in range(0, 1001):
            # Generate a random list of n elements
            arr = [random.randint(1, 1000) for _ in range(n)]

            # Measure the time taken for sorting
            start_time = time.time()

            match ConfigWindow.sort_algo:
                case "Merge Sort":
                    self.merge_sort(arr)
                case "Quick Sort":
                    self.quick_sort(arr, 0, len(arr)-1)
                case "Heap Sort":
                    self.heap_sort(arr)
                case "Radix Sort":
                    self.radix_sort(arr)
                case "Tim Sort":
                    self.tim_sort(arr)
                case "Counting Sort":
                    self.counting_sort(arr)
                case "Shell Sort":
                    self.shell_sort(arr)
                case "Insertion Sort":
                    self.insertion_sort(arr)
                case "Selection Sort":
                    self.selection_sort(arr)
                case "Bubble Sort":
                    self.bubble_sort(arr)
                case "Tree Sort":
                    self.tree_sort(arr)

            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds

            # Append n and time taken to the lists
            n_values.append(n)
            time_taken.append(elapsed_time)

        # Calculate average time
        average_time = np.mean(time_taken)

        # Create scatter plot
        fig, ax = plt.subplots(figsize=(8, 5), facecolor='black')
        ax.scatter(n_values, time_taken, marker="x", color="red", alpha=0.5, s=5, label="Data Points")
        ax.set_title("Sorting Algorithm Analysis", color="white")  # Set the title color to white
        ax.set_xlabel("Array Length", color="white")  # Set the x-axis label color to white
        ax.set_ylabel("Time Taken (milliseconds)", color="white")  # Set the y-axis label color to white
        ax.set_facecolor('black')  # Set the background color of the plot
        ax.tick_params(axis="x", colors="white")  # Set the color of the x-axis tick labels to white
        ax.tick_params(axis="y", colors="white")  # Set the color of the y-axis tick labels to white
        ax.spines["bottom"].set_color("white")  # Set the color of the x-axis spine to white
        ax.spines["left"].set_color("white")  # Set the color of the y-axis spine to white

        # Add regression line
        z = np.polyfit(n_values, time_taken, 2)
        p = np.poly1d(z)
        regression_curve = p(n_values)
        ax.plot(n_values, regression_curve, color="lime", linewidth=1.5, label="Regression Line")
        legend = ax.legend(facecolor="black")

        # Set the text color inside the legend to white
        for text in legend.get_texts():
            text.set_color("white")

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().place(x=550, y=0)

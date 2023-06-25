import random

from animation import Animation
from block.Block import Block


class ArrayBlock:

    def __init__(self, num_blocks):
        self.canvas_width = 1240
        self.canvas_height = 700
        self.current_pass = 0
        self.x = 55
        self._length = num_blocks
        self._blocks = []

        block_length = int(self.canvas_width * (13 / 17) / num_blocks)
        padX = block_length / 10

        for i in range(self._length):
            b = Block(self.x + (i * block_length) + (i * padX), self.canvas_height / 2.5, block_length, self)
            self._blocks.append(b)

    def paint(self, canvas):
        for block in self._blocks:
            block.paint(canvas)

    def delete_blocks(self):
        self._blocks = None

    @classmethod
    def swap(cls, b1, b2, canvas):
        b1.set_color("#cb6ce6")
        b2.set_color("#cb6ce6")
        Animation.swap(b1, b2)
        canvas.update()
        b1.set_color("#E44444")
        b2.set_color("#E44444")

    # This function sorts the blocks using bubble sort
    def bubble_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        n = len(self._blocks)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self._blocks is None:
                    return
                if self._blocks[j].random_number > self._blocks[j + 1].random_number:
                    ArrayBlock.swap(self._blocks[j + 1], self._blocks[j], canvas)
                    self._blocks[j], self._blocks[j + 1] = self._blocks[j + 1], self._blocks[j]
            self.current_pass += 1

        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()

    def insertion_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        n = len(self._blocks)

        for i in range(1, n):
            current = self._blocks[i]
            j = i - 1
            while j >= 0 and current.random_number < self._blocks[j].random_number:
                over_write = current
                ArrayBlock.swap(over_write, self._blocks[j], canvas)
                self._blocks[j + 1] = self._blocks[j]
                self._blocks[j] = current
                j -= 1
            self._blocks[j + 1] = current
            self.current_pass += 1

        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()

    def selection_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        n = len(self._blocks)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self._blocks[min_idx].random_number > self._blocks[j].random_number:
                    min_idx = j
            ArrayBlock.swap(self._blocks[min_idx], self._blocks[i], canvas)
            self._blocks[i], self._blocks[min_idx] = self._blocks[min_idx], self._blocks[i]
            self.current_pass += 1

        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()

    def quick_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        def quick_sort_recursive(start, end):
            def partition(lo, hi):
                pivot_index = random.randint(lo, hi)
                pivot = self._blocks[pivot_index]
                while lo <= hi:
                    while lo < len(self._blocks) and self._blocks[lo].random_number < pivot.random_number:
                        lo += 1
                    while self._blocks[hi].random_number > pivot.random_number:
                        hi -= 1
                    if lo <= hi:
                        if self._blocks[lo].random_number != self._blocks[hi].random_number:
                            ArrayBlock.swap(self._blocks[hi], self._blocks[lo], canvas)
                            self._blocks[lo], self._blocks[hi] = self._blocks[hi], self._blocks[lo]
                        lo += 1
                        hi -= 1
                return hi

            if start < end:
                p = partition(start, end)
                self.current_pass += 1
                quick_sort_recursive(start, p)
                quick_sort_recursive(p + 1, end)

        quick_sort_recursive(0, len(self._blocks) - 1)
        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()

    def merge_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        # Merge function to combine two sorted halves
        def merge(start, middle, end):
            left_index = start
            right_index = middle + 1

            # Iterate until one of the halves is exhausted
            while left_index <= middle and right_index <= end:
                if self._blocks[left_index].random_number <= self._blocks[right_index].random_number:
                    left_index += 1
                else:
                    # Move the elements to their correct positions
                    for i in range(right_index, left_index, -1):
                        ArrayBlock.swap(self._blocks[i], self._blocks[i - 1], canvas)
                        self._blocks[i], self._blocks[i - 1] = self._blocks[i - 1], self._blocks[i]
                    left_index += 1
                    middle += 1
                    right_index += 1

        def merge_sort_recursive(start, end):
            if start < end:
                middle = (start + end) // 2
                self.current_pass += 1
                merge_sort_recursive(start, middle)
                merge_sort_recursive(middle + 1, end)
                merge(start, middle, end)

        merge_sort_recursive(0, len(self._blocks) - 1)
        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()

    def tim_sort(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas

        MIN_MERGE = 3  # Minimum size of a subarray for merge sort
        n = len(self._blocks)

        # Insertion sort implementation
        def insertion_sort(lo, hi):
            for k in range(lo + 1, hi + 1):
                current = self._blocks[k]
                j = k - 1
                while j >= lo and current.random_number < self._blocks[j].random_number:
                    ArrayBlock.swap(self._blocks[j+1], self._blocks[j], canvas)
                    self._blocks[j + 1] = self._blocks[j]
                    self._blocks[j] = current
                    j -= 1

        # Merge sort implementation
        def merge_sort(lo, hi):
            if hi - lo < MIN_MERGE:
                insertion_sort(lo, hi)
            else:
                mid = (lo + hi) // 2
                merge_sort(lo, mid)
                merge_sort(mid + 1, hi)
                merge(lo, mid, hi)

        # Merge function to combine two sorted halves
        def merge(lo, mid, hi):
            left_index = lo
            right_index = mid + 1

            # Iterate until one of the halves is exhausted
            while left_index <= mid and right_index <= hi:
                if self._blocks[left_index].random_number <= self._blocks[right_index].random_number:
                    left_index += 1
                else:
                    # Move the elements to their correct positions
                    for x in range(right_index, left_index, -1):
                        ArrayBlock.swap(self._blocks[x], self._blocks[x - 1], canvas)
                        self._blocks[x], self._blocks[x - 1] = self._blocks[x - 1], self._blocks[x]
                    left_index += 1
                    mid += 1
                    right_index += 1

        # Perform Tim Sort
        for i in range(0, n, MIN_MERGE):
            insertion_sort(i, min((i + MIN_MERGE - 1), (n - 1)))

        size = MIN_MERGE
        while size < n:
            for start in range(0, n, size * 2):
                middle = start + size - 1
                end = min((start + size * 2 - 1), (n - 1))
                merge(start, middle, end)
            size *= 2

        # Update canvas and set is_sorted flag
        DrawingCanvas.set_is_sorted(True)
        DrawingCanvas.update_blocks()


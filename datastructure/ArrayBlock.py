from animation import Animation
from block.Block import Block


class ArrayBlock:

    def __init__(self, num_blocks):
        self.canvas_width = 1240
        self.canvas_height = 700
        self.x = 48
        self._length = num_blocks
        self._blocks = []

        block_length = int(self.canvas_width * (14 / 17) / num_blocks)
        padX = block_length / 10

        for i in range(self._length):
            b = Block(self.x + (i * block_length) + (i * padX), self.canvas_height / 2.75, block_length, self)
            self._blocks.append(b)

    def paint(self, canvas):
        for block in self._blocks:
            block.draw_square(canvas)

    def delete_blocks(self):
        self._blocks.clear()

    # This function sorts the blocks using bubble sort
    def bubble_sort(self, canvas):
        n = len(self._blocks)

        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self._blocks[j].random_number > self._blocks[j + 1].random_number:
                    self._blocks[j], self._blocks[j + 1] = self._blocks[j + 1], self._blocks[j]
                    Animation.swap(self._blocks[j], self._blocks[j + 1])
                    canvas.update()




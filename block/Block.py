import random


class Block:
    def __init__(self, x, y, length, canvas):
        self._x = int(x)
        self._y = int(y)
        self._length = length
        self._canvas = canvas
        self._block_color = "#E44444"

        # Generate a random integer
        self._random_number = random.randint(1, 100)

    # Getter and setter for x coordinate
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    # Getter and setter for y coordinate
    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y

    # Getter and setter for length
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    def set_color(self, block_color):
        self._block_color = block_color

    @property
    def random_number(self):
        return self._random_number

    # draws block on the window
    def paint(self, canvas):
        from uicomponents.DrawingCanvas import DrawingCanvas
        # Draw the square
        if DrawingCanvas.get_is_sorted():
            self._block_color = "#00bf63"
        canvas.create_rectangle(self._x, self._y, self._x + self._length, self._y + self._length,
                                fill=self._block_color)

        # Write the random number inside the square
        text_x = self._x + self._length / 2
        text_y = self._y + self._length / 2
        font_size = self.calculate_font_size()
        canvas.create_text(text_x, text_y, text=str(self._random_number), font=('Arial', font_size, 'bold'),
                           fill="#373737")

    def calculate_font_size(self):
        base_font_size = 12  # Base font size for reference
        scaling_factor = 0.4  # Adjust this factor to control the scaling

        font_size = int(self._length * scaling_factor)
        if font_size < base_font_size:
            font_size = base_font_size

        return font_size

    @random_number.setter
    def random_number(self, value):
        self._random_number = value

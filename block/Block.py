import random


class Block:
    def __init__(self, x, y, length, canvas):
        self._x = int(x)
        self._y = int(y)
        self._length = length
        self._canvas = canvas

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

    @property
    def random_number(self):
        return self._random_number

    # draws block on the window
    def draw_square(self, canvas):
        # Draw the square
        canvas.create_rectangle(self._x, self._y, self._x + self._length, self._y + self._length, fill="white")

        # Write the random number inside the square
        text_x = self._x + self._length / 2
        text_y = self._y + self._length / 2
        font_size = self.calculate_font_size()
        canvas.create_text(text_x, text_y, text=str(self._random_number), font=('Arial', font_size, 'bold'),
                           fill="black")

    def calculate_font_size(self):
        base_font_size = 12  # Base font size for reference
        scaling_factor = 0.4  # Adjust this factor to control the scaling

        font_size = int(self._length * scaling_factor)
        if font_size < base_font_size:
            font_size = base_font_size

        return font_size

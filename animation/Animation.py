from block.Block import Block


# This function is for animation for swapping of two blocks
def swap(b1: Block, b2: Block, delay=1):
    from uicomponents.DrawingCanvas import DrawingCanvas
    distance = abs(int(b1.get_x() - b2.get_x()))

    def animate_swap(step):
        if step < int(1.2 * b1.length):
            b1.set_y(b1.get_y() + 1)
            b2.set_y(b2.get_y() - 1)
            DrawingCanvas.update_blocks()
            DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))
        else:
            if step < int(1.2 * b1.length) + distance:
                b2.set_x(b2.get_x() + 1)
                b1.set_x(b1.get_x() - 1)
                DrawingCanvas.update_blocks()
                DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))
            else:
                if step < int(1.2 * b1.length) + distance + int(1.2 * b1.length):
                    b2.set_y(b2.get_y() + 1)
                    b1.set_y(b1.get_y() - 1)
                    DrawingCanvas.update_blocks()
                    DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))

    animate_swap(0)

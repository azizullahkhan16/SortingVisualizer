from block.Block import Block


def swap(b1: Block, b2: Block, delay=1):
    from uicomponents.DrawingCanvas import DrawingCanvas
    is_positive = False

    distance = int(b1.get_x() - b2.get_x())

    if distance > 0:
        is_positive = True
    else:
        distance = abs(distance)

    def animate_swap(step):

        while DrawingCanvas.get_animation_paused():
            DrawingCanvas.canvas.update()

        if step < int(1.1 * b1.length):
            b1.set_y(b1.get_y() + 1)
            b2.set_y(b2.get_y() - 1)
            DrawingCanvas.update_blocks()
            DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))
        else:
            if step < int(1.1 * b1.length) + distance:
                if not is_positive:
                    b2.set_x(b2.get_x() - 1)
                    b1.set_x(b1.get_x() + 1)
                else:
                    b2.set_x(b2.get_x() + 1)
                    b1.set_x(b1.get_x() - 1)
                DrawingCanvas.update_blocks()
                DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))
            else:
                if step < int(1.1 * b1.length) + distance + int(1.1 * b1.length):
                    b2.set_y(b2.get_y() + 1)
                    b1.set_y(b1.get_y() - 1)
                    DrawingCanvas.update_blocks()
                    DrawingCanvas.canvas.after(delay, lambda: animate_swap(step + 1))

    animate_swap(0)

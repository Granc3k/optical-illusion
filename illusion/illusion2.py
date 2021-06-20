
from graphics import Canvas

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
SQUARE_SIZE = 50
NUM_ROWS = 10
SQUARES = CANVAS_WIDTH

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Illusion 2")
    for i in range(NUM_ROWS):
        for j in range(SQUARES):



    canvas.mainloop()


if __name__ == '__main__':
    main()

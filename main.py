from karel_py import *

width = 32
height = 32

class ScreenBuffer:
    def __init__(self):
        global width, height
        self.pixels = [[1 for _ in range(width)] for _ in range(height)]

    def load(self, frame):
        global width
        pixels = []

        # will break if non-perfect numbers are used
        hex_chars_per_row: int = ((width * height) // 4) // width

        for i in range(0, len(frame), hex_chars_per_row):
            """
            Each frame is a string of hexadecimal with len w*h/4.
            Each bit is a single black/white pixel where 0 is black 
            and 1 is white. Decoding can be done easily for a grid
            by converting hex_chars_per_row hex chars into a row and then
            into a string with formating ({:b}
            """
            processed_byte = ""
            for j in range(i, i+hex_chars_per_row):
                processed_byte += frame[j]
            processed_byte = int(processed_byte, 16)

            row_str = f"{processed_byte:0{hex_chars_per_row * 4}b}"
            row = [int(c) for c in row_str]
            pixels.append(row)

        self.pixels = pixels

"""
Draws a row to the world, reading pixel data from the screen buffer.
Assumes karel is next to the east or west wall facing away from it.
Karel will end up next to the wall he was facing before the function, and he will be facing the same way.
"""
def draw_row(buf: ScreenBuffer, row: int):
    global width
    row, count = buf.pixels[row], 0
    if facing_west(): count = width - 1
    while front_is_clear():
        paint('black' if row[count] == 0 else 'white')
        move()
        count += -1 if facing_west() else 1
    paint('black' if row[count] == 0 else 'white')

"""
Completes a 180 degree turn landing one row higher then before unless standing below the ceiling. Assumes Karel is facing east or west.
"""
def elbow():
    east = facing_east()
    if east:
        turn_left()
    else:
        turn_right()

    if front_is_clear():
        move()
        if east:
            turn_left()
        else:
            turn_right()

"""
Colors the entire Karel world according to the colors stored in the screen buffer. Assumes that Karel is in the bottom left corner of the world facing east. Returns Karel to the bottom left corner facing east.
"""
def draw(buf: ScreenBuffer):
    global height
    for row in range(height):
        draw_row(buf, row)
        elbow()
    turn_around()

    for i in range(height - 1):
        move()
    turn_left()


"""
Initializes and runs the Karel program
"""
def main():
    with open('video.txt', 'r') as file:
        frames = file.read().split()
        for frame in frames:
            buf = ScreenBuffer()
            buf.load(frame)
            draw(buf)

if __name__ == "__main__":
    main()
    run_karel_program()

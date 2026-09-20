from PIL import Image, ImageDraw

SIZE = 1000
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))  
draw = ImageDraw.Draw(img)

cell = 180
gap = 12
grid_size = 3 * cell + 2 * gap
x0 = (SIZE - grid_size) // 2
y0 = (SIZE - grid_size) // 2

D, M, L, W = 135, 150, 165, 250
DARK   = (D, D, D, 255)
MEDIUM = (M, M, M, 255)
LIGHT  = (L, L, L, 255)
WHITE  = (W, W, W, 0)
BORDER = (35, 35, 35, 255)

BORDER_WIDTH = 3
CORNER_RADIUS = 35

for i in range(3):
    for j in range(3):
        color = WHITE
        if   i == 0 and j == 0: color = DARK
        elif i == 1 and j == 1: color = MEDIUM
        elif i == 2 and j == 2: color = LIGHT

        x = x0 + j * (cell + gap)
        y = y0 + i * (cell + gap)

        draw.rounded_rectangle(
            [x, y, x + cell, y + cell],
            radius=CORNER_RADIUS,
            fill=color,
            outline=BORDER,
            width=BORDER_WIDTH,
        )

img.save("./logo.png")  

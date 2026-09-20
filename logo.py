from PIL import Image, ImageDraw

SIZE = 1000
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))  
draw = ImageDraw.Draw(img)

cell = 180
gap = 25
grid_size = 3 * cell + 2 * gap
x0 = (SIZE - grid_size) // 2
y0 = (SIZE - grid_size) // 2


BORDER = (35, 35, 35, 255)

BORDER_WIDTH = 3
CORNER_RADIUS = 40

A = "#60B345" 
B = "#B0C223" 
C = "#FFD100"
D = "#F47920" 
E = "#E23838" 
F = "#A93265" 
G = "#6F2C91" 
H = "#3868BB"
I = "#00A4E4" 

colors = [(I, 0,0), (H, 0,1), (F, 0,2), (C, 1,0), (E, 1,1), (G, 1,2),(D, 2,0), (B, 2,1), (A,2,2)]

for color, i, j in colors:

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

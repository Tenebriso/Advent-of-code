"""
Now you're ready to decode the image.
The image is rendered by stacking the layers and aligning the pixels with the same positions in each
layer. The digits indicate the color of the corresponding pixel:
    0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back.
So, if a given position has a transparent pixel in the first and second layers, a black pixel in
the third layer, and a white pixel in the fourth layer, the final image would have a black pixel
at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000
corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:

The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10
What message is produced after decoding your image?
"""

def get_input(file_name):
    """ Open the input file and read the colors one by one. Put each color in its layer.
    Returns a dict of {layer: colors} """
    image = {}
    with open(file_name) as input_file:
        colors = input_file.readline().strip()
    level = ''
    layer = 0
    for pos, color in enumerate(colors):
        if pos % WIDTH == 0 and pos != 0:
            try:
                image[layer].append(level)
            except KeyError:
                image[layer] = [level]
            level = ''
        if pos % (WIDTH * HEIGHT) == 0:
            level = ''
            layer += 1
        level += color
    image[layer].append(level)

    return image


def get_color_of_pixel(pixel):
    """ Given the colors of a pixel as a string in which each letter represents the color
    of the layer X where X is the position in the string, return the first non-transparent colour:
        2 = transparent
        1 = white
        0 = black """
    for color in pixel:
        if color != '2':
            return color
    return '2'


def build_pixel():
    """ Given an image, construct the matrix of pixels """
    colors = []
    for i in range(HEIGHT):
        colors.append([])
        for j in range(WIDTH):
            color = ''
            for _layer, levels in IMAGE.items():
                color += levels[i][j]
            colors[i].append(color)
    return colors


def decode_image():
    """ Given an image, construct the matrix of pixels and print each pixel according to its colour:
        if the pixel is white, print #; if it's black, print a blank space """
    colors = build_pixel()
    for color in colors:
        for pixel in color:
            if get_color_of_pixel(pixel) == '1':
                print('#', end='')
            else:
                print(' ', end='')
        print()

WIDTH, HEIGHT = 25, 6
IMAGE = get_input('input')
decode_image()

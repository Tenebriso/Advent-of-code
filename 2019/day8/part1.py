"""
The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars
rovers, and so they are curious if you would spend a brief sojourn on Mars.
You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of rebooting!
It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a
picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding;
instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why
this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel.
The digits fill each row of the image left-to-right, then move downward to the next row,
filling rows top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way.
So, the first digit corresponds to the top-left pixel of the first layer, the second digit
corresponds to the pixel to the right of that on the same layer, and so on until the last digit,
which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds
to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the
layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by
the number of 2 digits?
"""

def get_input(file_name, width, height):
    """ Open the input file and read the colors one by one. Put each color in its layer.
    Returns a dict of {layer: colors} """
    image = {}
    with open(file_name) as input_file:
        colors = input_file.readline().strip()
    level = ''
    layer = 0
    for pos, color in enumerate(colors):
        if pos % width == 0 and pos != 0:
            try:
                image[layer].append(level)
            except KeyError:
                image[layer] = [level]
            level = ''
        if pos % (width * height) == 0:
            level = ''
            layer += 1
        level += color
    image[layer].append(level)

    return image


def check_image(image, width, height):
    """ Check that the given image corresponds to the dimensions """
    for _layer, levels in image.items():
        assert len(levels) == height
        for level in levels:
            assert len(level) == width


def find_layer_with_min_digit(image, digit):
    """ Find the layer that has the least number of digits equal to `digit` """
    min_digits, min_layer = 10000, 0
    for layer, levels in image.items():
        current_digits = 0
        for level in levels:
            current_digits += level.count(digit)
        if current_digits < min_digits:
            min_digits = current_digits
            min_layer = layer
    return min_layer


def count_layer_digits(image, layer, digit):
    """ Count the number of digits equal to `digit` in the given layer """
    digits = 0
    levels = image[layer]
    for level in levels:
        digits += level.count(digit)
    return digits


WIDTH, HEIGHT = 25, 6
IMAGE = get_input('input', WIDTH, HEIGHT)
check_image(IMAGE, WIDTH, HEIGHT)
LAYER = find_layer_with_min_digit(IMAGE, '0')
DIGIT_1 = count_layer_digits(IMAGE, LAYER, '1')
DIGIT_2 = count_layer_digits(IMAGE, LAYER, '2')
print(DIGIT_1 * DIGIT_2)

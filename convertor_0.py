'''
    Batch convert a folder with images to pdf.
    Expected usage:
        python conv_0.py [prefix] [min_range] [max_range] [suffix] [ouput_file]
    example:
        python conv_0.py -max_range=3 -suffix=.png -output_file=out.pdf
'''
from PIL import Image

# Hard coded program parameters
min_range = 0
max_range = 3
prefix = "imgs_png/"
suffix = ".png"
images = []

images = []
for i in range(min_range, max_range + 1):
    fname = prefix + str(i) + suffix
    print(fname)
    # Load the current image and store it
    im = Image.open(fname)
    # (Optional) Process the image if necessary ...
    # Pillow can't save RGBA images to pdf,
    # make sure the image is RGB
    if im.mode == "RGBA":
        im = im.convert("RGB")
    # Add the image to the images list
    images.append(im)

# Convert the images list to pdf
images[0].save("aaa.pdf", save_all = True, append_images = images[1:])

'''
    Batch convert a folder with images to pdf.
    Expected usage:
        python conv_0.py [prefix] [min_range] [max_range] [suffix] [ouput_file]
    example:
        python conv_0.py -max_range=3 -suffix=.png -output_file=out.pdf
    The code will read in all images from the current folder, image name format e.g. 0.png
'''
import img2pdf
import argparse

def process_images(min_range, max_range, prefix, suffix, out_file):
    images = []
    for i in range(min_range, max_range + 1):
        fname = prefix + str(i) + suffix
        images.append(fname)
    out_file.write(img2pdf.convert(images))

if __name__ == "__main__":
    # Let the user pass parameters to the code, all parameters are optional have some default values
    parser = argparse.ArgumentParser()
    parser.add_argument("-min_range", type=int, default=0, help="Min range of input images")
    parser.add_argument("-max_range", type=int, default=0, help="Max range of input images")
    parser.add_argument("-prefix", default="", help="Image name prefix")
    parser.add_argument("-suffix", default=".jpg", help="Image termination, e.g. .png or .jpg")
    parser.add_argument("-output", default="out.pdf", help="Output file name")
    args = parser.parse_args()

    min_range = args.min_range
    max_range = args.max_range
    prefix = args.prefix
    suffix = args.suffix
    out_fname = args.output

    # Make sure the output file ends with *.pdf*
    if not (out_fname.endswith(".pdf") or out_fname.endswith(".PDF")):
        out_fname += ".pdf"

    with open(out_fname, "wb") as out_file:
        process_images(min_range, max_range, prefix, suffix, out_file)

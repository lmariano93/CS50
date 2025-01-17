import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    input_ext, output_ext = sys.argv[1].split(".")[1], sys.argv[2].split(".")[1]
    if input_ext == output_ext:
        if output_ext in ["jpg", "jpeg", "png"]:
            try:
                image = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exist")
            shirt = Image.open("shirt.png")
            muppet = ImageOps.fit(image, shirt.size)
            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])
        else:
            sys.exit("Invalid Output")
    else:
        sys.exit("Input and output have different extensions")

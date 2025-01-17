import pyfiglet
import sys
import random

figlet = pyfiglet.Figlet()

while True:
    try:
        if len(sys.argv) == 1:
            is_random = True
            break
        elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            is_random = False
            font = sys.argv[2]
            break
        else:
            sys.exit(1)
    except ValueError:
        sys.exit(1)

if not is_random:
    figlet.setFont(font=font)
else:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)


text = input("Input: ")

print("Output:")
print(figlet.renderText(text))

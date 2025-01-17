import sys
import inflect

names = []
p = inflect.engine()

print("Name: ")
try:
    while True:
        name = input().strip()
        if name:
            names.append(name)
except EOFError:
    pass

farewell = p.join(names)

print(f"Adieu, adieu, to {farewell}")

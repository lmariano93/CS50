from fpdf import FPDF

class generate():
    def __init__(self, name):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 45)
        pdf.cell(0, 60, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=30, y=70, w=150)
        pdf.set_font_size(30)
        pdf.set_text_color(255, 255, 255)

        phrase = f"{name} took CS50"
        phrase_width = pdf.get_string_width(phrase)
        phrase_x = (210 - phrase_width) / 2  

        pdf.text(x=phrase_x, y=140, txt=phrase)
        pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = generate(name)

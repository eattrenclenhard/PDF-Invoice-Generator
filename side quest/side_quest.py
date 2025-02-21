from glob import glob as gl
from fpdf import FPDF
from pathlib import Path

filepaths = gl('Text-Files/*.txt')
filenames = [Path(f).stem.title() for f in filepaths]
# print(filenames)

pdf = FPDF(orientation='P', unit='mm', format='A4')

for f in filepaths:
    filename = Path(f).stem.title()
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=12, txt=filename, align='L', ln=1)

    with open(f) as f:
        desc = f.read()
    pdf.set_font(family='Times', size=12, style='I')
    pdf.multi_cell(w=0, h=6, txt=desc)
    # 0 means that multicell will span the entire width of the page

pdf.output('side_quest.pdf')

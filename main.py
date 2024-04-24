import pandas as pd
from glob import glob as gl
from fpdf import FPDF
from pathlib import Path

filepaths = gl('invoices/*.xlsx')

for f in filepaths:
    df = pd.read_excel(f, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(f).stem  # extracts the filename w/o extension
    invoice_no, date = filename.split('-')

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f'Invoice no. {invoice_no}', ln=1)

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    pdf.output(f'PDFs/{filename}.pdf')

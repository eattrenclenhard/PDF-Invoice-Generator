import pandas as pd
from glob import glob as gl
from fpdf import FPDF
from pathlib import Path

filepaths = gl('invoices/*.xlsx')

for f in filepaths:
    df = pd.read_excel(f, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='B')

    filename = Path(f).stem  # extracts the filename w/o extension
    invoice_no, date = filename.split('-')
    pdf.cell(w=50, h=8, txt=f'Invoice nr. {invoice_no}')

    pdf.output(f'PDFs/{filename}.pdf')

import pandas as pd
from glob import glob as gl

filepaths = gl('invoices/*.xlsx')

for f in filepaths:
    df = pd.read_excel(f, sheet_name='Sheet 1')
    print(df['product_id'])
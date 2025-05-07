import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), 'assets', "cleaned_pos_medical_notes.csv") 

df = pd.read_csv(file_path)

num_rows, num_columns = df.shape
print(f'Jumlah Baris: {num_rows}')
print(f'Jumlah Kolom: {num_columns}')

row_data = df.iloc[5:6] 

output_file_path = os.path.join(os.path.dirname(__file__), 'assets', '065123007.csv')
row_data.to_csv(output_file_path, index=False)

print(f"Data baris ke-7 telah disalin ke file {output_file_path}")
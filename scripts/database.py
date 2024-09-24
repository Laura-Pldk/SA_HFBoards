import sqlite3
import pandas as pd
import glob
import os

data_folder = os.path.join(os.getcwd(), 'data')

conn = sqlite3.connect('C:\\Users\\lplod\\OneDrive\\Dokumente\\SA_HFBoards\\forums.db')

csv_files = glob.glob(os.path.join(data_folder, '*_forum.csv'))

if not csv_files:
    print(f"No CSV files found in {data_folder}")
else:
    print(f"CSV files found: {csv_files}")

for file in csv_files:
    df = pd.read_csv(file)

    base_name = os.path.basename(file)
    print(f"Processing file: {base_name}") 

    if base_name.endswith('_forum.csv'):
        forum_name = base_name.replace('_forum.csv', '')
    else:
        print(f"Unexpected file name format: {base_name}")
        forum_name = 'unknown'
    
    print(f"Extracted forum name: {forum_name}")  

    df['forum'] = forum_name

    df.to_sql('forum_data', conn, if_exists='append', index=False)

conn.close()

print("Data successfully written to SQLite database.")
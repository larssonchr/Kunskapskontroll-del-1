import pandas as pd
import sqlite3
con = sqlite3.connect('studentlife.db')
df = pd.read_csv(r'C:\Users\chr08\anaconda3\student_lifestyle_dataset.csv', index_col=False)
df['Sleep_Hours_Per_Day'] = 10
import pandas as pd
import re
from nltk.tokenize import word_tokenize
import os
import nltk

# nltk.download('punkt')
# nltk.download('punkt_tab')

file_path = os.path.join(os.path.dirname(__file__), 'assets', "065123007.csv") 
df = pd.read_csv(file_path)
sample_text = df['text'].values[0] 

# 1. Output sebelum dan sesudah proses Basic Data Cleansing
# Sebelum cleansing (sample_text)
print("\n--- Sebelum Data Cleansing ---")
print("SUCCESS")
# print(sample_text)

cleaned_text = re.sub(r'<.*?>', '', sample_text) 
cleaned_text = ' '.join(cleaned_text.split()) 
cleaned_text = cleaned_text.lower() 

print("\n--- Setelah Data Cleansing ---")
# print(cleaned_text)
print("SUCCESS")

# 2. Output sebelum dan sesudah proses Lexical Analysis
# Sebelum Lexical Analysis (sample_text)
print("\n--- Sebelum Lexical Analysis ---")
# print(sample_text)
print("SUCCESS")


tokens = word_tokenize(cleaned_text)

print("\n--- Setelah Lexical Analysis (Tokens) ---")
print("SUCCESS")
# print(tokens)

before_cleansing_df = pd.DataFrame({'Before Data Cleansing': [sample_text]})
before_cleansing_df.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'before_data_cleansing.csv'), index=False)

after_cleansing_df = pd.DataFrame({'After Data Cleansing': [cleaned_text]})
after_cleansing_df.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'after_data_cleansing.csv'), index=False)

before_lexical_df = pd.DataFrame({'Before Lexical Analysis': [sample_text]})
before_lexical_df.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'before_lexical_analysis.csv'), index=False)

tokens_df = pd.DataFrame({'After Lexical Analysis (Tokens)': tokens})
tokens_df.to_csv(os.path.join(os.path.dirname(__file__), 'assets', 'after_lexical_analysis.csv'), index=False)

print("\nFiles have been saved with the results.")

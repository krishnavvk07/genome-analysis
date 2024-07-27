import pandas as pd

data = pd.read_excel('altered-allele.ods')

filtered_data = data.dropna(subset=['site'])

filtered_data.to_csv('filtered_altered_allele.ods', index=False)

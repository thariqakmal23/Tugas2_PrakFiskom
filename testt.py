import pandas as pd
import numpy as np

# Bagian 1: Membuat DataFrame pertama
last_names = ['Connor', 'Connor', 'Reese']
first_names = ['Sarah', 'John', 'Kyle']
df = pd.DataFrame({
  'first_name': first_names,
  'last_name': last_names,
})

# Bagian 2: Membaca data dari URL
url = "https://github.com/luminati-io/Instagram-dataset-samples/raw/main/Instagram%20Profiles%20-%20Github%20Hashtag.xlsx"
database = pd.read_excel(url)

# Bagian 3: Menampilkan informasi tentang DataFrame kedua
print("Columns:")
print(database.columns)

print("\nDescription:")
print(database.describe())

print("\nFirst 5 rows:")
print(database.head())

print("\nLast 5 rows:")
print(database.tail())

# Bagian 4: Membuat DataFrame kedua dengan kolom x, y, dan z
x = [i for i in range(0, 10)]
y = np.sin(x)

dataframe = pd.DataFrame({
    'x': x,
    'y': y
})

dataframe['z'] = np.cos(x)

# Bagian 5: Menampilkan DataFrame kedua
print("\nDataFrame kedua:")
print(dataframe)

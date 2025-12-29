import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('prakt9.csv')

df.columns = df.columns.str.strip()
df['Country Name'] = df['Country Name'].str.strip()
df['Series Code'] = df['Series Code'].str.strip()

year_columns = [col for col in df.columns if col.startswith('20')]
years = [int(col.split()[0]) for col in year_columns]

def clean_data(series):
    return pd.to_numeric(series.replace('..', np.nan))

indicator_code = 'FP.CPI.TOTL.ZG'

ukraine_row = df[
    (df['Country Name'] == 'Ukraine') &
    (df['Series Code'] == indicator_code)
]

usa_row = df[
    (df['Country Name'] == 'United States') &
    (df['Series Code'] == indicator_code)
]

if ukraine_row.empty or usa_row.empty:
    print("Дані з інфляції не знайдені")
    exit()

ukraine_data = clean_data(ukraine_row[year_columns].iloc[0]).values
usa_data = clean_data(usa_row[year_columns].iloc[0]).values

plt.figure(figsize=(10, 5))
plt.plot(years, ukraine_data, marker='o', label='Ukraine')
plt.plot(years, usa_data, marker='s', label='United States')
plt.title('Inflation, consumer prices (annual %)')
plt.xlabel('Year')
plt.ylabel('Inflation (%)')
plt.legend()
plt.grid(True)
plt.show()

country = input("Enter country (Ukraine or United States): ").strip()

if country == 'Ukraine':
    data = ukraine_data
elif country == 'United States':
    data = usa_data
else:
    print("Даних для цієї країни немає")
    exit()

print(f"{country} inflation data:", data)

plt.figure(figsize=(10, 5))
plt.bar(years, data)
plt.title(f'Inflation, consumer prices (annual %) – {country}')
plt.xlabel('Year')
plt.ylabel('Inflation (%)')
plt.show()
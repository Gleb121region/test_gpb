import pandas as pd

df = pd.read_csv('file.csv', delimiter='|')

df.columns = df.columns.str.strip()
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

unique_records = df.drop_duplicates(subset='id', keep=False)

duplicate_records = df[df.duplicated(subset='id', keep=False)]

unique_records.to_csv('unique_records.csv', index=False, sep='|')

duplicate_records.to_csv('duplicate_records.csv', index=False, sep='|')

print("Уникальные записи сохранены в 'unique_records.csv'")
print("Дублирующиеся записи сохранены в 'duplicate_records.csv'")

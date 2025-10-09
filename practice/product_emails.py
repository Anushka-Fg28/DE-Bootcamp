import csv

data = open('products.csv', encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

# Check header row
print(data_lines[0])

# Extract first 10 product names
product_names = []
for line in data_lines[1:11]:
    product_names.append(line[1])  # assuming 2nd column is product name

print(product_names)

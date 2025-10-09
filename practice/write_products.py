import csv

# Create a new file
file_to_output = open('new_products.csv', 'w', newline='', encoding="utf-8")

# Create a writer object
csv_writer = csv.writer(file_to_output, delimiter=',')

# Write header and rows
csv_writer.writerow(['product_id', 'product_name', 'price'])
csv_writer.writerows([
    [1, 'Keyboard', 499],
    [2, 'Mouse', 299],
    [3, 'Monitor', 7999]
])

file_to_output.close()
print("Data written to new_products.csv successfully.")

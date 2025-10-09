import csv

f = open('new_products.csv', 'a', newline='', encoding="utf-8")
csv_writer = csv.writer(f)
csv_writer.writerow([4, 'Laptop', 55000])
f.close()

print("Data appended to new_products.csv successfully.")

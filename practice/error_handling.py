import os
import csv

filename = "products.csv"

try:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist")

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if len(row) < 7:
                print(f"Skipping row with missing data: {row}")
                continue
            print(f"Product: {row[1]}, Price: {row[3]}, Rating: {row[6]}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'")
except csv.Error as e:
    print(f"CSV Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

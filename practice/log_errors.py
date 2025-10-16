import csv
import os

input_file = "products.csv"
error_log_file = "error_log.csv"

try:
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File '{input_file}' does not exist")

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(error_log_file, 'w', newline='', encoding='utf-8') as errfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(errfile)

     
        writer.writerow(["error_type", "row_data"])

        header = next(reader)  # Skip header of products.csv

        for row in reader:
            try:
              
                if len(row) < 7:
                    writer.writerow(["Missing Data", row])
                    continue

                float(row[3])   # Price
                int(row[4])     # Stock Quantity
                float(row[6])   # Rating

            except ValueError:
               
                writer.writerow(["Invalid Data", row])
            except Exception as e:
               
                writer.writerow([f"Unexpected Error: {e}", row])

    print(f"Error log has been created successfully in '{error_log_file}'.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError:
    print(f"Error: Permission denied to read '{input_file}'")
except Exception as e:
    print(f"Unexpected error: {e}")

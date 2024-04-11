# import csv
# import re

# def fix_csv(input_file, output_file):
#     with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         rows = list(reader)
    
#     for i in range(len(rows)):
#         # Check if the row has more than three fields
#         if len(rows[i]) > 3:
#             # Join all fields except the last two as the book title
#             title = ','.join(rows[i][:-2])
#             # Enclose the title in double quotes
#             rows[i] = ['"' + title.strip() + '"'] + rows[i][-2:]
#         # Check if the price tag starts with £ symbol
#         if rows[i][-2].startswith('£'):
#             # Remove the pound symbol from the price tag
#             rows[i][-2] = rows[i][-2][1:]
#         # Check if the title is not wrapped in double quotes
#         if not re.match(r'^\".*\"$', rows[i][0]):
#             rows[i][0] = '"' + rows[i][0] + '"'
    
#     with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(rows)

# if __name__ == "__main__":
#     input_file = 'Books.csv'
#     output_file = 'Fixed_Books.csv'
#     fix_csv(input_file, output_file)
#     print("CSV file has been fixed. Corrected data written to", output_file)

import csv
import re
import random

def fix_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    for i in range(len(rows)):
        # Check if the row has more than three fields
        if len(rows[i]) > 3:
            # Join all fields except the last two as the book title
            title = ','.join(rows[i][:-2])
            # Enclose the title in double quotes
            rows[i] = ['"' + title.strip() + '"'] + rows[i][-2:]
        # Check if the price tag starts with £ symbol
        if rows[i][-2].startswith('£'):
            # Remove the pound symbol from the price tag
            rows[i][-2] = rows[i][-2][1:]
        # Check if the title is not wrapped in double quotes
        if not re.match(r'^\".*\"$', rows[i][0]):
            rows[i][0] = '"' + rows[i][0] + '"'
        
        # Add user preference data
        user_id = 'user' + str(random.randint(1, 100))  # Generate a random user ID
        # rating = random.randint(1, 5)  # Generate a random rating
        rows[i] = [user_id] + rows[i] 
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

if __name__ == "__main__":
    input_file = 'Books.csv'
    output_file = 'Fixed_Books.csv'
    fix_csv(input_file, output_file)
    print("CSV file has been fixed. Corrected data written to", output_file)

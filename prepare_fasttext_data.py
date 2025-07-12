import os
import glob
import csv

csv_dir = 'csv_files'
output_path = os.path.join(csv_dir, 'fasttext_data.txt')

os.makedirs(csv_dir, exist_ok=True)
csv_files = glob.glob(os.path.join(csv_dir, '*.csv'))

total_reviews = 0

with open(output_path, 'w', encoding='utf-8') as out_f:
    for csv_file in csv_files:
        try:
            with open(csv_file, 'r', encoding='utf-8') as in_f:
                reader = csv.reader(in_f)
                for row in reader:
                    if row and len(row) > 0:
                        review = row[0].replace('\n', ' ')
                        out_f.write(review + '\n')
                        total_reviews += 1
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

print(f"Created {output_path} with {total_reviews} reviews from {len(csv_files)} files.")
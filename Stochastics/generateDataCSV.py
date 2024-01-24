import csv
import random

csv_file_path = 'homeprices_banglore.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

def generate_random_data():
    area = random.randint(800, 4000)
    bedrooms = random.randint(1, 5)
    price = round(random.uniform(30, 170), 2)
    return [area, bedrooms, price]

for _ in range(100000):
    new_row = generate_random_data()
    data.append(new_row)

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

import requests
import csv
import sqlite3

"""
Python script to fetch data from the FruityVice API.
You can filter by family, range, and/or ID
The results are saved as a CSV file

Inputs: name of file of where to save the CSV, family, genus, or ID range
Output: creates CSV file
"""

# separate function to fetch a request
def fetch_fruits(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Received status code {response.status_code}")
        return []

# Function to save to SQLite database
def save_to_db(fruits):
    conn = sqlite3.connect('fruits.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS fruits
                      (name TEXT, id INTEGER, family TEXT, genus TEXT, 
                      order_field TEXT, carbohydrates REAL, protein REAL, fat REAL, 
                      calories REAL, sugar REAL)''')

    for fruit in fruits:
        row = (fruit['name'], fruit['id'], fruit['family'], fruit['genus'], fruit['order'], 
               fruit['nutritions']['carbohydrates'], fruit['nutritions']['protein'], 
               fruit['nutritions']['fat'], fruit['nutritions']['calories'], fruit['nutritions']['sugar'])

        cursor.execute("INSERT INTO fruits VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()

# Function to read from db and print to console
def read_from_db():
    conn = sqlite3.connect('fruits.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM fruits")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def fetch_and_export_to_csv(filename='fruits.csv', family=None, genus=None, id_range=None, to_db=False):
    base_url = 'https://www.fruityvice.com'
    family_fruits = []
    genus_fruits = []

    # Fetch by family and genus
    if family:
        family_url = f"{base_url}/api/fruit/family/{family}"
        family_fruits = fetch_fruits(family_url)
    if genus:
        genus_url = f"{base_url}/api/fruit/genus/{genus}"
        genus_fruits = fetch_fruits(genus_url)

    # Filter by ID
    if id_range:
        all_url = f"{base_url}/api/fruit/all"
        all_fruits = fetch_fruits(all_url)
        all_fruits = [fruit for fruit in all_fruits if id_range[0] <= fruit['id'] <= id_range[1]]

    # If both family and genus are specified, take intersection. Else, take union
    if family and genus:
        family_ids = {f['id'] for f in family_fruits}
        genus_ids = {g['id'] for g in genus_fruits}
        intersection_ids = family_ids & genus_ids
        fruits = [f for f in family_fruits if f['id'] in intersection_ids]
    elif family:
        fruits = family_fruits
    elif genus:
        fruits = genus_fruits
    else:
        fruits = all_fruits  # Populate with all fruits if no family or genus is specified

    if id_range:
        ids_to_keep = {fruit['id'] for fruit in all_fruits}
        fruits = [fruit for fruit in fruits if fruit['id'] in ids_to_keep]

    if to_db:
        save_to_db(fruits)
        read_from_db()
    else:
        # Export to CSV
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'id', 'family', 'genus', 'order', 'carbohydrates', 'protein', 'fat', 'calories', 'sugar']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # write the header of the file

            writer.writeheader()
            for fruit in fruits:
                row = {
                    'name': fruit['name'],
                    'id': fruit['id'],
                    'family': fruit['family'],
                    'genus': fruit['genus'],
                    'order': fruit['order'],
                    **fruit['nutritions']
                }
                writer.writerow(row)

# Examples

# fetch_and_export_to_csv(filename='example1.csv', family='Rosaceae', genus='Malus', to_db=True)
# fetch_and_export_to_csv(filename='example2.csv', family='Rosaceae', id_range=(1, 10))
# fetch_and_export_to_csv(filename='example3.csv', family='Rosaceae')
# fetch_and_export_to_csv(filename='example4.csv', genus='Malus')


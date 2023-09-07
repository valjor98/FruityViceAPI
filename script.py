import requests
import csv

# separate function to fetch a request
def fetch_fruits(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Received status code {response.status_code}")
        return []

def fetch_and_export_to_csv(filename='fruits.csv', family=None, genus=None, id_range=None):
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
    
    # If both family and genus are specified, take intersection. Else, take union
    if family and genus:
        fruits = [fruit for fruit in family_fruits if fruit in genus_fruits]
    else:
        fruits = family_fruits + genus_fruits
    
    # Filter by ID
    if id_range:
        fruits = [fruit for fruit in fruits if id_range[0] <= int(fruit['id']) <= id_range[1]]
    
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
fetch_and_export_to_csv(filename='example1.csv', family='Rosaceae', genus='Malus')
fetch_and_export_to_csv(filename='example2.csv', id_range=(1, 10))
fetch_and_export_to_csv(filename='example3.csv', family='Rosaceae')
fetch_and_export_to_csv(filename='example4.csv', genus='Malus')


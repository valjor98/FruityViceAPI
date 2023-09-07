import requests
import csv

def fetch_and_export_to_csv(filename='fruits.csv', family=None, genus=None):
    base_url = 'https://www.fruityvice.com'
    url = ""

    if family:
        url = f"{base_url}/api/fruit/family/{family}"
    elif genus:
        url = f"{base_url}/api/fruit/genus/{genus}"
    else:
        url = f"{base_url}/api/fruit/all"

    print("url: ", url)

    params = {}

    response = requests.get(url)
    print(response)
    
    if response.status_code == 200:
        fruits = response.json()

        # Exportar a CSV
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'id', 'family', 'genus', 'order', 'carbohydrates', 'protein', 'fat', 'calories', 'sugar']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
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
    else:
        print(f"Error: Received status code {response.status_code}")


fetch_and_export_to_csv(filename='rosaceae_fruits.csv', family='Rosaceae')

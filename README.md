# FruityViceAPI

## Description

This Python script fetches data from the FruityVice API and allows you to filter the fruits by family, genus, and/or ID. You can export the data to a CSV file or save it to a SQLite database.

## Requirements

- Python 3
- Requests library
- SQLite3 library
- CSV library

## How to Run

1. Open the terminal and navigate to the folder containing the Python script.
2. Run the script by executing `python script.py`

## Example Usages

- To save fruits from the family 'Rosaceae' and the genus 'Malus' to a database:
  ```python
  fetch_and_export_to_csv(filename='example1.csv', family='Rosaceae', genus='Malus', to_db=True)
  ```

- To save fruits from the family 'Rosaceae' with ID ranging from 1 to 10 to a CSV:
  ```python
  fetch_and_export_to_csv(filename='example2.csv', family='Rosaceae', id_range=(1, 10))
  ```

## Testing
The tests are implemented using Pytest BDD and Gherkins. You can run the tests using the following command:
```bash
python -m pytest
```

## FAQ

### How would you generate a CSV file for fruits from #11 to #20 (as if it were paginated)?

To do this, use the `id_range` parameter when calling the function like so:
```python
fetch_and_export_to_csv(filename='example.csv', id_range=(11, 20))
```

### If the API were intermittent, returning an HTTP 500 status, how would you handle it?

The current code checks the HTTP status and prints an error message if the status code is not 200.


### How would you save the information to a database?

The feature to save data to a SQLite database is already implemented in the code using the `save_to_db()` function. This function creates a table if it doesn't exist and inserts the fruit data into the table.

### What test scenarios would you add?

The current feature file contains test scenarios for fetching fruits by family and by genus. Additional test scenarios could include:

1. Fetching fruits by ID range.
2. Fetching fruits when both family and genus are specified.
3. Fetching fruits when the API returns an error.
4. Testing the database save functionality.
5. Testing the CSV export functionality.

More scenarios ar e included in the .featue file. 
